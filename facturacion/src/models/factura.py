class Factura:
    
    def __init__ (self, cliente):
        self.__cliente = cliente
        
    def __str__(self):
        return f'{self.__cliente}'
    
    
    
    