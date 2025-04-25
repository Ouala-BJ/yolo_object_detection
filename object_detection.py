from ultralytics import YOLO
import numpy as np

# Charger le modèle une seule fois
model = YOLO("yolo11n.pt")

def detect_objects(image):
    results = model(image)
    return results[0].plot()
