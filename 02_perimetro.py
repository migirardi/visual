# Scrivi un programma che in base alla scelta dell'utente permetta di calcolare il perimetro di diverse figure geometriche
 
def per_figure():
    print("Opzioni disponibili:")
    print("1. Quadrato")
    print("2. Pentagono")
    print("3. Cerchio")

def calcola_perimetro(figura):
    while True:
        try:
            if figura == "quadrato" or figura == "pentagono":
                lato = float(input("Scegli la misura del lato in cm: "))
                if lato <= 0:
                    print("DEVI METTERE SOLO UN NUMERO POSITIVO IDIOTA!")
                else:
                    if figura == "quadrato":
                        perimetro = lato * 4
                        print(f"Il perimetro del quadrato in cm sarà: {perimetro:.2f}")
                    elif figura == "pentagono":
                        perimetro = lato * 5
                        print(f"Il perimetro del pentagono in cm sarà: {perimetro:.2f}")
                    break  # Uscita dal ciclo dopo calcolo valido

            elif figura == "cerchio":
                pi = 3.14
                raggio = float(input("Scegli la misura del raggio in cm: "))
                if raggio <= 0:
                    print("DEVI METTERE SOLO UN NUMERO POSITIVO IDIOTA!")
                else:
                    circonferenza = pi * raggio * 2
                    print(f"La circonferenza del cerchio in cm sarà: {circonferenza:.2f}")
                    break  # Uscita dal ciclo dopo calcolo valido

        except ValueError:
            print("Riprova, devi inserire un numero valido!")

def main():
    while True:
        per_figure()  # Mostra le opzioni per la figura
        figura = input("Scegli la figura: ").lower()
        
        if figura in ["quadrato", "pentagono", "cerchio"]:
            calcola_perimetro(figura)  # Calcola il perimetro o circonferenza

            # Chiedi se l'utente vuole fare un altro calcolo
            risposta = input("Vuoi calcolare il perimetro di un altro poligono? (si/no): ").strip().lower()
            if risposta != "si":
                print("Grazie per aver utilizzato il programma! Arrivederci!")
                break  # Esce dal ciclo principale e termina il programma
        else:
            print("Figura non valida. Per favore, scegli tra 'quadrato', 'pentagono' o 'cerchio'.")

# Avvia il programma
main()
