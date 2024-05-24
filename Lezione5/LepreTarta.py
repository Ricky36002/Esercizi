#In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento. I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati. Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

#- Tartaruga:
 #   - Passo veloce (50% di probabilità): avanza di 3 quadrati.
 #   - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
 #   - Passo lento (30% di probabilità): avanza di 1 quadrato.

#- Lepre:
 #   - Riposo (20% di probabilità): non si muove.
 #    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
 #    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
 #    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
 #    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

#Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

#Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole.

#Iniziate la gara stampando:
#'BANG !!!!! AND THEY'RE OFF !!!!!'

#Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente, i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

#Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!". Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

#Requisiti del Codice:
#- Utilizzare il modulo random per la generazione dei numeri casuali.
#- Definire e utilizzare:
# - una funzione per visualizzare le posizioni sulla corsia di gara,
#  - una funzione per calcolare la mossa della tartaruga,
#   - una funzione per calcolare la mossa della lepre.
#- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.

# Variabilità Ambientale:
#Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
#Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
 
#Modificatori mossa:
#- La Tartaruga in caso di pioggia subisce penalità mossa -1. In caso di sole non subisce variazioni.
#- La Lepre in caso di pioggia subisca una penalità mossa di -2. In caso di sole non subisce variazioni.


import random

def display_race(positions):
    for i in range(1, 71):
        if positions['tortoise'] == i and positions['hare'] == i:
            print('OUCH!!!', end='')
        elif positions['tortoise'] == i:
            print('T', end='')
        elif positions['hare'] == i:
            print('H', end='')
        else:
            print('-', end='')
    print()

def tortoise_move():
    move = random.randint(1, 10)
    if move <= 5:
        return 3
    elif move <= 7:
        return -6
    else:
        return 1

def hare_move():
    move = random.randint(1, 10)
    if move <= 2:
        return 0
    elif move <= 4:
        return 9
    elif move == 5:
        return -12
    elif move <= 8:
        return 1
    else:
        return -2

def race():
    tortoise_position = 1
    hare_position = 1

    print("BANG !!!!! AND THEY'RE OFF !!!!!")

    while True:
        tortoise_position += tortoise_move()
        hare_position += hare_move()
        if tortoise_position >= 70 and hare_position >= 70:
            print("It's a tie!")
            break
        elif tortoise_position >= 70:
            print("Tortoise wins! VAY!!!")
            break
        elif hare_position >= 70:
            print("Hare wins! YUCH!!!")
            break

        if tortoise_position < 1:
            tortoise_position = 1
        if hare_position < 1:
            hare_position = 1

        positions = {'tortoise': tortoise_position, 'hare': hare_position}
        display_race(positions)

################

import random

def display_positions(turtle_pos, rabbit_pos):
    
    positions = ['-'] * 70
    
    positions[turtle_pos] = 'T'
    positions[rabbit_pos] = 'H'
    
    if turtle_pos == rabbit_pos:
        positions[turtle_pos] = 'OUCH!!!'
    
    print(''.join(positions))

def turtle_move(energy, weather):
    
    r = random.randint(1, 10)
    
    
    if r <= 2:
        energy += 10
        if energy > 100:
            energy = 100
    
    
    if 3 <= r <= 7:
        move = 3
        energy -= 5
    elif 8 <= r <= 9:
        move = -6
        energy -= 10
    else:
        move = 1
        energy -= 3
    
    
    if weather == "rainy":
        move -= 1
    return move, energy

def rabbit_move(energy, weather):
    
    r = random.randint(1, 10)
    
    
    if r <= 2:
        energy += 10
        if energy > 100:
            energy = 100
    
    
    if r <= 2:
        move = 0
        energy += 10
        if energy > 100:
            energy = 100
    elif 3 <= r <= 5:
        move = 9
    elif r == 6:
        move = -12
    elif 7 <= r <= 8:
        move = 1
    else:
        move = -2
    
    
    if weather == "rainy":
        move -= 2
    return move, energy

def change_weather(tick):
    
    if tick % 10 == 0:
        return random.choice(["sunny", "rainy"])
    else:
        return "unchanged"

def main():
    
    turtle_pos = 1
    rabbit_pos = 1
    
    weather = "sunny"
    
    turtle_energy = 100
    rabbit_energy = 100
    
    tick = 1
    
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:
        
        turtle_move_result, turtle_energy = turtle_move(turtle_energy, weather)
        rabbit_move_result, rabbit_energy = rabbit_move(rabbit_energy, weather)
        turtle_pos += turtle_move_result
        rabbit_pos += rabbit_move_result
        
        
        if turtle_pos >= 70 or rabbit_pos >= 70:
            if turtle_pos > rabbit_pos:
                print('TORTOISE WINS! || VAY!!!')
            elif rabbit_pos > turtle_pos:
                print('HARE WINS || YUCH!!!')
            else:
                print('IT\'S A TIE.')
            break
        
        
        if turtle_pos < 1:
            turtle_pos = 1
        if rabbit_pos < 1:
            rabbit_pos = 1
        
        
        display_positions(turtle_pos, rabbit_pos)
        
        
        weather = change_weather(tick)
        if weather != "unchanged":
            print(f"The weather changed to: {weather.upper()}")
        
        
        tick += 1

if __name__ == '__main__':
    main()

def ostacoli(self,):
    pass