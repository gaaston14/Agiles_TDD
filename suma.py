
def sumar(cadena):
    if cadena == "":
        return 0
    if cadena.endswith(","):
        cadena = cadena[:-1]
    numeros = map(int, cadena.split(","))
    return sum(numeros)
