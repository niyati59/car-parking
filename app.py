import cv2
from deepface import DeepFace

path = r'C:\Users\pc\OneDrive\year\emmah.jpg'
img = cv2.imread(path)
results = DeepFace.analyze(img, actions="emotions")

print(results)