#1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

#2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

#3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

#4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

#Funzionalità:

#1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

#2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

#3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

#4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

#5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

#E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale) con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

#Guardians:

#ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

#Fences:

#Fence(area=100, temperature=25, habitat=Continent)

#with animals:

#Animal(name=Scoiattolo, species=Blabla, age=25)

#Animal(name=Lupo, species=Lupus, age=14)
#########################

#Fra un recinto e l'altro mettete 30 volte il carattere #.

class Animal:

    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str) -> None:
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = round(100 * (1 / age), 3)
        self.fence: Fence = None

class Fence:
   
    def __init__(self, area: float, temperature: float, habitat: str, animals: list[Animal] = []) -> None:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []
        self.animals = [animal for animal in animals if self.is_available(animal) and animal.preferred_habitat == habitat]
        for animal in self.animals:
            animal.fence = self

    def is_available(self, add_animal: Animal, feed: bool = False) -> bool:
       
        available = self.area - sum(animal.width*animal.height for animal in self.animals if self.animals)
        if feed:
            return available-(add_animal.width*add_animal.height + (add_animal.width*2/100)*(add_animal.height*2/100)) > 0
        return available-add_animal.width*add_animal.height > 0

class ZooKeeper:

    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.id: str = id
    
    def add_animal(self, animal: Animal, fence: Fence) -> None:
        
        if not animal.fence:
            if fence.habitat == animal.preferred_habitat:
                if fence.is_available(animal):
                    fence.animals.append(animal)
                    animal.fence = fence
                else:
                    print(f"\nThe animal {animal.name} cannot be contained in the specified fence.")
            else:
                print(f"\nThe animal {animal.name}'s preferred habitat '{animal.preferred_habitat}' is not the same as the fence's '{fence.habitat}'.")
        else:
            print(f"\nThe animal {animal.name} is already inside the fence {animal.fence.habitat}.")

    def remove_animal(self, remove_animal: Animal, fence: Fence) -> None:
        
        animals: list = fence.animals
        animals_names: list = [animal.name for animal in animals]
        if animals:
            if remove_animal.fence == fence:
                index: int = animals_names.index(remove_animal.name)
                del animals[index]
                remove_animal.fence = None
            else:
                print(f"\nThere is no animal by the name of {remove_animal.name} in the fence {fence.habitat}.")
        else:
            print("\nThe fence is empty.")
    
    def feed(self, feed_animal: Animal) -> None:
       
        if feed_animal.fence:
            if feed_animal.fence.is_available(feed_animal, feed=True):
                feed_animal.width += feed_animal.width/50
                feed_animal.height += feed_animal.height/50
                feed_animal.health += feed_animal.health/100
            else:
                print(f"\nThe animal {feed_animal.name} will get too big if fed.")
        else:
            print(f"\nThe animal {feed_animal.name} doesn't belong to any fence")
    
    def clean(self, fence: Fence) -> float:
        
        animals: list = fence.animals
        occupied: float = sum(animal.width*animal.height for animal in animals)
        available: float = fence.area - occupied
        time: float = occupied if available == 0 else occupied/available
        return time

class Zoo:

    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]) -> None:
        self.fences: list[Fence] = fences
        self.zoo_keepers: list[ZooKeeper] = zoo_keepers

    def describe_zoo(self) -> None:
        
        print("\n\nGuardians:")
        for keeper in self.zoo_keepers:
            print(f"\nZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})")
        print("\nFences:")
        for fence in self.fences:
            print(f"\nFence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})", end="\n\n")
            if fence.animals:
                print("with animals:\n")
                for animal in fence.animals:
                    print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})",end="\n\n")
            print("#"*30)
