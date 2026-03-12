import streamlit as st
import cv2
import tempfile
import random
import av
from ultralytics import YOLO
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
# from object_person_counting_system import labels_and_colors

st.set_page_config(page_title="Object Detection System", layout="centered")

st.title("🚶 Object & Person Detection System")

# ======================
# Load YOLO Model
# ======================
@st.cache_resource
def load_model():
    model = YOLO("yolo26n.pt")
    return model

model = load_model()

# ======================
# Color generator
# ======================
def get_color():
    return (
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
    )

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
    "cell phone" : get_color(),
    "donut" : get_color(),
}

# ======================
# Detection Function
# ======================
def detect_objects(frame):

    frame = cv2.resize(frame,(1280,720))

    result = model(frame, conf=0.3)

    counts = {cls:0 for cls in labels_and_colors.keys()}

    for r in result:
        for box in r.boxes:

            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            if label not in labels_and_colors:
                continue

            counts[label] += 1

            x1,y1,x2,y2 = map(int,box.xyxy[0])

            color = labels_and_colors[label]

            text = f"{label}: {counts[label]}"

            cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)

            cv2.putText(
                frame,
                text,
                (x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,255,255),
                2
            )

    return frame


# ======================
# Webcam Processor
# ======================
class YOLOProcessor(VideoProcessorBase):

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        img = detect_objects(img)

        return av.VideoFrame.from_ndarray(img, format="bgr24")


# ======================
# Mode Selection
# ======================
mode = st.radio(
    "Select Mode",
    ["Upload Video", "Live Webcam"]
)

# ======================
# Upload Video
# ======================
if mode == "Upload Video":

    uploaded_video = st.file_uploader(
        "Upload Video",
        type=["mp4","avi","mov"]
    )

    if uploaded_video:

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)

        stframe = st.empty()

        while cap.isOpened():

            ret,frame = cap.read()

            if not ret:
                break

            frame = detect_objects(frame)

            stframe.image(frame,channels="BGR")

        cap.release()


# ======================
# Live Webcam
# ======================
elif mode == "Live Webcam":

    webrtc_streamer(
        key="yolo-detection",
        video_processor_factory=YOLOProcessor,
        media_stream_constraints={"video": True, "audio": False},
    )