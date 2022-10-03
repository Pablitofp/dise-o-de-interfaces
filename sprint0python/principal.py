from fibonacci import funcion_fibonacci
from fibonacci2 import funcion_fibonacci2
import time

print()

num = int(input("Introduzca número: "))

print()

print("Opción A: Fibonacci 1.        Opción B: Fibonacci 2.")

print()

op = input("Introduzca opción: ")

print()

if op == 'A' or op == 'a':
    start_time = time.time()
    print(funcion_fibonacci(num))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')
elif op == 'B' or op == 'b':
    start_time = time.time()
    print(funcion_fibonacci2(num))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')
print()