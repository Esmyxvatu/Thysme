import tkinter as tk
import util, requests #noqa: E401

class Acceuil() :
    def __init__(self):
        self.acceuil = tk.Tk()
        self.input_texte = tk.Entry(self.acceuil)
        self.text = tk.Label(self.acceuil, text="", font=("Arial", 12), fg="white", bg="black", justify="left") #noqa

    def recup_text(self, event) : 
        text = self.input_texte.get()
        text = str(text)
        self.input_texte.delete(0, tk.END)
        send = requests.get(f"http://127.0.0.1:8080/api/modif?g={text}&k={self.username}")
        response = send.text
        util.log(0,f"say : {response}")
        self.see_discut("a")

    def see_discut(self, event) :
        util.log(0,"affichage ...")
        response = requests.get("http://127.0.0.1:8080/api/read")
        contenu = response.text
        self.text.configure(text=contenu)


    def start(self, username) :
        self.username = username
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
        self.username_entry = tk.Entry(self.login)
        self.password_entry = tk.Entry(self.login, show="*")
        self.login_button = tk.Button(self.login, text="Login", command=self.co)
    
    def configure(self) :
        # Définition de la fenetre
        self.login.configure(bg="black")
        self.login.title("Thysme | Login")
        self.login.geometry("800x500")
        # Placements des elements
        self.text_co.pack()
        self.username_entry.pack(side="left")
        self.password_entry.pack(side="right")
        self.login_button.pack()

    def co(self) :
        util.log(0,"Connection ...")
        util.changevalue("connected","True","config\conf.txt")
        self.login.destroy()
        

    def start(self) :
        self.configure()
        util.log(0,"Started login")
        self.login.mainloop()