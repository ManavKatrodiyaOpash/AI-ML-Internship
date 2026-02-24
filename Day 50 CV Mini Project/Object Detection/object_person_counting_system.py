import random
from ultralytics import YOLO
import cv2

model = YOLO("yolo26n.pt")

def get_color():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)

    c = (r, g, b)

    return c

videos = ["videos/home_burglary_video.mp4",
          "videos/man_woman_sitting.mp4",
          "videos/people_walking1.mp4",
          "videos/people_walking2.mp4",
          "videos/people_walking3.mp4",
          "videos/people_walking4.mp4",
          "videos/vehicles1.mp4",
          "videos/vehicles2.mp4",
          "videos/vehicles3.mp4"
          ]

labels_and_colors = {
    "person" : (0, 255, 0),
    "chair" : (255, 0, 0),
    "dining table" : (0, 0, 255),
    "couch" : get_color(),
    "cup" : get_color(),
    "potted plant" : get_color(),
    "laptop" : get_color(),
    "bird" : get_color(),
    "dog" : get_color(),
    "handbag" : get_color(),
    "backpack" : get_color(),
    "suitcase" : get_color(),
    "car" : get_color(),
    "bicycle" : get_color(),
    "motorcycle" : get_color(),
    "truck" : get_color(),
    "traffic light" : get_color(),
    "umbrella" : get_color(),
}

for video in videos:
    cap = cv2.VideoCapture(video)

    while True:
        ret, frame = cap.read()

        if not ret:
            break
        frame = cv2.resize(frame, (1280, 720))

        result = model(frame, conf = 0.3)

        counts = {cls : 0 for cls in labels_and_colors.keys()}

        for person in result:
            for box in person.boxes:
                cls_id = int(box.cls[0])
                label = model.names[cls_id]
                if label not in labels_and_colors.keys():
                    continue
                counts[label] += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                text = f"{label}: {counts[label]}"
                color = labels_and_colors[label]

                cv2.rectangle(frame, (x1, y1), (x2, y2), color=color, thickness=2)

                cv2.putText(frame,
                            text,
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale = 0.8,
                            color = (255, 255, 255),
                            thickness=2
                            )

        cv2.imshow("Person and Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()