import requests
global api
cont = "DOLAR BLUE"
contCen = cont.center(40, "-")
try:
    # Se conecta a la API de DolarAPI, si ocurre algo mostrara un error
    api = requests.get("https://dolarapi.com/v1/dolares/blue")
    print("Se obtuvo la API", end="\r")
except:
    print("⛔ | No se puede conectar, verifique su conexión a internet.")
    exit()
# Funciones obtener compra y venta.
def obtenerCompra():
    print(f"⌛", end="\r")
    convL = api.json()
    lFilt = convL.get("compra")
    print("💵 | COMPRA: $" + str(lFilt))
def obtenerVenta():
    print(f"⌛", end="\r")
    convL = api.json()
    lFilt = convL.get("venta")
    print("💵 | VENTA: $" + str(lFilt))
# Inicio del programa
print("🚀 | PullDolar 1.0.0 | Creado por DiskHat Computing Group")
# Imprime el titulo centrado
print(contCen)
obtenerCompra()
obtenerVenta()