import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

# Charger les données
data = pd.read_csv('data/SMSSpamCollection.txt', sep='\t', header=None, names=['label', 'message'])
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Préparer les données
X = data['message']
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convertir les messages en vecteurs TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Entraîner le modèle
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Évaluer le modèle
y_pred = model.predict(X_test_tfidf)
print(classification_report(y_test, y_pred))

# Sauvegarder le modèle et le vectorizer
with open('app/spam_model.pkl', 'wb') as model_file:
    pickle.dump((vectorizer, model), model_file)