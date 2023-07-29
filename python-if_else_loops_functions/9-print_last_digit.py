#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit)

# Ejemplo de uso
print_last_digit(12345)  # Salida esperada: 5
print_last_digit(-987)   # Salida esperada: 7
print_last_digit(100)
