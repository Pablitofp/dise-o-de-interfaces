from fibonacci import funcion_fibonacci
from fibonacci2 import funcion_fibonacci2

print()

num = int(input("Introduzca numero: "))

print()

print("Opción A: Fibonacci 1.        Opción B: Fibonacci 2.")

print()

op = input("Introduzca opción: ")

print()

if op == 'A' or op == 'a':
    print(funcion_fibonacci2(num))
elif op == 'B' or op == 'b':
    print(funcion_fibonacci(num))

print()