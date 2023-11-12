def calcola_valore_parola(parola):
    mappatura = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 8, 'g': 3, 'h': 5,
        'i': 1, 'j': 1, 'k': 2, 'l': 3,
        'm': 4, 'n': 5, 'o': 7, 'p': 8,
        'q': 1, 'r': 2, 's': 3, 't': 4,
        'u': 6, 'v': 6, 'w': 6, 'x': 5,
        'y': 1, 'z': 7
    }

    risultato = 0

    for lettera in parola:
        lettera_minuscola = lettera.lower()
        risultato += mappatura.get(lettera_minuscola, 0)

    return risultato

while True:
    parola_inserita = input("Inserisci una parola ('exit' per uscire): ")

    if parola_inserita.lower() == 'exit':
        break  # Esce dal ciclo se l'utente inserisce 'exit'

    risultato_calcolato = calcola_valore_parola(parola_inserita)
    print(f"Il risultato per la parola '{parola_inserita}' è: {risultato_calcolato}")
