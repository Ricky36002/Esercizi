'''
# Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. La classe offre un modo 
#semplice per tenere traccia di un conteggio che non può diventare negativo.

# Classe Contatore
# Attributi:
# - conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

# Metodi:
# - __init__(): Inizializza l'attributo conteggio a 0.
# - setZero(): Imposta il conteggio a 0.
# - add1(): Incrementa il conteggio di 1.
# - sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, stampa un messaggio di errore.
# - get(): Restituisce il valore corrente del conteggio.
# - mostra(): Stampa a schermo il valore corrente del conteggio.

'''
'''
#Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione di ricette e i loro ingredienti.

# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.

#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.

#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

#     - list_recipes(): Elenca tutte le ricette esistenti.

#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

'''
'''
# In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
# 1. Classe Base: Veicolo
# Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
# Attributi:

#     marca (stringa)
#     modello (stringa)
#     anno (intero)

# Metodi:

#     __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
#     descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

# 2. Classe Derivata: Auto
# Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:

#     numero_porte (intero)

# Metodi:

#     __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
#     descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il numero di porte nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

# 3. Classe Derivata: Moto
# Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
# Attributi:

#     tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

# Metodi:

#     __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
#     descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".

'''
'''
# Obiettivo
# L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni di due specie animali usando la programmazione orientata agli oggetti in Python.

# Descrizione del problema
# Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
# - In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
# - n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
# Specifiche tecniche

# 1. Classe Specie
# - Attributi:

#     nome (str): Nome della specie.
#     popolazione (int): Popolazione iniziale.
#     tasso_crescita (float): Tasso di crescita annuo percentuale.

# - Metodi:

#     __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): Costruttore per inizializzare gli attributi della classe.
#     cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
#     anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
#     getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².

 

# 2. Sottoclassi BufaloKlingon e Elefante
# Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e devono inizializzare il nome della specie rispettiva.
 
# Formule Matematiche:

#     Aggiornamento della popolazione per l'anno successivo:
#         Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
#     Calcolo della densità di popolazione:
#         Formula: popolazione / area_kmq
#         Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
#     Calcolo degli anni necessari per superare la popolazione di un'altra specie:
#         Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione di questa specie non supera quella dell'altra.
'''
