import cv2
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0        
cap = cv2.VideoCapture(0)
detector = htm.HandDetector()

while True:
    success, img = cap.read()
    
    if not success:
        break
    
    img = detector.findhands(img)
    lmlist = detector.findposition(img, draw = False)
    
    if len(lmlist) != 0:
        print(lmlist[4])        
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.putText(
        img = img, 
        text = str(int(fps)), 
        org = (10, 70), 
        fontFace = cv2.FONT_HERSHEY_PLAIN, 
        fontScale = 3, 
        color = (255, 0, 255), 
        thickness = 2
    )

    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break