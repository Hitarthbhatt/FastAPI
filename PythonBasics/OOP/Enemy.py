class Enemy:
    def __init__(self, name, attackPower, health = 10):
        ## private variable by adding __ before variable name
        self.__name = name
        
        ## Public variables
        self.attackPower = attackPower
        self.health = health

    def talk(self):
        print("I am " + self.__name + " be preparedd to fight")
        
    def attack(self):
        print(f"{self.__name} attacking you with {self.attackPower} power")
        
    def walk(self):
        print(f"{self.__name} move close to you")
