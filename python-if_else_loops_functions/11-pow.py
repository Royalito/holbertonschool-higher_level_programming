#!/usr/bin/python3
def pow(a, b):
    resultado = 1
    for _ in range(abs(b)):
        resultado *= a
    if b < 0:
        resultado = 1 / resultado
    return resultado
