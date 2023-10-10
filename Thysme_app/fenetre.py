import tkinter as tk
import util, requests #noqa

class Acceuil() :
    def __init__(self):
        self.acceuil = tk.Tk()
        self.input_texte = tk.Entry(self.acceuil)
        self.text = tk.Label(self.acceuil, text="", font=("Arial", 12), fg="white", bg="black", justify="left") #noqa

    def recup_text(self, event) : 
        text = self.input_texte.get()
        text = str(text)
        self.input_texte.delete(0, tk.END)
        send = requests.get(f"http://127.0.0.1:5000/api/modif?g={text}&k=Esmyx")
        response = send.text
        util.log(0,f"say : {response}")
        self.see_discut("aé")

    def see_discut(self, event) :
        util.log(0,"affichage ...")
        response = requests.get("http://127.0.0.1:5000/api/read")
        contenu = response.text
        self.text.configure(text=contenu)


    def start(self) :
        self.acceuil.configure(bg="black")
        self.acceuil.title("Thysme")
        self.acceuil.geometry("800x500")
        self.input_texte.bind("<Return>", self.recup_text)
        self.input_texte.pack(side=tk.BOTTOM, fill=tk.X)
        self.text.pack(anchor="w")
        util.log(0,"Started acceuil")
        self.see_discut("a")
        self.acceuil.mainloop()

class Login() :
    def __init__(self):
        if not tk._default_root :
            self.login = tk.Tk()
        else :
            self.login = tk._default_root
        self.text_co = tk.Label(self.login, text="Connection", font=("Arial", 24), fg="white", bg="black", justify="center") #noqa
    
    def start(self) :
        self.login.configure(bg="black")
        self.login.title("Thysme | Login")
        self.login.geometry("800x500")
        self.text_co.pack()
        util.log(0,"Started login")
        self.login.mainloop()