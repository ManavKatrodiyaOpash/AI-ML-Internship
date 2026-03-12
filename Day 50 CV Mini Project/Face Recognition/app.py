import streamlit as st
import face_recognition
import numpy as np
import cv2
import os
import tempfile
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av

st.set_page_config(page_title="Face Recognition System", layout="centered")

st.title("🧑 Face Recognition System")

# ======================
# Load Known Faces (CACHED)
# ======================
@st.cache_resource
def load_faces():

    known_encodings = []
    known_names = []

    for filename in os.listdir("known_faces"):

        if filename.endswith((".jpg",".png",".jpeg")):

            img = face_recognition.load_image_file(f"known_faces/{filename}")
            encoding = face_recognition.face_encodings(img)[0]

            known_encodings.append(encoding)
            known_names.append(os.path.splitext(filename)[0])

    return known_encodings, known_names


known_encodings, known_names = load_faces()

# ======================
# Face Recognition
# ======================
def recognize_faces(frame):

    small_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        distances = face_recognition.face_distance(known_encodings, face_encoding)

        name = "Unknown"

        if len(distances) > 0:

            best_match = distances.argmin()

            if distances[best_match] < 0.45:
                name = known_names[best_match]

        # scale back up
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),3)

        cv2.putText(frame,
                    name,
                    (left,top-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2)

    return frame


# ======================
# Webcam Processor
# ======================
class FaceProcessor(VideoProcessorBase):

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        img = recognize_faces(img)

        return av.VideoFrame.from_ndarray(img, format="bgr24")


# ======================
# UI Mode Selection
# ======================
mode = st.radio(
    "Select Mode",
    ["Upload Image","Upload Video","Capture Image","Live Webcam"]
)

# ======================
# Upload Image
# ======================
if mode == "Upload Image":

    uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

    if uploaded_file:

        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes,1)

        result = recognize_faces(img)

        st.image(result, channels="BGR")


# ======================
# Upload Video
# ======================
elif mode == "Upload Video":

    uploaded_video = st.file_uploader("Upload Video", type=["mp4","avi","mov"])

    if uploaded_video:

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)

        stframe = st.empty()

        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                break

            frame = recognize_faces(frame)

            stframe.image(frame, channels="BGR")

        cap.release()


# ======================
# Capture Image
# ======================
elif mode == "Capture Image":

    img_file = st.camera_input("Take a picture")

    if img_file:

        file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes,1)

        result = recognize_faces(frame)

        st.image(result, channels="BGR")


# ======================
# Live Webcam
# ======================
elif mode == "Live Webcam":

    webrtc_streamer(
    key="face-recognition",
    video_processor_factory=FaceProcessor,
    media_stream_constraints={"video": True, "audio": False},
    )