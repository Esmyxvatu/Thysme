//chargement de variable random
let password_list = [];
let username_list = [];
let userid_list = [];
var a, e, f, unte, passwordee, fuck, userid, useridtest, id;
let conf_lol = "";
let conected = "";
const MonScript = document.getElementById("theme")
var valueCookie = document.cookie.split('; ').find(cookie => cookie.startsWith('id='));
var valueCookieConnection = document.cookie.split('; ').find(cookie => cookie.startsWith('co='));

//definition du cookie :)
var dateExpiration = new Date();
dateExpiration.setFullYear(dateExpiration.getFullYear() + 10);


// Vérifier si valueCookie est définie
if (typeof valueCookie !== 'undefined') {
  // Utiliser la méthode split uniquement si valueCookie est définie
  var cookieValue = valueCookie.split('=')[1];

  // Utiliser la valeur du cookie
  console.log(cookieValue);
  valueCookie = cookieValue;
} else {
  // valueCookie n'est pas définie, faire quelque chose d'autre
  console.log("le cookie n'existe pas :(");
}

// Vérifier si valueCookie est définie
if (typeof valueCookieConnection !== 'undefined') {
  // Utiliser la méthode split uniquement si valueCookie est définie
  var cookieValueConnection = valueCookieConnection.split('=')[1];

  // Utiliser la valeur du cookie
  console.log(cookieValueConnection);
  valueCookieConnection = cookieValueConnection;
  if (valueCookieConnection === "y") {
    window.location.href = "/fr/acceuil.html";
  }
} else {
  // valueCookie n'est pas définie, faire quelque chose d'autre
  console.log("le cookie n'existe pas :(");
}

//verification du chargement des DOM
document.addEventListener("DOMContentLoaded", function() {
  console.log("DOM chargé :)")
});

//création d'une fonction qui va mettre un cookie sur le naviguateur
function setcookie(nomCookie, id) {
  document.cookie = nomCookie + "=" + id + "; expires=" + dateExpiration + "; path=/";
};

//definition de tt ce qui peut etre modifier plus tard
document.getElementById("username").value = "";
document.getElementById("password").value = "";
const message = document.getElementById("message");

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
      password_list.push(parts[1]);
    };
    //datae = parts;
    console.log(`Username : ${username_list}`);
    console.log(`Password : ${password_list}`);
    console.log(`UserID : ${userid_list}`);
  },
  error: function(error) {
    console.error(error);
  }
});

//si on clique sur le bouton login il charge tout le process en dessous
document.getElementById("login").addEventListener("click", function() {
    var pswd = document.getElementById("password").value;
    var username = document.getElementById("username").value;

    //verification de l'existence du nom d'utilisateur
    for (let unt = 0; unt < username_list.length; unt += 1) {
      let username_trye = username_list[unt];
      let username_try = username_trye.trim();
      console.log(username_try);
      if (username === username_try) {
        console.log(username_try); // Affiche "Esmyx"
        e = 1;
        unte = unt;
        useridtest = username_list.indexOf(username_try);
        useridtest = userid_list[useridtest];
        break;
      } else if (username !== username_try) {
        console.log("Error mauvais nom d'utilisateur (" + username_try + ")");
        e = 0;
      }
    }

    if (e === 0) {
      //affichage d'un msg
      message.style.display = "block";
      message.textContent = "Mauvais nom d'utilisateur";
      
      setTimeout(function() {
        message.style.display = "none";
      }, 2000);
    }

    //verification du mot de passe
    for (let passworde = 0; passworde < password_list.length; passworde += 0) {
      let password_try = password_list[passworde];
      console.log(password_try);
      if (pswd === password_try) {
        console.log(password_try); // Affiche "pswd"
        a = 1;
        passwordee = passworde;
        break;
      } else {
        console.log("Error mauvais mot de passe " + password_try);
        a = 0;
      }
    }

    //affichage d'un msg si il y a une erreur
    if (a === 0) {
      message.style.display = "block";
      message.textContent = "Mauvais mot de passe";

      setTimeout(function() {
        message.style.display = "none";
      }, 2000);
    }

    //verification du fait que le mdp est bien celui de l'utilisateur demandé
    if (a === 1 && e === 1) {
      f = password_list.indexOf(passwordee);
      unte = username_list.indexOf(unte);
      if (unte  === f) {
        for (i in userid_list) {
          let ntmfdp = userid_list[i];
          if (ntmfdp === useridtest) {
            id = userid_list[i];
            console.log(id);
            break;
          };
        };
        window.location.href = "/fr/acceuil.html";
        setcookie("id",id);
        setcookie("co","y");
      } else {
        console.log("Réessayer :)");
      }
    } else {
      console.log("a (mot de passe) = " + a + "; e (nom d'utilisateur) = " + e);
      console.log("Reessayer :)");
    };
});