def sumar(cadena):
    if cadena == "":
        return 0
    numeros = [int(x) for x in cadena.split(",") if x.strip() != ""]
    return sum(numeros)