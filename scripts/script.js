var nome = "Yuri Dirickson",
    idade = 30,
    cursos = ["ADS", "SI", "BD", "GTI"],
    notas = [
        [7, 4, 9],
        [3, 5, 8], 
        [0, 5, 7], 
        [2, 7.5, 4.5]
    ];

console.log("Aluno: "+nome+" Idade: "+idade);

for (var i = 0; i < cursos.length; i++){
    console.log("-----"+cursos[i]+"-----");
    console.log("Notas: "+notas[i]);
    var notaFinal = 0;
    for (var j = 0; j < notas[i].length; j++){
        notaFinal += notas[i][j];
    }
    notaFinal = notaFinal / notas[i].length;
    console.log("Nota Final: "+notaFinal);
    if(notaFinal >= 6) {
        console.log("Status: APROVADO");
    } else {
        console.log("Status: REPROVADO");
    }
}