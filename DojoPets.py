#Ninja Class
class Ninja: 
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self 

    def bathe(self):
        self.pet.noise()
        return self

    def display_info(self):
        print("Pet Name: ", self.pet.name)
        print("Pet Type: ", self.pet.type)
        print("Pet Health: ", self.pet.health)
        print("Pet Energy: ", self.pet.energy)
        return self

# Pet Class
class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0 
        self.energy = 0 

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("BARK BARK")
        return self

# Creating Objects
lyla = Pet("Lyla", "Dog", "Sit") 
oger = Ninja("Oger", "Carrillo", lyla, "Bits", "Call of the Wild")

oger.walk()
oger.feed()
oger.bathe()
oger.display_info()


