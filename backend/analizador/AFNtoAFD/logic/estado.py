from . import transicion
class Estado:
    def __init__(self):
        self.idEdo = None
        self.transiciones = []
        self.EdoAcept = False
        self.token = 0
        self.countEdos = 0
    
    def __eq__(self, other):
        if isinstance(other, Estado):
            return (self.idEdo == other.idEdo and
                    self.transiciones == other.transiciones and
                    self.EdoAcept == other.EdoAcept and
                    self.token == other.token and
                    self.countEdos == other.countEdos)
        return False

    def __hash__(self):
        return hash((self.idEdo, tuple(self.transiciones), self.EdoAcept, self.token, self.countEdos))

    def init_data(self, idEdo, transiciones, EdoAcept, token, countEdos):
        self.idEdo = idEdo
        self.transiciones = transiciones
        self.EdoAcept = EdoAcept
        self.token = token
        self.countEdos = countEdos

    def init_edo(self, auxEdo):
        self.idEdo = auxEdo._idEdo
        self.transiciones = auxEdo._transiciones
        self.EdoAcept = auxEdo._EdoAcept
        self.token = auxEdo._token
        self.countEdos = auxEdo._countEdos

    def get_idEdo(self):
        return self.idEdo

    def set_idEdo(self, idEdo):
        self.idEdo = idEdo

    def get_transiciones(self):
        return self.transiciones

    def set_transiciones(self, transiciones):
        self.transiciones = transiciones

    def get_EdoAcept(self):
        return self.EdoAcept

    def set_EdoAcept(self, EdoAcept):
        self.EdoAcept = EdoAcept

    def get_token(self):
        return self.token

    def set_token(self, token):
        self.token = token

    def get_countEdos(self):
        return self.countEdos

    def set_countEdos(self, countEdos):
        self.countEdos = countEdos
   
    