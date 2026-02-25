import face_recognition
import cv2
import os

known_encodings = []
known_names = []

for filename in os.listdir("known_faces"):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        img = face_recognition.load_image_file(f"known_faces/{filename}")
        encoding = face_recognition.face_encodings(img)[0]
        
        known_encodings.append(encoding)
        known_names.append(os.path.splitext(filename)[0])
    
print("loaded known faces:", known_names)

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error opening video")
    exit()

process_this_frame = True

while True:
    ret, frame = video.read()

    if not ret:
        break 

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    if process_this_frame:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame, model="hog")
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        names = []

        for face_encoding in face_encodings:

            # 🔥 Calculate distance first
            distances = face_recognition.face_distance(
                known_encodings, face_encoding
            )
            
            if len(distances) > 0:
                best_match_index = distances.argmin()
                
                if distances[best_match_index] < 0.45:
                    name = known_names[best_match_index]
                else:
                    name = "Unknown"
            else:
                name = "Unknown"  
            
            names.append(name)          

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name,
                    (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()