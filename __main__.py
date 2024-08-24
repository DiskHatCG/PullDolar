import requests, os
global api
try:
    api = requests.get("https://dolarapi.com/v1/dolares/blue")
    print("Se obtuvo la API", end="\r")
except:
    print("⛔ | No se puede conectar, verifique su conexión a internet.")
    exit()
def obtenerCompra():
    print(f"\n⌛", end="\r")
    convL = api.json()
    aa = convL.get("compra")
    print("💵 | COMPRA:",aa)
def obtenerVenta():
    print(f"⌛", end="\r")
    asd = api.json()
    aa = asd.get("venta")
    print("💵 | VENTA:",aa)
print("💵 | PullDolar 1.0.0")
print("🚀 | Creado por DiskHat Computing Group")
cont = "DOLAR BLUE"
contCen = cont.center(40, "-")
print(contCen)
obtenerCompra()
obtenerVenta()