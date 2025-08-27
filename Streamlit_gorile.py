
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import cv2
import numpy as np
from collections import Counter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

st.set_page_config(page_title="Détection YOLOv8", layout="wide")

# ================================
# 1. Charger le modèle
# ================================
@st.cache_resource
def load_model():
    model = YOLO("D:/Nouveau dossier/hermanTPEE/best_yolov8s_gorilles.pt")  # ⚠️ adapter le chemin
    return model

model = load_model()

# ================================
# 2. Fonction pour générer un PDF
# ================================
def generate_pdf(report_data, filename="rapport_detection.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 800, "Rapport de détection YOLOv8")

    c.setFont("Helvetica", 12)
    y = 760
    for img_name, detections in report_data.items():
        c.drawString(50, y, f"Image : {img_name}")
        y -= 20
        if detections:
            for obj, count in detections.items():
                c.drawString(80, y, f"- {obj} : {count}")
                y -= 15
        else:
            c.drawString(80, y, "- Aucun objet détecté")
            y -= 15
        y -= 10

        if y < 100:  # nouvelle page si trop bas
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 760

    c.save()
    return filename

# ================================
# 3. Interface principale
# ================================

st.title("🔍 Détection d’objets avec YOLOv8")
st.sidebar.title("⚙️ Options")

mode = st.sidebar.radio("Choisir un mode :", ["Uploader des images", "Détection temps réel (Webcam)"])

# ================================
# Mode 1 : Batch upload
# ================================
if mode == "Uploader des images":
    st.subheader("📂 Uploader jusqu'à 100 images")
    uploaded_files = st.file_uploader("Choisir des images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_files:
        if len(uploaded_files) > 100:
            st.warning("⚠️ Vous avez uploadé plus de 100 images, seules les 100 premières seront traitées.")
            uploaded_files = uploaded_files[:100]

        cols = st.columns(3)  # afficher en grille
        report_data = {}

        for i, uploaded_file in enumerate(uploaded_files):
            # Sauvegarder temporairement
            image = Image.open(uploaded_file)
            tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
            image.save(tfile.name)

            # Détection
            results = model(tfile.name)
            res_plotted = results[0].plot()

            # Récupérer les classes détectées
            detections = [model.names[int(c)] for c in results[0].boxes.cls]
            counts = dict(Counter(detections))
            report_data[uploaded_file.name] = counts

            # Afficher résultat
            with cols[i % 3]:
                 st.image(res_plotted, caption=f"Résultat - {uploaded_file.name}", use_container_width=True)
        # Générer un rapport PDF
        pdf_file = generate_pdf(report_data)
        with open(pdf_file, "rb") as f:
            st.download_button("📥 Télécharger le rapport PDF", f, file_name="rapport_detection.pdf")

# ================================
# Mode 2 : Détection en temps réel
# ================================
elif mode == "Détection temps réel (Webcam)":
    st.subheader("🎥 Détection en temps réel via webcam")
    run = st.checkbox("Démarrer la caméra")

    FRAME_WINDOW = st.image([])

    cap = cv2.VideoCapture(0)  # 0 = webcam par défaut

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("⚠️ Impossible d'accéder à la caméra")
            break

        # Détection YOLO
        results = model(frame)
        res_plotted = results[0].plot()

        # Convertir BGR -> RGB pour Streamlit
        FRAME_WINDOW.image(res_plotted[:, :, ::-1])

    cap.release()
    cv2.destroyAllWindows()
