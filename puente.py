class Puente:
    def __init__(self, inicioPuente, largoPuente):
        self.inicio=inicioPuente
        self.largo=largoPuente
    
    def dibujarPuente(self):
        print(' ' * self.inicio + '=' * self.largo)


