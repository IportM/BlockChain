# Fichier: simulation.py
import requests
import json

# 1. On définit la transaction
new_transaction = {
    "sender": "Alice",
    "recipient": "Bob",
    "amount": 50
}

print("Envoi de la transaction au serveur...")

try:
    # 2. On l'envoie au serveur qui tourne DEJA
    response = requests.post('http://127.0.0.1:5000/transactions/new', json=new_transaction)
    
    print("Réponse du serveur :")
    print(response.status_code)
    print(response.text)
except Exception as e:
    print(f"Erreur : Le serveur est-il bien lancé ?\n{e}")

