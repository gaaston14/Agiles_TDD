import pytest
from suma import sumar
def test_sumo_2_string():
    resultado = sumar("2,1")
    assert resultado == 3