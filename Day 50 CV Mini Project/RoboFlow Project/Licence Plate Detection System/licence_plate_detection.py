import cv2
import numpy as np
from ultralytics import YOLO
import easyocr
import re
from collections import defaultdict, deque
 
# --- CONFIG & INITIALIZATION ---
INPUT_PATH = 'vehicle_video.mp4'
OUTPUT_PATH = 'output.mp4'
 
model = YOLO('best.pt') 
reader = easyocr.Reader(['en'], gpu=True) 
plate_pattern = re.compile(r'^[A-Z]{2}[0-9]{2}[A-Z]{3}$')
 
dict_char_to_int = {'O': '0', 'I': '1', 'Z': '2', 'S': '5', 'B': '8'}
dict_int_to_char = {'0': 'O', '1': 'I', '2': 'Z', '5': 'S', '8': 'B'}
 
def correct_format(text):
    if len(text) != 7: return None
    res = ""
    for i in range(7):
        char = text[i]
        if i in [0, 1, 4, 5, 6]: 
            res += dict_int_to_char.get(char, char) if char.isdigit() else char
        else: 
            res += dict_char_to_int.get(char, char) if not char.isdigit() else char
    return res
 
def recognize_plate(plate_crop):
    gray = cv2.cvtColor(plate_crop, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    resized = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    results = reader.readtext(resized)
    for (_, text, conf) in results:
        clean_text = text.upper().replace(" ", "")
        candidate = correct_format(clean_text)
        if candidate and plate_pattern.match(candidate):
            return candidate
    return None
 
# --- VIDEO SETUP ---
cap = cv2.VideoCapture(INPUT_PATH)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
 
# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Standard for .mp4
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (frame_width, frame_height))
 
stabilization_buffer = defaultdict(lambda: deque(maxlen=15))
frame_count = 0
 
try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        frame_count += 1
        if frame_count % 50 == 0: print(f"Processing frame {frame_count}...")
 
        results = model.track(frame, persist=True, verbose=False)
        for result in results:
            if result.boxes is None or result.boxes.id is None:
                continue
            boxes = result.boxes.xyxy.cpu().numpy().astype(int)
            ids = result.boxes.id.cpu().numpy().astype(int)
            confs = result.boxes.conf.cpu().numpy()
 
            for box, track_id, conf in zip(boxes, ids, confs):
                if conf < 0.3: continue
                x1, y1, x2, y2 = box
                plate_crop = frame[max(0, y1):min(frame_height, y2), 
                                   max(0, x1):min(frame_width, x2)]
                if plate_crop.size == 0: continue
                raw_text = recognize_plate(plate_crop)
                if raw_text:
                    stabilization_buffer[track_id].append(raw_text)
                if stabilization_buffer[track_id]:
                    votes = list(stabilization_buffer[track_id])
                    stable_text = max(set(votes), key=votes.count)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"ID {track_id}: {stable_text}", (x1, y1-10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
 
        # Save frame to output file instead of showing it
        out.write(frame)
 
finally:
    cap.release()
    out.release()
    print(f"Done! Video saved to {OUTPUT_PATH}")