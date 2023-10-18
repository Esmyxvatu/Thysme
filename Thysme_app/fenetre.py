import tkinter as tk
import util, requests #noqa: E401

global createaccount


class Acceuil() :
    def __init__(self):
        self.acceuil = tk.Tk()
        self.frame = tk.Frame(self.acceuil, bg="black")
        self.input_texte = tk.Entry(self.acceuil)
        self.text = tk.Label(self.acceuil, text="", font=("Arial", 12), fg="white", bg="black", justify="left") #noqa
        self.settings_button = tk.Button(self.frame, text="Settings", font=("Arial", 12), fg="white", bg="black", command=self.settings)
        self.mp_button = tk.Button(self.frame, text="MP", font=("Arial", 12), fg="white", bg="black", command=exit)

    def settings(self) :
        # Redefinition de la fenetre
        self.acceuil.withdraw()
        self.settings = tk.Tk()
        self.settings.title("Thysme | Settings")
        self.settings.geometry("800x500")
        self.settings.configure(bg="black")
        # Création des éléments
        self.settings_button = tk.Button(self.settings, text="Back", font=("Arial", 12), fg="white", bg="black", command=self.settings_deco, anchor="w")
        self.deco_button = tk.Button(self.settings, text="Disconnect", font=("Arial", 12), fg="white", bg="black", command=self.disconnect)
        # Placement des éléments
        self.settings_button.pack()
        self.deco_button.pack()

    def settings_deco(self) :
        self.settings.destroy()
        self.acceuil.deiconify()

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
        self.mp_button.grid(row=0,column=0, sticky="e")
        self.settings_button.grid(row=0, column=1, sticky="w")
        self.frame.pack(fill=tk.BOTH)
        self.input_texte.bind("<Return>", self.recup_text)
        self.input_texte.pack(side=tk.BOTTOM, fill=tk.X)
        self.text.pack(anchor="w")
        util.log(0,"Started acceuil")
        self.see_discut("a")
        self.acceuil.mainloop()

    def disconnect(self) :
        util.changevalue("connected","False","config\conf.txt")
        util.changevalue("UserID","None","config\conf.txt")
        util.log(0,"Disconnect")
        self.acceuil.destroy()
        self.settings.destroy()
        util.start("main.py")

class Create_account() :
    def __init__(self):
        self.ca = tk.Tk()
        self.ca.withdraw()
        # Création des éléments
        self.username_entry = tk.Entry(self.ca, width=50)
        self.password_entry = tk.Entry(self.ca, show="*", width=50)
        self.password_entry_confirm = tk.Entry(self.ca, show="*", width=50)
        self.create_account_button = tk.Button(self.ca, text="Create account", command=self.create)
        self.create_account_text = tk.Label(self.ca, text="Create account", font=("Arial", 24), fg="white", bg="black", justify="center")
        self.cancel_button = tk.Button(self.ca, text="Cancel", command=exit)
        self.back_button = tk.Button(self.ca, text="Back", command=self.ca)
        self.username_text = tk.Label(self.ca, text="Username :", font=("Arial", 12), fg="white", bg="black", justify="left")
        self.password_text = tk.Label(self.ca, text="Password :", font=("Arial", 12), fg="white", bg="black", justify="left")
        self.password_confirm_text = tk.Label(self.ca, text="Confirm password :", font=("Arial", 12), fg="white", bg="black", justify="left")
    
    def create(self) :
        util.log(0,"Creating account ...")
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_confirm = self.password_entry_confirm.get()

        if password == password_confirm :
            uesr = requests.get("http://127.0.0.1:8080/api/getuser").text
            uesr = uesr.split("\n")
            for user in uesr:
                if user.startswith(username) :
                    util.log(0,"Username already exists")
                else :
                    response = requests.get(f"http://127.0.0.1:8080/api/adduser?u={username}&p={password}").text
                    util.log(0,"Account created")
                    util.changevalue("connected","True","config\conf.txt")
                    util.changevalue("UserID",response,"config\conf.txt")
                    self.ca.destroy()
                    util.start("main.py")
        else :
            util.log(0,"Passwords do not match")

    def configure(self) :
        self.ca.configure(bg="black")
        self.ca.title("Thysme | Create account")

        # Placement des elements
        self.back_button.grid(row=0, column=0, sticky="w")
        self.username_text.grid(row=1, column=0, sticky="w")
        self.password_text.grid(row=2, column=0, sticky="w")
        self.password_confirm_text.grid(row=3, column=0, sticky="w")
        self.create_account_button.grid(row=4, column=0, sticky="w")

        self.create_account_text.grid(row=0, column=1, columnspan=2, sticky="w")
        self.username_entry.grid(row=1, column=1, sticky="w")
        self.password_entry.grid(row=2, column=1, sticky="w")
        self.password_entry_confirm.grid(row=3, column=1, sticky="w")
        self.cancel_button.grid(row=4, column=1, sticky="e")
    
    def start(self) :
        self.configure()
        util.log(0,"Started create account")
        self.ca.deiconify()
        self.ca.mainloop()

class Login() :
    def __init__(self):
        if not tk._default_root :
            self.login = tk.Tk()
        else :
            self.login = tk._default_root

        self.text_co = tk.Label(self.login, text="Connection", font=("Arial", 24), fg="white", bg="black", justify="center") #noqa
        self.text_username = tk.Label(self.login, text="Username", font=("Arial", 12), fg="white", bg="black", justify="left") #noqa
        self.text_password = tk.Label(self.login, text="Password", font=("Arial", 12), fg="white", bg="black", justify="left") #noqa
        self.username_entry = tk.Entry(self.login, width=50)
        self.password_entry = tk.Entry(self.login, show="*", width=50)
        self.login_button = tk.Button(self.login, text="Login", command=self.co)
        self.ca_button = tk.Button(self.login, text="Create account", command=self.ca)
        self.annuler_button = tk.Button(self.login, text="Cancel", command=exit)
        self.caa = Create_account()

    def configure(self) :
        # Définition de la fenetre
        self.login.configure(bg="black")
        self.login.title("Thysme | Login")
        # Placements des elements
        self.text_co.grid(row=0, column=0, columnspan=3)
        self.text_username.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, columnspan=2)
        self.text_password.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, columnspan=2)
        self.login_button.grid(row=3, column=0, sticky=tk.W)
        self.ca_button.grid(row=3, column=1)
        self.annuler_button.grid(row=3, column=2, sticky=tk.E)

    def ca(self) :
        util.log(0,"Create account ...")
        self.configure()
        util.log(0,"Started create account")
        self.login.withdraw()
        self.caa.start()

    def co(self) :
        util.log(0,"Connection ...")

        username_try = self.username_entry.get()
        password_try = self.password_entry.get() #noqa:F841
        user = requests.get("http://127.0.0.1:8080/api/getuser").text
        un = user.split("\n")

        for element in un:
            if element.startswith(username_try):
                usn = un[un.index(element)]
                pswd = usn.split(" = ")[1]
                if password_try == pswd:
                    util.log(0,"Connected")
                    util.changevalue("connected","True","config\conf.txt")
                    util.changevalue("UserID",un.index(element),"config\conf.txt")
                    self.login.destroy()
                    util.start("main.py")
                else :
                    util.log(0,"Wrong password")
        util.log(0,"Wrong username")

    def start(self) :
        self.configure()
        util.log(0,"Started login")
        self.login.mainloop()
