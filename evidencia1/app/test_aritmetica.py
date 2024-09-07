import aritmetica

def test_suma():
    assert aritmetica.suma(1.5, 2.5) == 4.0
    assert aritmetica.suma(-1.5, 1.5) == 0.0
    assert aritmetica.suma(10, 20) == 30.0

def test_resta():
    assert aritmetica.resta(10, 5) == 5.0
    assert aritmetica.resta(3, 2.5) == 0.5
    assert aritmetica.resta(-5, -5) == 0.0

def test_div():
    assert aritmetica.div(10, 2) == 5.0
    assert aritmetica.div(9, 3) == 3.0
    assert aritmetica.div(7.5, 2.5) == 3.0

def test_mult():
    assert aritmetica.mult(3, 4) == 12.0
    assert aritmetica.mult(2.5, 2) == 5.0
    assert aritmetica.mult(-3, 3) == -9.0

def test_sumar_n():
    assert aritmetica.sumar_n(1, 2, 3) == 6.0
    assert aritmetica.sumar_n(1.5, 2.5, 3.5) == 7.5
    assert aritmetica.sumar_n(-1, 0, 1) == 0.0

def test_promedio():
    assert aritmetica.promedio(2, 4, 6) == 4.0
    assert aritmetica.promedio(1, 2, 3, 4, 5) == 3.0
    assert aritmetica.promedio(10, 20, 30) == 20.0

# Ejecutar todas las pruebas
if __name__ == "__main__":
    test_suma()
    test_resta()
    test_div()
    test_mult()
    test_sumar_n()
    test_promedio()
    print("Todas las pruebas pasaron correctamente.")