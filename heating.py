import pymongo
from pymongo import MongoClient
from models import Equipement

# Connexion à la base de données
client = MongoClient(host="mongodb", port=27017)
db = client["heating_db"]
col = db["equipements"]

# Récupération de tous les équipements via pymongo
equipements_db = col.find()

print("--- Début de l'analyse des équipements ---")
invalides_trouves = 0

# Itération sur la collection
for eq_data in equipements_db:
    # On recrée l'objet Python à partir des données de la BDD
    eq = Equipement(
        type_eq=eq_data["type_eq"],
        annee_installation=eq_data["annee_installation"],
        puissance_kw=eq_data["puissance_kw"]
    )
    
    # Vérification de la validité
    if not eq.is_valid():
        invalides_trouves += 1
        print(f" DÉFAUT DÉTECTÉ (ID: {eq_data['_id']}) :")
        print(f"   Type: {eq.type_eq} | Année: {eq.annee_installation} | Puissance: {eq.puissance_kw} kW")

if invalides_trouves == 0:
    print(" Tous les équipements en base sont valides.")
else:
    print(f"\n Analyse terminée : {invalides_trouves} équipement(s) invalide(s) trouvé(s).")