import cv2
import pandas as pd
from datetime import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/model.yml")

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cam = cv2.VideoCapture(0)
attendance = {}

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.2, 5)

    for (x,y,w,h) in faces:
        id_, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        if confidence < 70:
            time = datetime.now().strftime("%H:%M:%S")
            attendance[id_] = time
            cv2.putText(img, f"ID: {id_}", (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        else:
            cv2.putText(img, "Unknown", (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow("Attendance", img)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()

df = pd.DataFrame(attendance.items(), columns=["Student ID", "Time"])
df.to_csv("attendance.csv", index=False)
print("Attendance saved")
