Duplicate Question Pairs Detector

A Machine Learning web application to detect if two questions are duplicates. Built with Python, Scikit-learn, and Streamlit, this project demonstrates advanced feature engineering, preprocessing, and a Random Forest classifier achieving 79% accuracy.

live demo: https://duplicate-question-pair-detection-bysatyam.streamlit.app/

Features

✅ Detects duplicate question pairs using machine learning

✅ Built with Random Forest Classifier for robust performance

✅ Advanced feature engineering including:

Token-based features (common words, first/last word matches)

Character-based features (min/max lengths, token counts)

Fuzzy string similarity scores (QRatio, WRatio, token sort/set ratios)

✅ Full preprocessing pipeline:

Text cleaning (lowercasing, stripping, tokenization)

Feature vector creation ready for ML model

✅ User-friendly Streamlit interface:

Enter two questions side-by-side

Click “Predict” to instantly see if questions are duplicates

Installation

Clone the repository:

git clone <your-repo-link>

cd duplicate-question-detector


Install dependencies:

pip install -r requirements.txt

Usage

Run the Streamlit app:

streamlit run app.py


Enter Question 1 and Question 2 in the text areas

Click Predict

The app will display “Duplicate” or “Not Duplicate”

Model Details

Algorithm: Random Forest Classifier

Accuracy: 79% on validation dataset

Features: Combination of token-based, character-based, and fuzzy matching features

Preprocessing: Full text cleaning and feature vectorization using custom helper functions

Folder Structure
Duplicate-Question-Detector/
│

├── app.py                 # Streamlit web app

├── helper.py              # Feature engineering & preprocessing

├── model.zip              # Trained Random Forest model (zipped)

├── cv.pkl                 # Count vectorizer

├── requirements.txt       # Project dependencies

└── STOPWORDS              # list of stopwords in english 

└── README.md              # Project documentation

Future Improvements

Experiment with deep learning models (LSTM, BERT) for better accuracy

Add multi-language support for questions

Deploy on cloud platforms for live usage


Author

Satyam Singh – BTech & Python ML Developer

Linkedin: https://www.linkedin.com/in/satyam-singh-61152a334





