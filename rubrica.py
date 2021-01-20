#TecnoGeppetto
# esercizio construire una rubrica semplice con i dizionari
# Aggiunto la funzione di salvataggio con Shelve (Pickle)

import yaml
import shelve
import peewee
import datetime
global rubrica
rubrica = []

# Creo un modello per gli elementi della rubrica
db = peewee.SqliteDatabase('rubrica.db')
class Rubrica(peewee.Model):
    nome = peewee.CharField()
    cognome = peewee.CharField()
    indirizzo = peewee.CharField()
    telefono = peewee.CharField()
    creato = peewee.DateField(default=datetime.date.today)
    class Meta:
        database = db
        db_table = 'rubrica'

# Qui creo l'accesso ai dati della rubrica con la libreria PEEWEE (che si basa su Pickle)
def peewee_salva(rubrica): #
    # Agganciato il DB, create le tabelle  e scrive in DB ok 
    Rubrica.create_table(Rubrica)
    elemento1 = Rubrica.create(nome='Andrea', cognome='Verdi', indirizzo='via le mani dal naso Roma', telefono=['772321','888888'])
    elemento1.save()
 
def peewee_carica():
    # lettura del DB  e carica delle variabili OK
    tutta = Rubrica.select()
    print(tutta)
    for rubrica in Rubrica.select():
        print(rubrica.nome)
        print(rubrica.creato)
        print(rubrica.id)
        print(rubrica.telefono)

# queste due funzioni servono per testare la libreria Shelve 
# per fare il salvataggio di file in formato binario Shelve usa Pickle per 
# salvare su file.
# Al momento non e' collegata al resto delle funzioni ma funziona perfettamente -
def salva_shelve(rubrica):
    with shelve.open("rubrica_shelve.dat") as f:
        f['rubrica'] = rubrica
def carica_shelve():
    f = shelve.open('rubrica_shelve.dat')
    try:
        rubrica = f['rubrica']
    except:
        pass
    finally:
        f.close()
    # se non trova la lista rubrica dentro il file  .dat va in crash ( accade se il file non esiste o e' vuoto.) da sistemare
    return rubrica

# Qui invece costruisco la rubrica sensa librerie, solo con funzioni di base di python
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
#peewee_salva()
peewee_carica()