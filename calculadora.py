

def calculadora():
    print(" -- Calculadora Basica --")

    try:
        primer_numero = float(input("Primer numero: "))
        segundo_numero = float(input("Segundo numero: "))
        operacion = int(input("Elegi operacion (ingresa numero) - 1. Sumar, 2. Restar, 3. Multiplicar, 4. Dividir: "))

        resultado = calcular(operacion, primer_numero, segundo_numero)

        print(f"Resultado: {resultado}")

    except ZeroDivisionError as e:
        print(f"Dividir por cero es invalido")

    except ValueError as e:
       print(f"Error: {e}")


def calcular(operacion, primer_numero, segundo_numero):
    if operacion == 1:
        return sumar(primer_numero, segundo_numero)
    elif operacion == 2:
        return restar(primer_numero, segundo_numero)
    elif operacion == 3:
        return multiplicar(primer_numero, segundo_numero)
    elif operacion == 4:
        return dividir(primer_numero, segundo_numero)
    else:
        raise ValueError("El numero ingresado no coresponde a una operacion valida")


def sumar(primer_numero, segundo_numero):
    return primer_numero + segundo_numero


def restar(primer_numero, segundo_numero):
    return primer_numero - segundo_numero


def multiplicar(primer_numero, segundo_numero):
    return primer_numero * segundo_numero


def dividir(primer_numero, segundo_numero):
    return primer_numero / segundo_numero


if __name__ == "__main__":
    calculadora()