import tkinter as tk #noqa:F401
import util, fenetre, requests #noqa:E401

connected = util.getvalue("connected", "config\conf.txt")
UserID = util.getvalue("UserID", "config\conf.txt")

username = requests.get("http://127.0.0.1:8080/api/getuser").text

un = username.split("\n")
usn = un[int(UserID)].split(" : ")[0]

acceuil = fenetre.Acceuil()
login = fenetre.Login()

if connected == "True" :
    acceuil.start(username=usn)
else :
    login.start()
