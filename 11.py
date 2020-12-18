class  SUNY:
    def __init__(self,DOG,CAT=None):
        self.DOG=DOG
        self.CAT= CAT
        
class SUNY_Container:
    def __init__(self):
        self.SUNY= None 
        
    def put(self,DOG,CAT):
        if self.SUNY is None:
            self.SUNY= SUNY(DOG,CAT)
        elif self.SUNY.DOG < DOG:
            self.SUNY= SUNY(DOG,CAT)
            
    def get (self):
        if self.SUNY is None:
            return None
        return self.SUNY.CAT
        
        
c1= SUNY_Container()
print(c1.get())
c1.put(1,'snow')
print(c1.get())
c1.put(2,'forest')
print(c1.get())
