import os, win32com.client, getpass, time, requests, shutil # noqa: E401, F401
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

global start, filename, racourci, user

# Définition des variables
user = getpass.getuser()
filename = f"C:\\Users\\{user}\\AppData\\Local"
urls = ["https://github.com/Esmyxvatu/Thysme/raw/main/Thysme_app/fenetre.py",
            "https://github.com/Esmyxvatu/Thysme/raw/main/Thysme_app/util.py",
            "https://github.com/Esmyxvatu/Thysme/raw/main/Thysme_app/main.py",
            "https://github.com/Esmyxvatu/Thysme/raw/main/Thysme_app/config/util_config.txt",]
dossier = ["config"]
racourci = False
start = False
num_files = len(urls)

# Définition des Classes
class Window() :
    def __init__(self) :
        # Créer la fenêtre
        self.window = tk.Tk()

        # Ajouter les boutons (1 = choisir un dossier, 2 = installer, 3 = annuler) #noqa:E501
        self.button = tk.Button(self.window, text="Choisir un dossier", command=self.file_to_save, anchor="w")  # noqa: E501
        self.button_start = tk.Button(self.window, text="Installer", command=self.download_file)  # noqa: E501
        self.bouton_annuler = tk.Button(self.window, text="Annuler", command=self.window.destroy)  # noqa: E501

        # Création de la barre de chargement
        self.progress = ttk.Progressbar(self.window, orient="horizontal", length="200", mode="determinate")  # noqa: E501

        # Ajouter les checkbox (1 = lancer le programme, 2 = créer un raccourci sur le bureau) #noqa:E501
        self.checked_1 = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.window, text="Lancer le programme après l'installation", variable=self.checked_1, command=self.on_checkbox_change, anchor="w")  # noqa: E501
        self.checked_2 = tk.BooleanVar()
        self.checkboxe = tk.Checkbutton(self.window, text="Créer un raccourci sur le bureau", variable=self.checked_2, command=self.on_checkbox_change_2, anchor="w")  # noqa: E501
    
    def on_checkbox_change(self):
        global start
        if self.checked_1.get():
            start = True
        else:
            start = False

    def on_checkbox_change_2(self):
        global racourci
        if self.checked_1.get():
            racourci = True
        else:
            racourci = False

    def download_file(self): #noqa
        self.reconfigure()

        global start, target, racourci, user
        
        shortcut = f"C:\\Users\\{user}\\Desktop\\Thysme.lnk"
        target = f"{filename}\\Thysme\\main.py"

        #   Creation du répertoire "Thysme"
        try :
            os.chdir(filename)
            os.system("mkdir Thysme")
            os.chdir(f"{filename}\\Thysme")
        except : #noqa:E722
            print("Erreur lors de la création du répertoire Thysme")
            print(f"Path : {filename}")

        # Création des autres répertoires
        for i in dossier :
            try :
                os.chdir(f"{filename}\\Thysme")
                os.system(f"mkdir {i}")
                os.chdir(f"{filename}\\Thysme")
            except : #noqa:E722
                print(f"Erreur lors de la création du dossier {dossier[i]}")

        for url in urls:
            file_name = url.split("/")[-1]
            print(f"Downloading {file_name}...")
            with open(file_name, 'w') as f:
                response = requests.get(url)
                content = response.text
                f.write(content)
            self.update_progress(num_files, urls.index(url))

        if racourci :
            try :
                create_shortcut(target, shortcut)
            except : #noqa:E722
                print("Erreur lors de la création du raccourci")
                pass
        if start :
            try :
                os.chdir(f"{filename}\\Thysme")
                os.startfile("main.py")
            except : #noqa:E722
                print("Erreur lors de l'ouverture du fichier")
                pass
        
        self.reset()
        print("Téléchargement réussi !")
        exit()

    def reset(self):
        try :
            shutil.copy(f"{filename}\\Thysme\\util_config.txt", f"{filename}\\Thysme\\config\\util_config.txt") #noqa:E501
            os.remove(f"{filename}\\Thysme\\util_config.txt")
        except : #noqa:E722
            print("Erreur lors de la copie du fichier")

    def file_to_save(self):
        global filename
        filename = filedialog.askdirectory(title="Choisir un dossier où installer Thysme") #noqa:E501

    def update_progress(self, num_files, place_of_file):
        self.progress["maximum"] = num_files

        self.progress["value"] = place_of_file + 1
        self.window.update()
        time.sleep(0.5)

    def sup(self):
        try :
            os.chdir(filename)
            os.system("rmdir /s /q Thysme")
            os.remove(f"{filename}\\util_config.txt")
        except : #noqa:E722
            print("Erreur lors de la suppression du dossier")
        self.window.destroy()

    def reconfigure(self) :
        #   Modification de la fenetre
        self.window.title("Thysme | Installer | Progression")
        self.window.resizable(False, False)

        #   Placement des elements
        self.button_start.configure(text="Ok")
        self.bouton_annuler.configure(command=self.sup)
        self.button_start.grid(row=1, column=0, sticky="w")
        self.bouton_annuler.grid(row=1, column=0, sticky="e")
        self.button.destroy()
        self.checkbox.destroy()
        self.checkboxe.destroy()
        self.progress.grid(row=0, column=0, sticky="w")

    def configure(self) :
        #   Modification de la fenetre
        self.window.title("Thysme | Installer")
        self.window.resizable(False, False)

        #   Placement des elements
        self.button.grid(row=0, column=0, sticky="w")
        self.checkbox.grid(row=1, column=0, sticky="w")
        self.checkboxe.grid(row=2, column=0, sticky="w")
        self.button_start.grid(row=3, column=0, sticky="w")
        self.bouton_annuler.grid(row=3, column=1, sticky="w")

    def hide(self) :
        self.window.withdraw()

    def start(self) :
        self.window.deiconify()
        self.configure()
        #   Lancer la boucle principale de la fenêtre
        self.window.mainloop()

# Définition des fonctions
def create_shortcut(target_path, shortcut_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.save()

# Création des instances
window = Window()

# Lancement des instances
window.hide()
window.start()

exit()