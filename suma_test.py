import pytest
from suma import sumar

def test_sumo_2_string():
    resultado = sumar("2,1")
    assert resultado == 3

def test_sumo_valores_vacios():
    resultado = sumar("")
    assert resultado == 0