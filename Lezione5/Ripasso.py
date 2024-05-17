nome_variabile: int = 10
nome_variabile: int = 10.0
nome_variabile: bool = False
nome_variabile: str = "ciao"


nome_variabile: float = 10


nome_variabile = nome_variabile + 5.5
print(nome_variabile)


variabile_float: float = 0.0


variabile_float = 5.0 + 10.0
print(variabile_float)


variabile_int: int =0
variabile_int =10 + 5
print(variabile_int)


lunghezza_lista: int = 7
import math
punto_di_mezzo: int = 7//2
print(math.ceil(punto_di_mezzo))
print (math.acosh(1))

var_1: bool =True
var_2: bool=False

print(var_1 and var_2)
print(var_1 or var_2)
print(not var_1)

x: int = -1000
lista: list =[1, 2, 3, 5]
i: int = 0
if lista[i] > lista [i+1]:

    temp: int = lista[i]

    lista[i]= lista[i+1]
    lista[i+1] = temp

    if x > 0 or x < 20:
        print(f"{var_1 and var_2}")
    
for x in range(10):
    print(f"x = {x}")
    
# cambiando b=false si entra nel elif cambiano a=false and b=false si entra nel else

a: bool= True
b:bool= True
if a and b:

    print(f"sono nel primo if")

elif a or b:

    print(f"sono nelprimo elif")

else:

    print(f"sono nell'else")



anagrafe: dict = {
    "persona_1": "Flavio",
    "persona_2": "Marco",
    "persona_3": "Leonardo"
}
print(anagrafe ["persona_1"])


anagrafe["persona_4"] = "Riccardo"


anagrafe: dict = {
    "persona_1": "Flavio",
    "persona_2": "Marco",
    "persona_3": "Leonardo"
}

key: str = "persona_5"

if key in anagrafe:
    
    print(anagrafe[key])
else:

    anagrafe[key] = None    


voti: list = [{"nome": "Flavio", "voto": 18},{"nome": "Marco", "voto": 20},{"nome": "Leonardo", "voto": 26}]
exemple: dict = {"Flavio": [18, 25], "Marco": [20, 19], "Leonardo": [26, 18]}
aggr: dict = {}

for dizionario in voti:
    
    nome : str = dizionario["nome"]
    voto : int = dizionario["voto"]

    if nome in aggr:

        aggr[nome].append(voto)
    else:
        aggr[nome] = [voto] 

for key, value in aggr.items():

    print(key, value)

for key in aggr.keys():
    print(key)

for value in aggr.values():
    print(value)


Boh: dict = {
    "key_1": {
        "key_1_1": {
            "floor": 0
        }
    },
    "key_2": {
        "key_2_1": {
            "floor": 1
        },
        "key_2_2": {
            "floor": 2
        }
    }
}


Boh["key_1"]["key_1_1"]["floor"]
Boh["key_2"]["key_2_1"]["floor"]
Boh["key_2"]["key_2_2"]["floor"]

a: list =[3, 2]
b: tuple =[1, 2]

a[0]= 3
i, j= b

a
b






























































