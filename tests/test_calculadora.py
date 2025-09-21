import pytest
from calculadora import sumar, dividir, restar, multiplicar

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (9, 3, 12),
        (-5, 5, 0),
        (2.5, 7.5, 10.0),
    ],
)
@pytest.mark.smoke
def test_sumar_positivo(a, b, esperado):
    assert sumar(a, b) == esperado

def test_sumar_negativo():
    with pytest.raises(TypeError):
        sumar("a", 3)

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (9, 3, 6),
        (-5, -5, 0),
        (2.5, 1.2, 1.3),
    ],
)
def test_restar_positivo(a, b, esperado):
    assert restar(a, b) == esperado

def test_restar_negativo():
    with pytest.raises(TypeError):
        restar(5, "b")

def test_multiplicar_positivo(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == 27

def test_multiplicar_negativo():
    with pytest.raises(TypeError):
        multiplicar("a", "b")

def test_dividir_positivo(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 3

def test_dividir_flotantes_positivo(numeros_flotantes):
    a, b = numeros_flotantes
    assert dividir(a, b) == 0.5

@pytest.mark.exception
def test_dividir_negativo():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)

@pytest.fixture
def numeros_enteros():
    return 9, 3

@pytest.fixture
def numeros_flotantes():
    return 0.1, 0.2