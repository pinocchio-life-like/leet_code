class User():
    def sign_in(self):
        print('logged in')
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def attack(self):
        print(f'Attacking with power of {self.power}')
    
class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        
    def check_arrows(self):
        print(f'{self.arrows} arrows left')
    
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        self.name = name
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)
        
hb1 = HybridBorg("Eliyas", 100, 500)

# Inheritance from the Upper Class
print(hb1.sign_in()) 

# Inheritance from Wizard class
print(hb1.attack())

# Inheritance from the Archer Class
print(hb1.check_arrows())

