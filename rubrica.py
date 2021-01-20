#TecnoGeppetto
# esercizio construire una rubrica semplice con i dizionari
# Aggiunto la funzione di salvataggio con Shelve (Pickle)

import yaml
import shelve
global rubrica
rubrica = []


def peewee_salva():
    #qui e' tutto da fare solo riportato qui esercizio ma tutto da fare
        
    import peewee
    import datetime
    db = peewee.SqliteDatabase('test.db')
    class Note(peewee.Model):
        text = peewee.CharField()
        created = peewee.DateField(default=datetime.date.today)
        class Meta:
            database = db
            db_table = 'notes'
    Note.create_table(Note)
    note1 = Note.create(text='Went to the cinema')
    note1.save()
    note2 = Note.create(text='Exercised in the morning',
            created=datetime.date(2018, 10, 20))
    note2.save()
    note3 = Note.create(text='Worked in the garden',
            created=datetime.date(2018, 10, 22))
    note3.save()
    note4 = Note.create(text='Listened to music')
    note4.save()




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
