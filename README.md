# TD_HEATING_SYSTEM2

BENAISSA Samy 20222548

Ajout du docker, vérifé avec le prof.
https://hub.docker.com/r/samy213/seed_mongo


Résultat de la q5 : 
TD_HEATING_SYSTEM2> docker exec -it td_heating_system2-heating-1 bash
56e56a901d72:/app# python heating.py
--- Début de l'analyse des équipements ---
 DÉFAUT DÉTECTÉ (ID: 6a01bb381b919bda11a8a910) :
   Type: Micro-onde | Année: 2021 | Puissance: 2 kW
 DÉFAUT DÉTECTÉ (ID: 6a01bb381b919bda11a8a911) :
   Type: Chauffe-eau | Année: 1990 | Puissance: 15 kW
 DÉFAUT DÉTECTÉ (ID: 6a01bb381b919bda11a8a912) :
   Type: Chaudiere | Année: 2019 | Puissance: 30 kW
 DÉFAUT DÉTECTÉ (ID: 6a01bb381b919bda11a8a913) :
   Type: Radiateur | Année: 2023 | Puissance: 60 kW
 DÉFAUT DÉTECTÉ (ID: 6a01bb381b919bda11a8a914) :
   Type: Pompe a chaleur | Année: 2021 | Puissance: 0 kW

 Analyse terminée : 5 équipement(s) invalide(s) trouvé(s).
56e56a901d72:/app# exit