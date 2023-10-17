import time, threading  # noqa: E401
#from win10toast import ToastNotifier
from colorama import Fore, Style

color = None
uc = "./config/util_config.txt"
log_file = "./config/log.txt"

def getvalue(var,file) :
    with open(file, "r") as fichier:
        contenu = fichier.read()

    # Recherche de la ligne contenant "variable"
    ligne_variable = [ligne for ligne in contenu.split('\n') if var in ligne]

    # Extraction de la valeur de "variable"
    valeur_variable = ligne_variable[0].split('=')[1].strip()

    # Utilisation de la valeur de "variable"
    return valeur_variable

#config :
clear__log = getvalue("clear__log",uc)
join_thread = getvalue("join_thread",uc)
clear_terminal = getvalue("clear_terminal",uc)
prevention = getvalue("prevention",uc)
say_in_terminal = getvalue("say_in_terminal",uc)

def wait(tiime,function_to_execute_after) :
    thread = threading.Timer(tiime,function_to_execute_after)
    thread.start()
    if join_thread == "True" :  # noqa: E712
        thread.join()

def sleepy(tiime) :
    time.sleep(tiime)

def every(tiime) :
    time.sleep(tiime)

def calendar(where="l") :
    if where == "local" or "l" :
        return time.strftime('%Y-%m-%d', time.localtime())
    if where == "internationnal" or "utc" :
        return time.strftime('%Y-%m-%d', time.gmtime())
    
def clock(where="l") :
    if where == "local" or "l" :
        return time.strftime('%H:%M', time.localtime())
    if where == "internationnal" or "utc" :
        return time.strftime('%H:%M', time.gmtime())

def notif(title,msg,icon=None) :
    #toaster = ToastNotifier() 
    #toaster.show_toast(title, msg, duration=5, icon_path= icon)
    log(2,"On work for linux")

def save(text,file) :
    # Cr�er un fichier et �crire du contenu
    with open(file, "a") as fiile:
        fiile.write(text)

    # Enregistrer un fichier
    fiile.close()

def start(file) :
    exec(open(file).read())

def clear_file(file) :
    with open(file, "w") as file :
        file.write("")
    file.close

def read(file) :
    with open(file,"r") as fiile :
        reading = fiile.read()  # noqa: F841
    return reading

def changevalue(var,new_val,file) :
    with open(file, "r") as filee:
        lignes = filee.readlines()

    with open(file, "w") as filee:
        for ligne in lignes:
            if var in ligne:
                ligne = f"{var} = {new_val}\n"
            filee.write(ligne)

def createvar(var,val,file) :
    with open(file, "r") as filee:
        lignes = filee.readlines()

    with open(file, "w") as filee:
        filee.write(f"{var} = {val}\n")
        for ligne in lignes:
            filee.write(ligne)

def changevar(var,name,value,file) :
    with open(file, "r") as filee:
        lignes = filee.readlines()

    with open(file, "w") as filee:
        for ligne in lignes:
            if var in ligne:
                ligne = f"{name} = {value}\n"
            filee.write(ligne)

def getligne(file) :
    filename = file

    with open(filename, 'r') as fiile:
        lines = fiile.readlines()
        num_lines = len(lines)
    
    return num_lines

def log(state,info) :
    if state == 0 :
        value = "[Info]"
        color = Fore.CYAN
    elif state == 1 :
        value = "[Warn]"
        color = Fore.YELLOW
    elif state == 2 :
        value = "[Error]"
        color = Fore.LIGHTRED_EX
    else :
        log(2,"Niveau d'information non specifier")

    hour = clock("local")

    if say_in_terminal == "True" :
        print(color + f"[{hour}]{value}> {info}" + Style.RESET_ALL)

    save(f"[{hour}]{value}> {info}",log_file)
    save("\n",log_file)

save("\n",log_file)

if say_in_terminal == "True" :
    #clear le terminal
    if clear_terminal == "True" :  # noqa: E712
        for i in range(100) :
            print("")
    #pr�vention xd
    if prevention == "True" :  # noqa: E712
        log(0,f"Log du {calendar()} a {clock()}")
        log(0,"Import d'UTIL reussi")

if clear__log == "True" :  # noqa: E712
    clear_file(log_file)