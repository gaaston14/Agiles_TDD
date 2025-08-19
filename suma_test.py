import pytest
from suma import sumar

def test_sumo_2_string():
    resultado = sumar("2,1")
    assert resultado == 3

def test_sumo_valores_vacios():
    resultado = sumar("")
    assert resultado == 0

def test_sumo_numero_y_valor_vacio():
    resultado = sumar("5,")
    assert resultado == 5

def test_sumo_valor_vacio_y_numero():
    resultado = sumar(",3")
    assert resultado == 3

def test_sumo_valor_negativo():
    resultado = sumar("-1,2")
    assert resultado == 1

def test_sumo_negativo_primero():
    resultado = sumar("-2,1")
    assert resultado == -1