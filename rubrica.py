#TecnoGeppetto
# esercizio construire una rubrica semplice con i dizionari
# Le funzioni carica() svuota() rendono la rubrica intera come lista
# Le altre funzioni rendono la stringa "OK"

import yaml
global rubrica
rubrica = []

def aggiungi(nome, cognome, telefono, indirizzo):
    rubrica=carica()
    rubrica.append({"nome" : nome, "cognome" : cognome, "telefono" : telefono, "indirizzo" : indirizzo})
    salva(rubrica)
    return 
def modifica(elemento, nome, cognome, telefono, indirizzo):
    rubrica=carica()
    rubrica[int(elemento)]={"nome" : nome, "cognome" : cognome, "telefono" : telefono, "indirizzo" : indirizzo}
    salva(rubrica)
    return 
def cancella(elemento):
    rubrica=carica()
    del rubrica[int(elemento)]
    salva(rubrica)
    return 
def svuota(noparam=False):
    if noparam == False:
        s =input("Sei proprio sicuro di svuotare la tua Rubrica?? Y/N ")
        if s == "y" or s == "Y":
            rubrica.clear()
        salva(rubrica)
        return 
    else:
        rubrica.clear()
        salva(rubrica)
        return 
def salvaA(files="rubrica.txt"):
    with open(files, "a") as my_rub:
        #my_rub = open("rubrica.txt", "w")
        my_rub.write(yaml.dump(rubrica, default_flow_style=False))
    return 
def salva(rubrica):
    with open("rubrica.txt", "w") as my_rub:
        #my_rub = open("rubrica.txt", "w")
        my_rub.write(yaml.dump(rubrica, default_flow_style=False))
    return 
def carica():
    try:
        f = open("rubrica.txt", "r")
    except FileNotFoundError:
        f = open("rubrica.txt", "w")
        rubrica = []
        f.write(yaml.dump(rubrica, default_flow_style=False))
        f.close()
        f= open("rubrica.txt", "r")
    rubrica = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return rubrica

   