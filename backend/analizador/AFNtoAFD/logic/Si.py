class Si:
    def __init__(self):
        self.id = 0
        self.S = []
        self.accept = False

    def __eq__(self, other):
        if isinstance(other, Si):
            return self.S == other.S
    
    def init_data(self, id, S):
        self.id = id
        self.S = S
    
    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id
    
    def set_S(self, S):
        self.S = S

    def get_S(self):
        return self.S

    def set_accept(self, accept):
        self.accept = accept

    def get_accept(self):
        return self.accept
    