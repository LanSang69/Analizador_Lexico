class Renglon:
    def __init__(self):
        self.movimientos = [-1] * 258
    
    def SetOrigin(self, idEdo):
        self.movimientos[0] = idEdo
    
    def Assign(self, ascii, id):
        index = ord(ascii)
        self.movimientos[index] = id

    def setToken(self, token):
        self.movimientos[257] = token
