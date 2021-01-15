
from bottle import route, run, post, request, static_file, get, error, template




@error(404)
def error404(error):
    return "Non ho trovato la pagina"

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public/')

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

run(host='localhost', port=8080, reloader=True, debug=True)
#   http://localhost:8080/msg?name=pippo&age=33    questa e' la richiesta di esempio da fare nel browser 



#giocare con le TK inter che sono le estensioni standard per creare una interfaccia GUI
# passare la  rubrica in questo sistema fatto on Peewee
#  e creare una interfaccia da riga di comando  ed una web che accedano agli stessi dati su DB 

