import streamlit as st
import joblib
import numpy as np

# Charger le modèle
model = joblib.load('model_save.pkl')

# Définir la fonction de prédiction
def predict(transaction_data):
    prediction = model.predict([transaction_data])
    return prediction[0]

# Interface utilisateur Streamlit
st.title("Détection de Transactions Frauduleuses")

# Créer des champs pour les données de la transaction
st.header("Entrez les détails de la transaction")

# Supposons que la transaction comporte des features comme 'amount', 'time', etc.
a1 = st.number_input("Distance de la maison", min_value=0.0, max_value=10000.0, value=0.0, step=0.01)
a2 = st.number_input("Distance depuis la dernière transaction", min_value=0.0, max_value=100000.0, value=0.0, step=0.01)
a3 = st.number_input("rapport au prix d'achat médian", min_value=0.0, max_value=10000.0, value=0.0, step=0.01)
aa4 = st.radio("Est ce un détaillant régulier ?", ["oui", "non"])
if(aa4 == "oui"):
    a4 = 1
elif(aa4 == "non"):
    a4 = 0

aa5 = st.radio("Est ce une puce usagée ?", ["oui", "non"])
if(aa5 == "oui"):
    a5 = 1
elif(aa5 == "non"):
    a5 = 0

aa6 = st.radio("Le Numéro de broche a t-il été utilisé ?", ["oui", "non"])
if(aa6 == "oui"):
    a6 = 1
elif(aa6 == "non"):
    a6 = 0

aa7 = st.radio("Est ce une commande en ligne ?", ["oui", "non"])
if(aa7 == "oui"):
    a7 = 1
elif(aa7 == "non"):
    a7 = 0

# Ajoute d'autres champs nécessaires en fonction de tes features
# Par exemple:
# age = st.number_input("Âge du titulaire de la carte", min_value=0, max_value=120, value=30)
# category = st.selectbox("Catégorie de transaction", ["A", "B", "C", "D"])

# Créer un bouton pour lancer la prédiction
if st.button("Prédire"):
    # Rassembler les données de la transaction
    transaction_data = np.array([a1, a2, a3, a4, a5, a6, a7])  # Ajoute les autres champs ici, par ex. [amount, time, age, category]

    # Effectuer la prédiction
    prediction = model.predict(transaction_data.reshape(1, 7))
    
    # Afficher le résultat
    if prediction == 1:
        st.error("Transaction Frauduleuse Détectée!")
    else:
        st.success("Transaction Valide.")

# Pour lancer l'application Streamlit, utilise la commande suivante dans le terminal :
# streamlit run app.py
