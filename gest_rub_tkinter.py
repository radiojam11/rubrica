import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import yaml
import rubrica
import finestra_prova as nw

def apri():
    """Richiama dal motore rubrica.py la funzione carica()"""
    rubrica_ = rubrica.carica()
    for num, el in enumerate(rubrica_):
        stringa = f"Elem. {num+1} "+ "\t-"+el["nome"] + "\t-"+ el["cognome"]+ "\t-"+ el["indirizzo"] + "\t-"+ "-".join(el["telefono"])+"\n"
        finestra_rubrica.insert(tk.END, stringa)
    window.title(f"TecnoGeppetto Rubrica App")

def crea_form(): #ancora non funziona la seconda window va in crash
    """Richiama da rubrica.py la funzione aggiungi()  passa  nome cognome indirizzo  num tel"""
    window2 = tk.Tk()
    window2.rowconfigure(0, minsize=200, weight=1)
    window2.columnconfigure(1, minsize=200, weight=1)
    #rubrica.aggiungi(nome=nome,cognome=cognome,indirizzo=indirizzo,telefono=telefono)
    window2.title(f"Aggiungi a Rubrica")
    label_nome = tk.Label(text="Digita Nome", fg="white", bg="black")
    finestra_form_nome = tk.Entry()
    label_cognome = tk.Label(text="Digita Cognome", fg="white", bg="black")
    finestra_form_cognome = tk.Entry()
    button = tk.Button(
        text="Click me!",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
    )
    label_nome.pack()
    finestra_form_nome.pack()
    label_cognome.pack()
    finestra_form_cognome.pack()
    button.pack()

    window2.mainloop()

def modifica():
    pass
def cancella():
    pass

window = tk.Tk()
window.title(f"TecnoGeppetto Rubrica App")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

finestra_rubrica = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_apri = tk.Button(fr_buttons, text="Apri", command=apri)
btn_aggiungi = tk.Button(fr_buttons, text="Aggiungi", command=crea_form)
btn_modifica = tk.Button(fr_buttons, text="Modifica", command=modifica)

btn_apri.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_aggiungi.grid(row=1, column=0, sticky="ew", padx=5, pady=5 )
btn_modifica.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
finestra_rubrica.grid(row=0, column=1, sticky="nsew")

window.mainloop()