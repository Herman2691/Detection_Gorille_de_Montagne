 
 Reconnaissance de Gorilles de Montagne avec YOLOv8s 
  
Objectif du projet 0. Description du projet 
Ce modèle permet la détection automatique des gorilles à partir d’images, en identifiant immédiatement s’il s’agit d’un gorille de montagne, d’un autre type de gorille, ou d’un animal non gorille. 
Nous avons défini trois classes pour l’entraînement : 
•	Gorille de montagne 
•	Autres gorilles 
•	Non gorilles 
L’objectif principal est de contribuer à la conservation de la faune sauvage, en facilitant le suivi des espèces à partir de données visuelles. 
Le modèle repose sur YOLOv8s, entraîné sur un jeu de données annoté et enrichi par augmentation, puis intégré dans une application Streamlit pour une inférence en temps réel. 
 
 
1.	Modèle & Entraînement 
•	Modèle : YOLOv8s (Ultralytics 8.3.174) 
•	Framework : PyTorch 
•	Matériel : Entraînement sur CPU uniquement (Intel i5-6200U) 
•	Nombre d’époques : 100 • 	Pipeline :  
o 	Annotation : Roboflow o 	Prétraitement : redimensionnement, normalisation o 	Augmentation de données : rotation, flip, contraste, teinte o 	Entraînement → Évaluation → Déploiement Streamlit 
 
2.	Jeu de données 
•	Images initiales : 3 270 • 	Répartition :  
o	Entraînement : 80 % o 	Validation : 10 % o 	Test : 10 % 
•	Après augmentation : 6 736 images utilisées pour l’entraînement • 	Classes :  
o	Gorille de Montagne o 	Autres Gorilles o 	Autres Animaux 
•	Instances (validation) : 327 
•	Images de validation : 291 
 
3.	Résultats de performance 
Classe 	Précision 	Rappel 	F1-score 
Gorille de Montagne 	0.928 	0.926 	0.927 
Autres Gorilles 	0.912 	0.934 	0.923 
Autres Animaux 	0.831 	0.800 	0.815 
Métriques globales : 
•	mAP50 : 0.918 
•	mAP50–95 : 0.625 
•	Précision globale : 0.89 • 	Rappel global : 0.887 
4.	Déploiement 
• 	Application Streamlit : interface d’inférence en temps réel • 	Fonctionnalités :  
o 	Téléversement d’image o 	Détection instantanée o 	Affichage des classes et scores de confiance o 	Encadrés visuels (bounding boxes) 
 
🧠 Ce que ce projet démontre 
•	Détection personnalisée avec YOLOv8s 
•	Prétraitement et augmentation de données 
•	Évaluation avec mAP et métriques par classe 
•	Déploiement en temps réel avec Streamlit 
•	Faisabilité d’un entraînement sur CPU pour des modèles légers 

 
 
 
   
 
 
 
 
 
