import streamlit as st
import cv2
import numpy as np
import tempfile
import av
from ultralytics import YOLO
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

st.set_page_config(page_title="Helmet Detection System", layout="centered")

st.title("👷 Helmet Detection System")

# ======================
# Load YOLO model
# ======================
@st.cache_resource
def load_model():
    model = YOLO("best.pt")
    return model

model = load_model()

# ======================
# Detection Function
# ======================
def detect_helmet(frame):

    results = model(frame, conf=0.4)

    for r in results:
        for box in r.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            color = (0,255,0) if "helmet" in label.lower() else (0,0,255)

            cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)

            cv2.putText(
                frame,
                label,
                (x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

    return frame


# ======================
# Webcam Processor
# ======================
class HelmetProcessor(VideoProcessorBase):

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        img = detect_helmet(img)

        return av.VideoFrame.from_ndarray(img, format="bgr24")


# ======================
# Mode Selection
# ======================
mode = st.radio(
    "Select Mode",
    ["Upload Image", "Capture Image", "Upload Video", "Live Webcam"]
)

# ======================
# Upload Image
# ======================
if mode == "Upload Image":

    uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg", "avif", "webp"])

    if uploaded_file:

        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes,1)

        result = detect_helmet(img)

        st.image(result, channels="BGR")


# ======================
# Capture Image
# ======================
elif mode == "Capture Image":

    img_file = st.camera_input("Take a picture")

    if img_file is not None:

        file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes,1)

        result = detect_helmet(frame)

        st.image(result, channels="BGR")


# ======================
# Upload Video
# ======================
elif mode == "Upload Video":

    uploaded_video = st.file_uploader(
        "Upload Video",
        type=["mp4","avi","mov"]
    )

    if uploaded_video:

        temp_video = tempfile.NamedTemporaryFile(delete=False)
        temp_video.write(uploaded_video.read())

        cap = cv2.VideoCapture(temp_video.name)

        width = int(cap.get(3))
        height = int(cap.get(4))
        fps = cap.get(cv2.CAP_PROP_FPS)

        output_path = "helmet_output.mp4"

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_path,fourcc,fps,(width,height))

        stframe = st.empty()

        stop = st.button("Stop Processing")

        while cap.isOpened():

            ret,frame = cap.read()

            if not ret:
                break

            if stop:
                break

            frame = detect_helmet(frame)

            out.write(frame)

            stframe.image(frame,channels="BGR")

        cap.release()
        out.release()

        st.success("Processing finished / stopped")

        st.write("Saved output video:", output_path)


# ======================
# Live Webcam
# ======================
elif mode == "Live Webcam":

    webrtc_streamer(
        key="helmet-detection",
        video_processor_factory=HelmetProcessor,
        media_stream_constraints={"video": True, "audio": False},
    )