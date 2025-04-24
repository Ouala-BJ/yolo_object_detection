from ultralytics import YOLO
import gradio as gr
from PIL import Image

model = YOLO("yolo11n.pt")  # Charger le modèle pré-entraîné

def detect_objects(image):
    results = model(image)
    return results[0].plot()  # Retourne l'image avec les détections superposées

demo = gr.Interface(
    fn=detect_objects,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="numpy"),
    title="Détection d'objets avec YOLOv8"
)

if __name__ == "__main__":
    print("Starting Gradio interface...")
    demo.launch(server_name="0.0.0.0", server_port=7860)