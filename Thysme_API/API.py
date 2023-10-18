from flask import Flask, request
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/api/modif')
def modif() :
    g = str(request.args.get('g'))
    k = str(request.args.get('k'))
    nom_fichier = './config/discussion.txt'
    text = f"[{util.clock()}][{k}] > {g} \n"

    util.save(text,nom_fichier)
    util.log(0,"Fichier enregistré avec succès !")

    return 'Fichier modifié avec succès'

@app.route('/api/adduser')
def adduser() :
    username = str(request.args.get('u'))
    password = str(request.args.get('p'))
    
    userid = util.getligne("./config/uesr.txt")

    line = f"\n{username} : {userid} = {password}"
    file = "./config/uesr.txt"

    util.save(line,file)

    return str(userid)

@app.route('/api/getuser')
def getuser() :
    user = util.read("./config/uesr.txt")
    return user

@app.route('/api/read')
def getdisuct() :
    discut = util.read("./config/discussion.txt")
    return discut

if __name__ == '__main__':
    app.run(port="8080")