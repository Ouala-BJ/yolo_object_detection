FROM python:3.10-slim

WORKDIR /app

# Dépendances système pour OpenCV
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# Installer les dépendances Python
RUN pip install --no-cache-dir ultralytics gradio

# Copier le code
COPY . .

EXPOSE 7860

CMD ["python", "app.py"]
