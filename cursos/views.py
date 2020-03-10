from django.shortcuts import render

# Create your views here.
def cursos(request):
    context = {
        "cursos":[
            {
                "nome":"Análise e Desenvolvimento de Sistemas",
                "descricao":"Descrição teste de ADS",
                "link":"ads/"
            },
            {
                "nome":"Sistemas da Informação",
                "descricao":"Descrição teste de SI",
                "link":"si/"
            },
            {
                "nome":"Banco de Dados",
                "descricao":"Descrição teste de BD",
                "link":"bd/"
            },
            {
                "nome":"Gestão em Tecnologia da Informação",
                "descricao":"Descrição teste de GTI",
                "link":"gti/"
            },
        ]
    }
    return render(request, "cursos.html", context)

def curso(request, sigla):
    cursos = {
        "ads":{
            "nome":"Análise e Desenvlvimento de Sistemas",
            "sobre": "Descrição sobre o Curso",
            "periodo":[
                "Matutino | 08h00 às 11:40",
                "Noturno | 19h00 às 23:40"
            ],
            "duracao":"4 Semestres"
        },
        "si":{
            "nome":"Sistemas da Informação",
            "sobre": "Descrição sobre o Curso",
            "periodo":[
                "Matutino | 08h00 às 11:40",
                "Noturno | 19h00 às 23:40"
            ],
            "duracao":"8 Semestres"
        }
    }

    context = {
        "curso":cursos[sigla]
    }
    return render(request, "curso.html", context)