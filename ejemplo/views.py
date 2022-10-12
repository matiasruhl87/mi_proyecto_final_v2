from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ejemplo/saludar.html",
    {"nombre":"Matias",
    "apellido":"Ruhlmann"}
    )

def index_dos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html",
    {"nombre":nombre,
    "apellido":apellido}
    )

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    {"notas": [1,2,3,4,5,6,7,8]}
    )

def imc(request, peso, altura):
    return render(request, "ejemplo/imc.html",
    {"peso":peso, "altura":altura},
    peso/(altura^2)
    )