import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("video.mp4")

unique_ids = set()
while True:
    ret, frame = cap.read()

    result = model.track(frame, classes=[0], persist=True, verbose=False)
    annotated_frame = result[0].plot()
    reduced_frame = cv2.resize(annotated_frame, None, fx=0.25, fy=0.25)

    if result[0].boxes and result[0].boxes.id is not None:
        ids = result[0].boxes.id.numpy()

        for oid in ids:
            unique_ids.add(oid)

        cv2.putText(reduced_frame, f"Count : {len(unique_ids)}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("object tracking", reduced_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()