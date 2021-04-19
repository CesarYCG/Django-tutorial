from django.http import HttpResponse #Modulo para retornar al usuario

def saludo(request): #Primera vista
    return HttpResponse("Hola mundo, primer pagina con Django :D")

def despedida(request): #Segunda vista
    return HttpResponse("Adios, estudiante de DJango") 