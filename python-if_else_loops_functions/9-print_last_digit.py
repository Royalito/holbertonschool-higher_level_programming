#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit))

def pow(a, b):
    resultado = 1
    for _ in range(abs(b)):
        resultado *= a
    if b < 0:
        resultado = 1 / resultado
    return resultado

# Ejemplos de uso
print_last_digit(88) # Salida esperada: 8
print_last_digit(0.01) # Salida esperada: 0
print(pow(2, 3)) # Salida esperada: 8
print(pow(10, -2)) # Salida esperada: 0.01
