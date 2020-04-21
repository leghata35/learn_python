# La fenetre principale de l'application
from tkinter import *

window = Tk()

# Personalisation de la fenetre principale de l'application
window.title("Sante pay")
window.minsize(1200, 600)
# window.iconbitmap("pay.ico")
window.config(background="#605f61")

labet_title = Label(window, text="Logiciel de pay", font=("Courrier", 40), bg="#605f61", fg="white")
labet_title.pack(expand=YES)

# Demarrer l'application
window.mainloop()
