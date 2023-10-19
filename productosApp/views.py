from django.shortcuts import render

def renderInicio(request):
    return render(request, 'productosApp/inicio.html')

def renderMenuElectronica(request):
    data = {"tipo": "Electronica", "cardUnoNombre": "Mac", "cardDosNombre": "Iphone", "cardTresNombre": "Playstation"}
    return render(request, 'productosApp/menu.html', data)

def renderMenuJuguetes(request):
    data = {"tipo": "Juguetes", "cardUnoNombre": "Auto", "cardDosNombre": "Pelota de futbol", "cardTresNombre": "Figura de acción"}
    return render(request, 'productosApp/menu.html', data)

def renderMenuRopa(request):
    data = {"tipo": "Ropa", "cardUnoNombre": "Pantalones", "cardDosNombre": "Chaqueta", "cardTresNombre": "Camisa"}
    return render(request, 'productosApp/menu.html', data)