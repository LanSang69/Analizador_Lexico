import transicion
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
    # idEdo
    @property
    def id_edo(self):
        return self._idEdo

    @id_edo.setter
    def id_edo(self, idEdo):
        self._idEdo = idEdo

    # transiciones
    @property
    def transiciones(self):
        return self._transiciones

    @transiciones.setter
    def transiciones(self, transiciones):
        self._transiciones = transiciones

    # EdoAcept
    @property
    def edo_acept(self):
        return self._EdoAcept

    @edo_acept.setter
    def edo_acept(self, EdoAcept):
        self._EdoAcept = EdoAcept

    # token
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    # countEdos
    @property
    def count_edos(self):
        return self._countEdos

    @count_edos.setter
    def count_edos(self, countEdos):
        self._countEdos = countEdos

    