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