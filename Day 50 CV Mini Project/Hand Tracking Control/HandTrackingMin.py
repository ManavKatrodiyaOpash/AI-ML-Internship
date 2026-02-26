import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    if not success:
        break
    
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgrgb)
    
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                
                if id == 4 or id == 8:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)
            
            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)
    
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

cap.release()
cv2.destroyAllWindows()