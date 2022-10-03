def funcion_fibonacci2(num):

    A = (1 + 5 ** 0.5) / 2

    B = (1 - 5 ** 0.5) / 2

    return int((A ** num - B ** num) / (5 ** 0.5))