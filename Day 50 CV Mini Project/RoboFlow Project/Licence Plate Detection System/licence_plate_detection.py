import cv2
from ultralytics import YOLO
import easyocr
import re
import os
from collections import defaultdict, deque

model = YOLO("plate_best.pt")
reader = easyocr.Reader(["en"])

plate_pattern = re.compile(r"^[A-Z]{2}[0-9]{2}[A-Z]{3}$")


def correct_plate_format(ocr_text):
    mapping_num_to_alpha = {
        "0": "O",
        "1": "I",
        "5": "S",
        "8": "B"
    }
    mapping_alpha_to_num = {
        "O": "0",
        "I": "1",
        "Z": "2",
        "S": "5",
        "B": "8"
    }
    ocr_text = ocr_text.upper().replace(" ", "")
    if len(ocr_text) != 7:
        return ""

    corrected = []

    for i, ch in enumerate(ocr_text):
        if i < 2 or i >= 4:

            if ch.isdigit() and ch in mapping_num_to_alpha:
                corrected.append(mapping_num_to_alpha[ch])

            elif ch.isalpha():
                corrected.append(ch)

            else:
                return ""

        else:
            if ch.isalpha() and ch in mapping_alpha_to_num:
                corrected.append(mapping_alpha_to_num[ch])

            elif ch.isdigit():
                corrected.append(ch)

            else:
                return ""

    return "".join(corrected)

def recognise_plate(plate_crop):
    if plate_crop.size == 0:
        return ""

    gray = cv2.cvtColor(plate_crop, cv2.COLOR_BGR2GRAY)
    # Light contrast enhancement instead of binary threshold
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    plate_resize = cv2.resize(enhanced, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    try:
        ocr_result = reader.readtext(
                                    plate_resize,
                                    detail=0,
                                    allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                                )
        if len(ocr_result) > 0:
            candidate = correct_plate_format(ocr_result[0])
            if candidate and plate_pattern.match(candidate):
                return candidate

    except Exception as e:
        print(f"OCR Error: {e}")
        pass

    return ""

plate_history = defaultdict(lambda: deque(maxlen=10))
plate_final = {}

def get_box_id(x1, y1, x2, y2):
    # Divide by 15-20 for better stability than 10, but not too coarse
    return f"{int(x1/15)}_{int(y1/15)}_{int(x2/15)}_{int(y2/15)}"

def get_stable_plate(box_id, new_text):
    # Only add to history if text is valid (non-empty)
    if new_text:
        plate_history[box_id].append(new_text)
    
    # Get most common valid result from history
    if plate_history[box_id]:
        most_common = max(set(plate_history[box_id]), key=plate_history[box_id].count)
        plate_final[box_id] = most_common

    return plate_final.get(box_id, "")

def shrink_box(x1, y1, x2, y2, percent=0.08):
    """Shrink bounding box by percentage to remove padding"""
    w = max(1, x2 - x1)
    h = max(1, y2 - y1)
    shrink_x = int(w * percent)
    shrink_y = int(h * percent)
    return (x1 + shrink_x, y1 + shrink_y, max(x1 + shrink_x + 1, x2 - shrink_x), max(y1 + shrink_y + 1, y2 - shrink_y))

input_video = "vehicle_video.mp4"
output_video = "output_vehicle_video.mp4"

# Check if input video exists
if not os.path.exists(input_video):
    print(f"Error: {input_video} not found!")
    print(f"Available files: {os.listdir('.')}")
    exit(1)

cap = cv2.VideoCapture(input_video)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_video, fourcc,
                      cap.get(cv2.CAP_PROP_FPS),
                      (int(cap.get(3)), int(cap.get(4))))

# Confidence threshold - lower to catch more plates (0.30 for better recall)
conf_thresh = 0.30

frame_count = 0
detected_plates = set()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    detections_this_frame = 0

    results = model(frame, verbose=False)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            conf = float(box.conf.cpu().numpy()[0])
            if conf < conf_thresh:  # Skip low confidence detections
                continue

            detections_this_frame += 1
            x1, y1, x2, y2 = map(int, box.xyxy.cpu().numpy()[0])
            
            # Optional: shrink box to remove padding (set to None to disable)
            # Uncomment the next line to shrink boxes
            # x1, y1, x2, y2 = shrink_box(x1, y1, x2, y2, percent=0.10)
            
            plate_crope = frame[y1:y2, x1:x2]
            text = recognise_plate(plate_crope)

            box_id = get_box_id(x1, y1, x2, y2)
            stable_text = get_stable_plate(box_id, text)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=3)

            if plate_crope.size > 0:
                overlay_h, overlay_w = 150, 400
                plate_resized = cv2.resize(plate_crope, (overlay_w, overlay_h))

                oy1 = max(0, y1 - overlay_h - 40)
                ox1 = x1
                oy2, ox2 = oy1 + overlay_h, ox1 + overlay_w

                if oy2 <= frame.shape[0] and ox2 <= frame.shape[1]:
                    frame[oy1:oy2, ox1:ox2] = plate_resized

                    # Show text if available (current or stable)
                    display_text = stable_text if stable_text else text
                    if display_text:
                        detected_plates.add(display_text)
                        cv2.putText(
                            frame,
                            display_text,
                            (ox1, oy1 - 20),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1.5,
                            (0, 0, 0),
                            5
                        )
                        cv2.putText(
                            frame,
                            display_text,
                            (ox1, oy1 - 20),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1.5,
                            (255, 255, 255),
                            2
                        )
    
    out.write(frame)
    cv2.imshow("Annotated Video", frame)
    
    # Print progress occasionally
    if frame_count % 30 == 0:
        print(f"Frame {frame_count}: {detections_this_frame} plates detected this frame | Total unique plates: {len(detected_plates)}")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

# Print summary
print(f"\n=== Detection Summary ===")
print(f"Total frames processed: {frame_count}")
print(f"Unique plates detected: {len(detected_plates)}")
if detected_plates:
    print(f"Plates: {', '.join(sorted(detected_plates))}")
print(f"Output saved to: {output_video}")