import cv2
import mediapipe as mp
import time

class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode = self.mode, max_num_hands = self.maxHands,
                                        min_detection_confidence = self.detectionCon, 
                                        min_tracking_confidence = self.trackCon
                                        )
        self.mpDraw = mp.solutions.drawing_utils
    
    def findhands(self, img, draw = True):
        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgrgb)
    
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS)
        
        return img
    
    def findposition(self, img, handNo = 0, draw = True):
        
        lmlist = []
        
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id, cx, cy])
            
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
        
        return lmlist

def main():
    pTime = 0
    cTime = 0        
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    
    while True:
        success, img = cap.read()
        
        if not success:
            break
        
        img = detector.findhands(img)
        lmlist = detector.findposition(img)
        
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

if __name__ == "__main__":
    main()