import face_recognition
import cv2

videos = ["face_recognize.mp4", "face_recognize2.mp4"]

known_image = face_recognition.load_image_file("Me.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

person_name = "Manav"

for v in videos:
    video = cv2.VideoCapture(v)

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
                face_distance = face_recognition.face_distance(
                    [known_encoding], face_encoding
                )[0]

                # 🔥 Strict threshold
                if face_distance < 0.45:
                    name = person_name
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