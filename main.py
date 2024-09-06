import requests
global api, cont, uniapi
uniapi = "https://dolarapi.com/v1/dolares/"
def obtener(tipo, filt): # Funcion obtener
    print(f"⌛", end="\r")
    try:
        api = requests.get(uniapi + tipo ) # Se conecta a la API de DolarAPI, si ocurre algo mostrara un error
        print("Se obtuvo la API", end="\r")
    except:
        print("⛔ | No se puede conectar, verifique su conexión a internet.")
        exit()
    convL = api.json()
    if filt == "compra":
        lFilt = convL.get("compra")
        print("💵 | COMPRA: $" + str(lFilt))
    elif filt == "venta":
            lFilt = convL.get("venta")
            print("💵 | VENTA: $" + str(lFilt))
def main(): # Funcion principal (i) esto podria o va a ser optimizado usando diccionarios.
    selec = input("¿Qué tipo de dolar desea averiguar? \n(Blue / Oficial / Bolsa / Tarjeta / Salir)\nSelección: ")
    if selec.lower() == "blue":
        obtener("blue", "compra")
        obtener("blue", "venta")
    elif selec.lower() == "oficial":
        obtener("oficial", "compra")
        obtener("oficial", "venta")
    elif selec.lower() == "bolsa":
        obtener("bolsa", "compra")
        obtener("bolsa", "venta")
    elif selec.lower() == "tarjeta":
        obtener("bolsa", "compra")
        obtener("bolsa", "venta")
    elif selec.lower() == "salir":
        exit()
    else:
        print("⛔ | El dolar", selec.lower(), "no existe.")
        main()
print("🚀 | PullDolar 2.0.0 | DiskHat Computing Group\n") # Inicio del programa
main() 