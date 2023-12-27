'''
    The Below code is to see Abstarction in
    Python. 
    And as it is clearly stated in pyhton there
    is no Real abstraction.
    That means there is no private and public keywrods
    that limit access to attributes as in another
    Programming languages.
    So The pyhton community has a convention
    that says to put a underscore before an attribute that
    you dont want to be accessed or chnaged.
    FOr_example: _name or _func and so on.
'''
class practice:
    def __init__(self, name):
        self._name = name
        
    def runner(self, name):
        print(f"{self.name}")
        
obj = practice("Eliyas")
obj.name = "Not you"
print(obj._name)