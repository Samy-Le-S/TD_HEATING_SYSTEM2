import pymongo
from pymongo import MongoClient
from models import Equipement 


client = MongoClient(host="mongodb", port=27017)
db = client["heating_db"]
col = db["equipements"]

col.delete_many({})


equipements_a_inserer = [
    # --- DONNÉES VALIDES ---
    Equipement("Chaudiere", 2020, 25),
    Equipement("Pompe a chaleur", 2022, 10),
    Equipement("Radiateur", 2015, 5),
    
    # --- DONNÉES INVALIDES ---
    # Invalide : Mauvais type
    Equipement("Micro-onde", 2021, 2),
    # Invalide : Année <= 1995 ou égale à 2019
    Equipement("Chauffe-eau", 1990, 15),
    Equipement("Chaudiere", 2019, 30),
    # Invalide : Puissance hors limites (1 - 50)
    Equipement("Radiateur", 2023, 60),
    Equipement("Pompe a chaleur", 2021, 0)
]

print("Début du peuplement de la base de données...")

for eq in equipements_a_inserer:

    equipement_dict = {
        "type_eq": eq.type_eq,
        "annee_installation": eq.annee_installation,
        "puissance_kw": eq.puissance_kw
    }
    
    res = col.insert_one(equipement_dict)
    

    statut = "Valide" if eq.is_valid() else "Invalide"
    print(f"[{statut}] Équipement inséré avec l'ID: {res.inserted_id}")

print("Peuplement terminé avec succès !")