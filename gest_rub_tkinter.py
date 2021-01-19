#TecnoGeppetto
#Il sistema si aggancia al suo motore "rubrica.py" e fornisce una GUI con il framework Tk inter
#ancora da perfezionare la visualizzazione grafica degli elementi nella finestra.
#

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import yaml
import rubrica


def apri():
    """Richiama dal motore rubrica.py la funzione carica()"""
    finestra_rubrica.delete("1.0", tk.END) #cancella la finestra di testo
    rubrica_ = rubrica.carica()
    for num, el in enumerate(rubrica_):
        stringa = f"Elem. {num+1} "+ "\t-"+el["nome"] + "\t-"+ el["cognome"]+ "\t-"+ el["indirizzo"] + "\t-"+ "-".join(el["telefono"])+"\n"
        finestra_rubrica.insert(tk.END, stringa)
    window.title(f"TecnoGeppetto Rubrica App")

def handle_click(event):
    """ gestisce l'evento click sul tasto aggiungi a rubrica """
    nome=finestra_form_nome.get()
    cognome=finestra_form_cognome.get()
    indirizzo = finestra_form_indirizzo.get()
    telefono = finestra_form_telefono.get()
    rubrica.aggiungi(nome=nome,cognome=cognome,indirizzo=indirizzo,telefono=telefono)
    apri()

def crea_form(): #ancora non funziona la seconda window va in crash
    """Richiama da rubrica.py la funzione aggiungi()  passa  nome cognome indirizzo  num tel"""
    window.title(f"Aggiungi a Rubrica")
    button.bind("<Button-1>", handle_click)
    
    
def modifica():
    pass
def cancella():
    pass

window = tk.Tk()
window.title(f"TecnoGeppetto Rubrica App")
window.rowconfigure(0, minsize=1, weight=1) #la grandezza della riga
window.columnconfigure(1, minsize=10, weight=1) #la colonna del form Aggiungi
window.columnconfigure(2, minsize=10, weight=1) #la colonna del campo testo dove viene scritto il contenuto della rubrica
finestra_rubrica = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_apri = tk.Button(fr_buttons, text="Apri", command=apri)
btn_aggiungi = tk.Button(fr_buttons, text="Aggiungi", command=crea_form)
btn_modifica = tk.Button(fr_buttons, text="Modifica", command=modifica)
btn_cancella = tk.Button(fr_buttons, text="Cancella", command=cancella)

fr_form_aggiungi = tk.Frame(window, relief=tk.RAISED, bd=2)
label_nome = tk.Label(text="Digita Nome")
finestra_form_nome = tk.Entry()
label_cognome = tk.Label(text="Digita Cognome")
finestra_form_cognome = tk.Entry()
label_indirizzo = tk.Label(text="Digita Indirizzo")
finestra_form_indirizzo = tk.Entry()
label_telefono = tk.Label(text="Digita Telefono")
finestra_form_telefono = tk.Entry()
button = tk.Button(
    text="Aggiungi",
    width=25,
    height=5,
    
    )
### costruisco i bottoni principali in un frame nella colonna 0
btn_apri.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_aggiungi.grid(row=1, column=0, sticky="ew", padx=5, pady=5 )
btn_modifica.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_cancella.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky="ns")

###creo la finestra in colonna 2 con il frame testo dove ricevo la rubrica
finestra_rubrica.grid(row=10, column=2, sticky="nsew")

###creo il form con le variabili per fare la modifica dei dati 
label_nome.grid(row=0, column=1, padx=5, pady=5) # la istruzione sticky proporziona lo spazio occupato dalla label. vedi
finestra_form_nome.grid(row=1, column=1,  padx=5, pady=5)
label_cognome.grid(row=2, column=1, padx=5, pady=5)
finestra_form_cognome.grid(row=3, column=1, padx=5, pady=5)
label_indirizzo.grid(row=4, column=1, padx=5, pady=5)
finestra_form_indirizzo.grid(row=5, column=1, padx=5, pady=5)
label_telefono.grid(row=6, column=1,  padx=5, pady=5)
finestra_form_telefono.grid(row=7, column=1,  padx=5, pady=5)
button.grid(row=8, column=1,  padx=5, pady=5)
fr_form_aggiungi.grid(row=0, column=1, sticky="ns")



window.mainloop()