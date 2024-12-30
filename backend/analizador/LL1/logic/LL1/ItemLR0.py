class ItemLR0:
    def __init__(self):
        self.NumRegla = -1
        self.PosPunto = -1

    def __eq__(self, value):
        return self.NumRegla == value.NumRegla and self.PosPunto == value.PosPunto
    
    def __hash__(self):
        return hash((self.NumRegla, self.PosPunto))

    def init(self, NumRegla, PosPunto):
        self.NumRegla = NumRegla
        self.PosPunto = PosPunto