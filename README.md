# Flask Application for Automatic Text Summarization

Cette application Flask permet de télécharger des fichiers PDF, DOCX ou TXT et de générer automatiquement un résumé du contenu de ces fichiers en utilisant des modèles de résumé basés sur la bibliothèque `transformers` de Hugging Face.

## Fonctionnalités

- **Téléchargement de fichiers** : Les utilisateurs peuvent télécharger des fichiers PDF, DOCX ou TXT via l'interface web.
- **Extraction de texte** : Le texte est extrait des fichiers PDF et DOCX à l'aide de `pdfminer` et `python-docx`.
- **Résumé automatique** : Le texte extrait est résumé à l'aide de deux modèles de summarization : BART (`facebook/bart-large-cnn`) et mT5 (`csebuetnlp/mT5_multilingual_XLSum`).

## Dépendances

- `Flask` : Cadre de travail web léger pour Python.
- `pdfminer` : Outil pour extraire du texte des fichiers PDF.
- `python-docx` : Bibliothèque pour travailler avec des documents Word.
- `transformers` : Bibliothèque de Hugging Face pour les modèles de NLP (Natural Language Processing).

## Structure du Code

- **Initialisation de l'application Flask** : L'application Flask est initialisée avec un dossier de téléchargement configuré.
- **Chargement des modèles** : Deux modèles de summarization (BART et mT5) sont initialisés pour générer des résumés.
- **Fonctions d'extraction de texte** :
  - `read_pdf(file_path)` : Extrait le texte d'un fichier PDF.
  - `read_word(file_path)` : Extrait le texte d'un fichier DOCX.
- **Fonction de résumé** :
  - `summarize_file(file_path)` : Extrait le texte du fichier téléchargé et génère des résumés en utilisant les modèles BART et mT5.
- **Routes Flask** :
  - `'/'` : Affiche la page d'accueil avec un formulaire de téléchargement de fichier.
  - `'/upload'` : Gère le téléchargement de fichiers et renvoie les résumés générés.

## Utilisation

1. Clonez le dépôt et installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Créez le dossier de téléchargement si nécessaire :
   ```bash
   mkdir uploads
   ```
3. Lancez l'application Flask :
   ```bash
   python app.py
   ```
4. Accédez à l'application via un navigateur web à l'adresse `http://127.0.0.1:5000/` et téléchargez un fichier pour obtenir son résumé.

## Remarques

- Cette application est conçue pour fonctionner avec des fichiers de format PDF, DOCX et TXT.
- Assurez-vous que les modèles BART et mT5 sont téléchargés correctement lors de l'initialisation de la pipeline.
