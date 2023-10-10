let texte;
const cheminFichier = '/config/discussion.txt';

var valueCookie = document.cookie.split('; ').find(cookie => cookie.startsWith('id='));

// Vérifier si valueCookie est définie
if (typeof valueCookie !== 'undefined') {
  // Utiliser la méthode split uniquement si valueCookie est définie
  var cookieValue = valueCookie.split('=')[1];

  // Utiliser la valeur du cookie
  console.log(cookieValue);
  valueCookie = cookieValue;
} else {
  // valueCookie n'est pas définie, faire quelque chose d'autre
  window.location.href = "/fr/login.html";
}

let username_list = [];
let userid_list = [];
let fuck;
//chargement de uesr.txt (les utilisateurs + les mdp + les emails)
$.ajax({
  url: '/config/uesr.txt',
  method: 'GET',
  success: function(data) {
    // Utilise le contenu du fichier ici
    fuck = data.split("\r\n");
    for (let i = 0; i < fuck.length; i += 1) { 
      const parts = fuck[i].split(" = ") ;
      username_list.push(parts[0].split(" : ")[0]);
      userid_list.push(parts[0].split(" : ")[1])
    };
    //datae = parts;
    console.log(`Username : ${username_list}`);
    console.log(`UserID : ${userid_list}`);
  },
  error: function(error) {
    console.error(error);
  }
});


const bouton1 = document.getElementById("envoi");
const input2 = document.getElementById("textinput");
const setting = document.getElementById("Settings");
const langue = document.getElementById("langue");

bouton1.addEventListener("click", function() {
  texte = input2.value;
  input2.value = "";
  modification(texte, convertisseur(valueCookie));
});

setting.addEventListener("click", function() {
    window.location.href = "/fr/setting.html"
});

langue.addEventListener("click", function() {
  window.location.href = "/fr/langue.html"
});

input2.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault(); // Empêche le comportement par défaut de la touche "Entrée"
      texte = input2.value; // Récupère le texte de l'entrée de texte
      // Utilise la précédente valeur "cc"
      input2.value = "";
      modification(texte,convertisseur(valueCookie));
    }
  });

function convertisseur(id) {
    var position = username_list[id];
    return position;
}


function modification(contenu,id) {
    $.ajax({
      url: `http://127.0.0.1:5000/api/modif?g=${contenu}&k=${id}`,
      method: 'GET',
      success: function(data) {
        console.log('Résultat :', data);
      },
      error: function(error) {
        console.error('Une erreur s\'est produite lors de la requête.', error);
      }
    });
  };