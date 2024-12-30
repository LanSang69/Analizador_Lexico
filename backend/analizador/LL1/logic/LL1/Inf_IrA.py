class InfoIrA:
    def __init__(self):
        self.Si = 0
        self.IrA_Sj = -1
        self.IrA_Simbolo = ""
        self.ConjuntoItems = ""
        self.existe = False

    def __eq__(self, value):
        return self.NumRegla == value.NumRegla and self.PosPunto == value.PosPunto
    
