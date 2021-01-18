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
    return "OK"
def modifica(elemento, nome, cognome, telefono, indirizzo):
    rubrica=carica()
    rubrica[int(elemento)]={"nome" : nome, "cognome" : cognome, "telefono" : telefono, "indirizzo" : indirizzo}
    salva(rubrica)
    return "OK"
def cancella(elemento):
    rubrica=carica()
    del rubrica[int(elemento)]
    salva(rubrica)
    return "OK"
def svuota(noparam=False):
    if noparam == False:
        s =input("Sei proprio sicuro di svuotare la tua Rubrica?? Y/N ")
        if s == "y" or s == "Y":
            rubrica.clear()
        salva()
        return rubrica
    else:
        rubrica.clear()
        salva()
        return rubrica
def salvaA(files="rubrica.txt"):
    with open(files, "a") as my_rub:
        #my_rub = open("rubrica.txt", "w")
        my_rub.write(yaml.dump(rubrica, default_flow_style=False))
    return "OK"
def salva(rubrica):
    with open("rubrica.txt", "w") as my_rub:
        #my_rub = open("rubrica.txt", "w")
        my_rub.write(yaml.dump(rubrica, default_flow_style=False))
    return "OK"
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

        
def componi_html():
    """la funzione compone il file della rubrica dopo un chiamata di carica_rubrica """
    #componi il file rubrica_car.html
    pass




"""

R1 = {
    "nome" : "uno",
    "cognome" : "tale",
    "telefono" : ["343222332","4433223322"],
    "indirizzo" : "via con l0'indirizzo Roma"}

R2 = {
    "nome" : "due",
    "cognome" : "tale",
    "telefono" : ["34776677332","4777886622"],
    "indirizzo" : "via con l0'indirizzo Genova"}

rubrica.append(R1)
rubrica.append(R2)

print(rubrica)

print(aggiungi("Mario", "Rossi", [222333221,123123432],"via Andiamo n.11 Roncisvalle (PT)"))
print(rubrica[2])

print(modifica(2, "Giuseppe", "Rossi", [222333221,123123432],"via Andiamo n.11 Roncisvalle (PT)" ))
print(rubrica[2])
svuota()
print(rubrica)
salva()

rubrica = carica()
aggiungi("Mario", "Rossi", [222333221,123123432],"via Andiamo n.11 Roncisvalle (PT)")
aggiungi("Paolo", "Verdi", [55533251,775566432],"via Versi n.13 Chissaddove (MT)")
print(rubrica)
# salva("pinko.txt")
rubrica = svuota()
print(rubrica)
salva()
"""
