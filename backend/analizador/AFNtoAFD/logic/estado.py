class Estado:
    def __init__(self):
        self._idEdo = 0
        self._transiciones = []
        self._EdoAcept = False
        self._token = 0
        self._countEdos = 0

    @classmethod
    def init_data(cls, idEdo, transiciones, EdoAcept, token, countEdos):
        estado = cls() 
        estado._idEdo = idEdo
        estado._transiciones = transiciones
        estado._EdoAcept = EdoAcept
        estado._token = token
        estado._countEdos = countEdos
        return estado

    @classmethod
    def init_edo(cls, auxEdo):
        estado = cls() 
        estado._idEdo = auxEdo._idEdo
        estado._transiciones = auxEdo._transiciones
        estado._EdoAcept = auxEdo._EdoAcept
        estado._token = auxEdo._token
        estado._countEdos = auxEdo._countEdos
        return estado
    
    