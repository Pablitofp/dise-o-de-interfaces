puntuacion = 0


print()
print("Cada respuesta correcta suma 10 puntos.")
print("Cada respuesta incorrecta resta 5 puntos.")
print("La puntuación se mostrará al finalizar las preguntas.")


print()
print()
print("¿Cuántas asignaturas tenemos?")
print()
print("Opción A: Cinco asignaturas.             Opción B: Seis asignaturas.              Opción C: Siete asignaturas.")


print()
respuesta = input("Respuesta: ")


if respuesta == 'a':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5
elif respuesta == 'A':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5
elif respuesta == 'b':
    print("Respuesta correcta")
    puntuacion = puntuacion + 10
elif respuesta == 'B':
    print("Respuesta correcta")
    puntuacion = puntuacion + 10
elif respuesta == 'c':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5
elif respuesta == 'C':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5



print()
print()
print("¿En qué año se decubrió América?")
print()
print("Opción A: 1492.                          Opción B: 1942.                          Opción C: 492")


print()
respuesta = input("Respuesta: ")


if respuesta == 'a':
    print("Respuesta correcta")
    puntuacion = puntuacion + 10
elif respuesta == 'A':
    print("Respuesta correcta")
    puntuacion = puntuacion + 10
elif respuesta == 'b':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5
elif respuesta == 'B':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5
elif respuesta == 'c':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5
elif respuesta == 'C':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5


print()
print()
print("¿Cuánto es 50 + 44?")
print()
print("Opción A: 84.                            Opción B: 6.                             Opción C: 94")


print()
respuesta = input("Respuesta: ")


if respuesta == 'a':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5
elif respuesta == 'A':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5
elif respuesta == 'b':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5
elif respuesta == 'B':
    print("Respuesta incorrecta")
    puntuacion = puntuacion - 5
elif respuesta == 'c':
    print("Respuesta correcta")
    puntuacion = puntuacion + 10
elif respuesta == 'C':
    print("Respuesta correcta")
    puntuacion = puntuacion + 10


puntuacion = str(puntuacion)


print()
print()
print('Has obtenido ' + puntuacion + ' puntos.')
print()
print()