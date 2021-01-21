#TecnoGeppetto
# esercizio construire una rubrica semplice con i dizionari
# Aggiunto la funzione di salvataggio con Shelve (Pickle)
# ed iniziato a progettae l'accesso ai file con PeeWee.

# elemento test di rubrica =   [{'nome': 'Paolo', 'cognome': 'White', 'telefono': "['772321', '888888']", 'indirizzo': 'via versi Roma'}]
# #

import yaml
import shelve
import peewee
import datetime
import os
global rubrica
rubrica = []

# ########################################################  PeeWee  ################
# Per utilizzare lo stesso motore rubrica.py con PeeWee non si deve usare la funzione salva come con tutte le altre librerie
# perche' in questo caso i dati vengono trattenuti nel DB e non soostituiti tutte le volte come negli altri casi.
# Quindi per salvare nuovi item in rubrica va utilizzato la funzione apposita (da creare)  ma non la funzione salva 
# che duplicherebbe tutti i vecchi dati#

# Creo un modello per gli elementi della rubrica
db = peewee.SqliteDatabase('rubrica.db')
class Rubrica(peewee.Model):
    id = peewee.PrimaryKeyField()
    nome = peewee.CharField()
    cognome = peewee.CharField()
    indirizzo = peewee.CharField()
    telefono = peewee.CharField()
    creato = peewee.DateField(default=datetime.date.today)
    class Meta:
        database = db
        db_table = 'rubrica'

# Qui creo l'accesso ai dati della rubrica con la libreria PEEWEE (che si basa su Pickle)
# l'effetto e' quello di un DB
# LA FUNZIONE SALVA()  Va utilizzata solamente per creare il file di DB. per gli aggiornamenti 
# e le modifiche vanno usate le funzioni apposite. (da creare)

def peewee_salva(): # rubrica
    # se il file 'rubrica.db' non esiste, lo creo e ci metto le tabelle che mi servono
    if not os.path.exists("rubrica.db") :
        # Agganciato il DB, create le tabelle  e scrive in DB ok 
        Rubrica.create_table(Rubrica)
    else:
        pass
    # Queste cose sotto servono per popolare il file rubrica.db per fare i test
    #elemento1 = Rubrica.create(nome='Paolo', cognome='White', indirizzo='via versi Roma', telefono=['772321','888888'])
    #print(type(elemento1))
    #elemento1.save()
    #######################################
    """
    for el in rubrica:
        nome = el["nome"]
        cognome = el["cognome"]
        indirizzo = el["indirizzo"]
        telefono = el["telefono"]
        Rubrica.create(nome=nome, cognome=cognome, indirizzo=indirizzo, telefono=telefono)
    """
 
def peewee_carica():
    # lettura del DB  e carica delle variabili OK
    #tuttalarubrica = Rubrica.select()       # carico la SELECT dal DB
    for elemento in Rubrica.select():       # itero la SELECT del DB e ricavo un singolo elemento
        nome = elemento.nome
        cognome = elemento.cognome
        indirizzo = elemento.indirizzo
        telefono = elemento.telefono
        creato = elemento.creato
        print(elemento.id)
        rubrica.append({"nome" : nome, "cognome" : cognome, "telefono" : telefono, "indirizzo" : indirizzo})
    print(rubrica)  # riga da cancellare
    return rubrica 

    
def peewee_aggiungi(nome, cognome, telefono, indirizzo):
    """ La funzione aggiunge un nuovo record al file DB  """
    nuovo_record = Rubrica()
    nuovo_record.nome = nome
    nuovo_record.cognome = cognome 
    nuovo_record.indirizzo = indirizzo
    nuovo_record.telefono =  telefono
    nuovo_record.save()
    return

def peewee_modifica(elemento, nome, cognome, telefono, indirizzo):
    """ La funizone modifica il record alla posizione elemento nel DB ## 
    NB. elemento parte da 1 (quindi non togliere 1 come negli altri casi) """
    modifica_record = Rubrica()
    modifica_record.id = int(elemento)
    modifica_record.nome = nome
    modifica_record.cognome = cognome 
    modifica_record.indirizzo = indirizzo
    modifica_record.telefono =  telefono
    modifica_record.save()
    return


# ########################################################    Shelve    #################
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

# ########################################################  Metodo TESTO con Yaml  #################
# Yaml passa tutta la lista dentro il file di testo trasformandola in una lunga stringa 
# ed utilizzando una specie di Markup Language.
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

#peewee_salva()
#peewee_salva([{'nome': 'Maria', 'cognome': 'Rossi', 'telefono': "['772321', '888888']", 'indirizzo': 'via versi Roma'}])
#peewee_aggiungi(nome='Federico', cognome='Rovazzi', indirizzo='via di culo  Roma', telefono=['33452321','9987888888'])
peewee_modifica(elemento = 1, nome= "Asdrubale", cognome = "Aniscalchi", indirizzo = " via le mani dal naso", telefono = "['123213']" )
peewee_carica()