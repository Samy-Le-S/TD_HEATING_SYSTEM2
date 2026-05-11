class Equipement:
    VALID_TYPES = ["Chaudiere", "Radiateur", "Pompe a chaleur", "Chauffe-eau"]
    def __init__(self, type_eq: str, annee_installation: int, puissance_kw: int):
        self.type_eq = type_eq 
        self.annee_installation = annee_installation 
        self.puissance_kw = puissance_kw 
def is_valid(self) -> bool:

        if self.type_eq not in self.VALID_TYPES:
            return False
        

        if not isinstance(self.annee_installation, int) or self.annee_installation <= 1995 or self.annee_installation == 2019:
            return False
            

        if not isinstance(self.puissance_kw, int) or not (1 <= self.puissance_kw <= 50):
            return False
            
        return True 

class Installation:
    def __init__(self, surface_m2: float, equipements: list[Equipement], zones: list[Zone]):
        self.surface_m2 = surface_m2 # [cite: 22]
        self.equipements = equipements # [cite: 22]
        self.zones = zones # [cite: 22]

    def is_valid(self) -> bool:

        if self.surface_m2 % 10 != 0 or self.surface_m2 >= 300:
            return False
            

        somme_surfaces_zones = sum(zone.surface_m2 for zone in self.zones)
        if somme_surfaces_zones != self.surface_m2:
            return False
            

        if any(zone.surface_m2 <= 0 for zone in self.zones):
            return False
            

        for zone in self.zones:
            if zone.equipement_associe not in self.equipements:
                return False
                
        return True
    

class Zone:
    def __init__(self, nom: str, surface_m2: float, equipement_associe: Equipement):
        self.nom = nom
        self.surface_m2 = surface_m2
        self.equipement_associe = equipement_associe