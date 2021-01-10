# esercizio construire una rubrica semplice con i dizionari
import yaml
rubrica = []

def aggiungi(nome, cognome, telefono, indirizzo):
    rubrica.append({"nome" : nome, "cognome" : cognome, "telefono" : telefono, "indirizzo" : indirizzo})
    return "OK"
def modifica(elemento, nome, cognome, telefono, indirizzo):
    rubrica[elemento]={"nome" : nome, "cognome" : cognome, "telefono" : telefono, "indirizzo" : indirizzo}
    return "OK"
def cancella(elemento):
    rubrica.remove(elemento)
    return "OK"
def svuota():
    s =input("Sei proprio sicuro di svuotare la tua Rubrica?? Y/N ")
    if s == "y" or s=="Y":
        rubrica.clear()
        return "OK"
def salva(files="rubrica.txt"):
    with open(files, "w") as my_rub:
        #my_rub = open("rubrica.txt", "w")
        my_rub.write(yaml.dump(rubrica, default_flow_style=False))
    return "OK"
def carica(files="rubrica.txt", modo = "r"):
    with open(files, modo) as mia_rub:
        rubrica = yaml.load(mia_rub)
        print("fatto")
        # da completare
        
        
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
"""
carica()
#aggiungi("Mario", "Rossi", [222333221,123123432],"via Andiamo n.11 Roncisvalle (PT)")
print(rubrica)