import streamlit as st
import cv2
import time
import av
import HandTrackingModule as htm
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

st.set_page_config(page_title="Hand Tracking System", layout="centered")

st.title("✋ Hand Tracking with Webcam")

st.write("Move your hand in front of the camera to track hand landmarks.")

# ======================
# Video Processor
# ======================
class HandTrackingProcessor(VideoProcessorBase):

    def __init__(self):
        self.detector = htm.HandDetector()
        self.pTime = 0

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        img = self.detector.findhands(img)
        lmlist = self.detector.findposition(img, draw=False)

        if len(lmlist) != 0:
            # example: print thumb position
            thumb = lmlist[4]
            cv2.putText(
                img,
                f"Thumb: {thumb[1]}, {thumb[2]}",
                (10,120),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (255,0,255),
                2
            )

        # FPS calculation
        cTime = time.time()
        fps = 1 / (cTime - self.pTime) if self.pTime != 0 else 0
        self.pTime = cTime

        cv2.putText(
            img,
            f"FPS: {int(fps)}",
            (10,70),
            cv2.FONT_HERSHEY_PLAIN,
            3,
            (255,0,255),
            2
        )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


# ======================
# Webcam Stream
# ======================
webrtc_streamer(
    key="hand-tracking",
    video_processor_factory=HandTrackingProcessor,
    media_stream_constraints={"video": True, "audio": False},
)