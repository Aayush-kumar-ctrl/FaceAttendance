import cv2
import os
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = []
ids = []

for folder in os.listdir("dataset"):
    user_id = int(folder.split("_")[0])
    path = os.path.join("dataset", folder)

    for image in os.listdir(path):
        img = cv2.imread(os.path.join(path, image), cv2.IMREAD_GRAYSCALE)
        faces.append(img)
        ids.append(user_id)

recognizer.train(faces, np.array(ids))
os.makedirs("trainer", exist_ok=True)
recognizer.save("trainer/model.yml")

print("Model trained successfully")
