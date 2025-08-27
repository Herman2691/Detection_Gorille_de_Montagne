# DetectGorilleM > 2025-08-16 9:24am
# 🦍 Reconnaissance et classification des gorilles avec YOLOv8s

## 📘 Contexte
Ce projet de recherche s’inscrit dans le domaine de la **vision par ordinateur**.  
Il vise à développer un système de reconnaissance automatique des gorilles et à distinguer spécifiquement les **gorilles de montagne**.  
L’accent est mis sur cette espèce particulière, considérée comme menacée.  

## 🧩 Méthodologie
- Les données ont été **annotées à l’aide de Roboflow**, afin d’assurer une préparation adaptée à l’entraînement du modèle.  
- Un modèle de détection basé sur **YOLOv8s** a été entraîné pour reconnaître les différentes classes (gorilles de montagne, autres gorilles, autres animaux).  
- Une interface interactive a été développée avec **Streamlit** pour visualiser et tester les résultats en temps réel.  

## 🛠️ Technologies utilisées
- **Python**  
- **YOLOv8s (Ultralytics)**  
- **Roboflow** (annotation et gestion du dataset)  
- **Streamlit** (interface de déploiement)  
- **OpenCV, NumPy, Pandas, Matplotlib**  

## 📂 Organisation du projet
- `data/` → Images et annotations (Roboflow)  
- `notebooks/` → Expérimentations et entraînements du modèle  
- `app/` → Code Streamlit pour le déploiement interactif  
- `results/` → Prédictions et visualisations  

## 🚀 Résultats
- Capacité à **détecter et classifier les gorilles** dans différentes images.  
- Mise en évidence de la distinction entre les **gorilles de montagne** et les autres classes.  
- Prototype fonctionnel utilisable via une **interface web simple (Streamlit)**.  

## 🌍 Perspectives
- Améliorer les performances en entraînant le modèle sur un dataset plus large et plus diversifié.  
- Intégrer la reconnaissance en **temps réel (vidéo/caméra)**.  
- Étendre l’application à d’autres espèces menacées.  

## 👤 Auteur
- **Kandolo Herman**  
Étudiant à l’**Institut Francophone International (IFI – UOI)**  
Passionné par l’IA, le Machine Learning et la Vision par Ordinateur.  
