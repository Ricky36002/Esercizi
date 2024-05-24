#Riccardo Russo

class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
    
    def area(self):
        return self.height * self.width
    
    def growth_area(self):
        return (self.height * 1.02) * (self.width * 1.02) - self.area()
    
    def feed(self):
        self.health = min(100, self.health + 1)
        self.height *= 1.02
        self.width *= 1.02

class Fence:
    def __init__(self, area, temperature, habitat):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
    
    def available_area(self):
        occupied_area = sum(animal.area() for animal in self.animals)
        return self.area - occupied_area
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def remove_animal(self, animal):
        self.animals.remove(animal)
    
    def clean(self):
        occupied_area = sum(animal.area() for animal in self.animals)
        residual_area = self.available_area()
        if residual_area == 0:
            return occupied_area
        return occupied_area / residual_area
    


class ZooKeeper:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id
    
    def add_animal(self, animal, fence):
        if fence.habitat == animal.preferred_habitat and fence.available_area() >= animal.area():
            fence.add_animal(animal)
        else:
            print(f"Cannot add {animal.name} to fence due to habitat or space constraints.")
    
    def remove_animal(self, animal, fence):
        fence.remove_animal(animal)
    
    def feed_animal(self, animal):
        for fence in self.fences:
            if animal in fence.animals:
                if fence.available_area() >= animal.growth_area():
                    animal.feed()
                else:
                    print(f"Not enough space to feed {animal.name} in its current fence.")
            else:
                print(f"{animal.name} is not in any of the fences.")

class Zoo:
    def __init__(self, fences: list[Fence], zoo_keeper: list [ZooKeeper]):
        self.fences = fences
        self.zoo_keepers = zoo_keeper
    
    
    def describe_zoo(self):
        description = "Guardians:\n"
        for keeper in self.zoo_keepers:
            description += f"ZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})\n"
        
        description += "\nFences:\n"
        for fence in self.fences:
            description += f"Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})\n"
            description += "with animals:\n"
            for animal in fence.animals:
                description += f"Animal(name={animal.name}, species={animal.species}, age={animal.age})\n"
            description += "#" * 30 + "\n"
        
        print(description)