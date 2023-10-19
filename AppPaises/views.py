from django.shortcuts import render

def renderMenuPaises(request):
    data = {
        "disable": "not-active",
        "pais": "Toca un país para ver info",
        "anoindependencia": "por definir", 
        "lema": "por definir",
        "continente": "por definir"}
    return render(request, 'productosApp/menupaises.html', data)

def renderMenuChile(request):
    data = {
        "disabled0": "not-active",
        "nombreImagen":"imagenes/chile.png",
        "pais": "Chile",
        "anoindependencia": "1818", 
        "lema": "Por la razón o la fuerza",
        "continente": "Americano"}
    return render(request, 'productosApp/menupaises.html', data)

def renderMenuEspana(request):
    data = {
        "disable1": "not-active",
        "nombreImagen":"imagenes/espana.png",
        "pais": "España", 
        "anoindependencia": "1808", 
        "lema": "Plus ultra",
        "continente": "Europeo",}
    return render(request, 'productosApp/menupaises.html', data)

def renderMenuMexico(request):
    data = {
        "disable2": "not-active",
        "nombreImagen":"imagenes/mexico.png",
        "pais": "Mexico", 
        "anoindependencia": "1821", 
        "lema": "Dios, Patria y Libertad",
        "continente": "Americano",}
    return render(request, 'productosApp/menupaises.html', data)