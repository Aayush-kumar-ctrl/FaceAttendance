import cv2
import os

cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

user_id = input("Enter Student ID: ")
name = input("Enter Name: ")

path = f"dataset/{user_id}_{name}"
os.makedirs(path, exist_ok=True)

count = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        cv2.imwrite(f"{path}/{count}.jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow('Collecting Faces', img)
    if cv2.waitKey(1) == 27 or count >= 50:
        break

cam.release()
cv2.destroyAllWindows()
