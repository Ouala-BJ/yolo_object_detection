import gradio as gr
from object_detection import detect_objects

demo = gr.Interface(
    fn=detect_objects,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="numpy"),
    title="Détection d'objets avec YOLOv8"
)

if __name__ == "__main__":
    print("Démarrage de l'interface Gradio...")
    demo.launch(server_name="0.0.0.0", server_port=7860)
