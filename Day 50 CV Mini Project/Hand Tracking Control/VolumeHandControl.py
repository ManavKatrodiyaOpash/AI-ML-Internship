import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math

from pycaw.pycaw import AudioUtilities

devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume
volrange = volume.GetVolumeRange() # min = -63.5, max = 0,
min_vol = volrange[0]
max_vol = volrange[1]

wCam = 640
hCam = 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
vol = 0
volBar = 400
volPer = 0

detector = htm.HandDetector(detectionCon = 0.7)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    success, img = cap.read()
    if not success:
        break
    detector.findhands(img)
    lmlist = detector.findposition(img, draw = False)
    if len(lmlist) !=0:
        # print(lmlist[4], lmlist[8])
        
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3, cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
        
        length = math.hypot(x2 - x1, y2 - y1)
        
        vol = np.interp(length, [20, 100], [min_vol, max_vol])
        volBar = np.interp(length, [20, 100], [400, 150])
        volPer = np.interp(length, [20, 100], [0, 100])
        # print(length, vol)
        volume.SetMasterVolumeLevel(vol, None)
        
        if length < 20:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
        
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(
            img = img, 
            text = f"{int(volPer)} %",
            org = (40, 450), 
            fontFace = cv2.FONT_HERSHEY_COMPLEX, 
            fontScale = 1, 
            color = (255, 0, 0), 
            thickness = 2
        )
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.putText(
            img = img, 
            text = f"FPS: {int(fps)}",
            org = (20, 50), 
            fontFace = cv2.FONT_HERSHEY_PLAIN, 
            fontScale = 2, 
            color = (255, 0, 0), 
            thickness = 3
        )
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()