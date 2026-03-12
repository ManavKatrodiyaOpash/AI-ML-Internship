import streamlit as st
import cv2
import numpy as np
import tempfile
import av
import easyocr
import re
from ultralytics import YOLO
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

st.set_page_config(page_title="License Plate Detection", layout="centered")

st.title("🚗 License Plate Detection System")

# ======================
# Load Models (cached)
# ======================
@st.cache_resource
def load_models():
    model = YOLO("best.pt")
    reader = easyocr.Reader(['en'], gpu=False)
    return model, reader

model, reader = load_models()

plate_pattern = re.compile(r'^[A-Z]{2}[0-9]{2}[A-Z]{3}$')

dict_char_to_int = {'O': '0', 'I': '1', 'Z': '2', 'S': '5', 'B': '8'}
dict_int_to_char = {'0': 'O', '1': 'I', '2': 'Z', '5': 'S', '8': 'B'}

# ======================
# OCR correction
# ======================
def correct_format(text):

    if len(text) != 7:
        return None

    res = ""

    for i in range(7):

        char = text[i]

        if i in [0,1,4,5,6]:
            res += dict_int_to_char.get(char,char) if char.isdigit() else char
        else:
            res += dict_char_to_int.get(char,char) if not char.isdigit() else char

    return res


# ======================
# Plate recognition
# ======================
def recognize_plate(plate_crop):

    gray = cv2.cvtColor(plate_crop, cv2.COLOR_BGR2GRAY)

    _,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    resized = cv2.resize(thresh,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

    results = reader.readtext(resized)

    for (_,text,conf) in results:

        clean = text.upper().replace(" ","")

        candidate = correct_format(clean)

        if candidate and plate_pattern.match(candidate):
            return candidate

    return None


# ======================
# Detection function
# ======================
def detect_plate(frame):

    results = model(frame)

    for r in results:

        for box in r.boxes:

            x1,y1,x2,y2 = map(int,box.xyxy[0])

            crop = frame[y1:y2,x1:x2]

            text = recognize_plate(crop)

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

            if text:
                cv2.putText(
                    frame,
                    text,
                    (x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2
                )

    return frame


# ======================
# Webcam processor
# ======================
class PlateProcessor(VideoProcessorBase):

    def recv(self,frame):

        img = frame.to_ndarray(format="bgr24")

        img = detect_plate(img)

        return av.VideoFrame.from_ndarray(img,format="bgr24")


# ======================
# Mode selection
# ======================
mode = st.radio(
    "Select Mode",
    ["Upload Video","Live Webcam"]
)


# ======================
# Upload Video
# ======================
if mode == "Upload Video":

    uploaded_video = st.file_uploader("Upload Video", type=["mp4","avi","mov"])

    if uploaded_video:

        temp_video = tempfile.NamedTemporaryFile(delete=False)
        temp_video.write(uploaded_video.read())

        cap = cv2.VideoCapture(temp_video.name)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        output_path = "output_video_streamlit.mp4"

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        stframe = st.empty()

        stop_button = st.button("Stop Processing")

        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                break

            if stop_button:
                break

            frame = detect_plate(frame)

            out.write(frame)

            stframe.image(frame, channels="BGR")

        cap.release()
        out.release()

        st.success("Processing stopped / completed")

        st.write("Output video saved as:", output_path)

# ======================
# Live Webcam
# ======================
elif mode == "Live Webcam":

    webrtc_streamer(
        key="plate-detection",
        video_processor_factory=PlateProcessor,
        media_stream_constraints={"video":True,"audio":False},
    )