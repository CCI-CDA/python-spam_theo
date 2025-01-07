from fastapi import FastAPI, Query
import pickle

app = FastAPI()

# Charger le modèle et le vectorizer
with open('app/spam_model.pkl', 'rb') as model_file:
    vectorizer, model = pickle.load(model_file)

@app.get("/check")
def check_message(message: str = Query(..., description="Message to classify")):
    vectorized_message = vectorizer.transform([message])
    prediction = model.predict(vectorized_message)[0]
    return {"resp": bool(prediction)}

@app.get("/")
def root():
    return {"message": "Bienvenue dans l'API de classification de spam. Utilisez /check avec un message pour classifier."}