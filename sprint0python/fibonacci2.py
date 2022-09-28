def funcion_fibonacci2(num2):

    A = (1 + 5 ** 0.5) / 2

    B = (1 - 5 ** 0.5) / 2

    return int((A ** num2 - B ** num2) / (5 ** 0.5))