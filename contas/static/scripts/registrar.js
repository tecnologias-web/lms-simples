var email = document.getElementById("campo-email");
email.onchange = function(){
    var url = "/contas/validar/?email="+this.value;
    var xhttp = new XMLHttpRequest();

    xhttp.open("GET", url, true);
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200) {
            var dados = JSON.parse(this.responseText);
            if(dados.existe == true) {
                alert("Nome de usuário já existe!");
            }
        }
    }
    xhttp.send();
};