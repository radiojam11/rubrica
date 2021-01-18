
from bottle import route, run, post, request, static_file, get, error, template
import rubrica

@get('/msg')
def message():
    azione = request.query.azione

    if azione == "aggiungi" :
        nome= request.query.nome
        cognome = request.query.cognome
        telefono_str = request.query.telefono
        indirizzo = request.query.indirizzo
        if "," in telefono_str:
            telefono = telefono_str.split(",")
        else:
            telefono =[]
            telefono.append(telefono_str)
        rubrica.aggiungi(nome=nome, cognome=cognome, telefono=telefono, indirizzo=indirizzo)
        return "Elemento Aggiunto con successo"

    elif azione == "modifica":
        nome= request.query.nome
        cognome = request.query.cognome
        telefono_str = request.query.telefono
        indirizzo = request.query.indirizzo
        elemento = request.query.elemento
        if "," in telefono_str:
            telefono = telefono_str.split(",")
        else:
            telefono =[]
            telefono.append(telefono_str)
        rubrica.modifica(elemento=elemento, nome=nome, cognome=cognome, telefono=telefono, indirizzo=indirizzo)
        return ("Elemento %s modificato con successo" % elemento)

    elif azione == "cancella":
        elemento = request.query.elemento
        rubrica.cancella(int(elemento))
        return ("Elemento %s Cancellato con successo" % elemento)
 
    elif azione == "svuota":
        rubrica.svuota(noparam=True)
        return "Rubrica svuotata con successo"
    
    elif azione == "carica":
        nomefile = request.query.nomefile
        mia_rubrica = rubrica.caricaW()
        return template('mostra_rubrica', mia_rubrica=mia_rubrica)

    return ("Per eseguire azioni su Rubrica digita /msg?azione={AZIONE_da_eseguire} dopo indirizzo e porta nel Brawser")


@error(404)
def error404(error):
    return "Non ho trovato la pagina"

"""
@route('/rubrica')
def rubrica_completa():
    return template('mostra_rubrica')

"""

@route('/')
def indice():
    #return template('mostra_rubrica')
    return static_file("index.html", root='./www/')

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./www/')

"""
@route('/')
def server_static(filepath="/index.html"):
    return static_file(filepath, root="./public/")


@route('/test')
def server_static(filepath="/prova/test.html"):
    return static_file(filepath, root="./public/")



@route("/hello")
def hello():
    return '<div class="col-12" align="center" id="titolo_pag"><h1 align="center">Benvenuto nel nostro Sistema </div>'





@get('/msg')
def message():
    name = request.query.name
    age = request.query.age
    if name == "" or age == "":
        return "Non mi hai dato i parametri necessari"
    return("%s is %s year old" % (name,age))
"""

run(host='localhost', port=8081, reloader=True, debug=True)
#   http://localhost:8080/msg?name=pippo&age=33    questa e' la richiesta di esempio da fare nel browser 



#giocare con le TK inter che sono le estensioni standard per creare una interfaccia GUI
# passare la  rubrica in questo sistema fatto on Peewee
#  e creare una interfaccia da riga di comando  ed una web che accedano agli stessi dati su DB 

