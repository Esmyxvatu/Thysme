let username_list = [];
let userid_list = [];
let password_list = [];
let fuck;
let id;


var dateExpiration = new Date();
dateExpiration.setFullYear(dateExpiration.getFullYear() + 10);

//chargement de uesr.txt (les utilisateurs + les mdp + les emails)
$.ajax({
  url: '/config/uesr.txt',
  method: 'GET',
  success: function(data) {
    // Utilise le contenu du fichier ici
    fuck = data.split("\r\n");
    for (let i = 0; i < fuck.length; i += 1) { 
      const parts = fuck[i].split(" = ") ;
      password_list.push(parts[1]);
      username_list.push(parts[0].split(" : ")[0]);
      userid_list.push(parts[0].split(" : ")[1])
    };
    //datae = parts;
    console.log(`Username : ${username_list}`);
    console.log(`UserID : ${userid_list}`);
    console.log(`Password : ${password_list}`)
  },
  error: function(error) {
    console.error(error);
  }
});

function setcookie(nomCookie, id) {
    document.cookie = nomCookie + "=" + id + "; expires=" + dateExpiration + "; path=/";
};

function adduser(username, password) {
    $.ajax({
        url: `http://127.0.0.1:5000/api/adduser?u=${username}&p=${password}`,
        method: 'GET',
        success: function(data) {
          console.log('Résultat :', data);
          id = data;
            setcookie("id",id);
            setcookie("co","y");
        },
        error: function(error) {
          console.error('Une erreur s\'est produite lors de la requête.', error);
        }
      });
};
  


//DEBUT DE LA MERDE INCOMPREHENSIBLE !


document.getElementById("login").addEventListener("click", function() {
    var password = document.getElementById("password").value;
    var password_confirm = document.getElementById("password_confirm").value;
    var username = document.getElementById("username").value;

    console.log(`Username : ${username} ; Password : ${password} ; Password (confirmation) : ${password_confirm}`);

    if (password === password_confirm) {

        if (username_list.includes(username)) {
            console.log("Nom d'utilisateur deja pris");
        } else {
            adduser(username,password);
            window.location.href = "/fr/acceuil.html";
        }

    } else {
        console.log("Merci de faire correspondre les mdp");
    };

});