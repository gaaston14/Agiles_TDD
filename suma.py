
def sumar(cadena):
    if cadena == "":
        return 0
    numeros = map(int, cadena.split(","))
    return sum(numeros)
