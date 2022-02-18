from asyncio.windows_events import NULL


error = 0


def DeterminaSiEsNumeroValido(Entrada):  # Determina si el mensaje es una
    # letra o un numero.

    Resultado1 = bool

    if Entrada.isdigit() is False:
        Resultado1 = True  # El mensaje es una letra
        error = 1003
        print("ERROR:" + str(error))
        return Resultado1
    elif 0 <= int(Entrada) <= 99:
        Resultado1 = False  # El mensaje es un numero valido
        return Resultado1
    else:
        Resultado1 = True  # El mensaje NO es un numero valido
        error = 1004
        print("ERROR:" + str(error))
        return Resultado1


def DeterminaSiEntraEnRango(Entrada):  # Determina si el mensaje ingresado
    # se encuentra entre 0 y 99

    Resultado2 = bool

    if Entrada.isdigit() is False:
        Resultado2 = False  # Es False si el mensaje no es un numero
        error = 1003
        print("ERROR:" + str(error))
        return Resultado2

    elif 0 <= int(Entrada) <= 99:
        Resultado2 = True  # Es True si el mensaje es un numero entero entre
        #  0 y 99
        return Resultado2

    else:
        Resultado2 = False  # Es False si el mensaje no es un numero entero
        # entre 0 y 99
        error = 1004
        print("ERROR:" + str(error))
        return Resultado2


def RetornaNumeroEnTexto(Entrada):  # Toma el mensaje ingresado y si es un
    # numero devuelve su nombre.

    NumeroTexto = ""  # Se crea una variable para almacenar
    # el nombre del numero
    i = 0  # Se crea una variable para almacenar el valor integer del numero
    j = NULL  # En caso de que el mensaje no sea un numero o no este entre
    # 0 y 99, el programa va a devolver un error

    NombresNumeros = ["Cero", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis",
                      "Siete", "Ocho", "Nueve", "Diez", "Once", "Doce",
                      "Trece", "Catorce", "Quince", "Dieciseis", "Diecisiete",
                      "Dieciocho", "Diecinueve", "Veinte", "Veinte_y_uno",
                      "Veinte_y_dos", "Veinte_y_tres", "Veinte_y_cuatro",
                      "Veinte_y_cinco", "Veinte_y_seis", "Veinte_y_siete",
                      "Veinte_y_ocho", "Veinte_y_nueve", "Treinta",
                      "Treinta_y_uno", "Treinta_y_dos", "Treinta_y_tres",
                      "Treinta_y_cuatro", "Treinta_y_cinco",
                      "Treinta_y_seis", "Treinta_y_siete", "Treinta_y_ocho",
                      "Treinta_y_nueve", "Cuarenta", "Cuarenta_y_uno",
                      "Cuarenta_y_dos", "Cuarenta_y_tres", "Cuarenta_y_cuatro",
                      "Cuarenta_y_cinco", "Cuarenta_y_seis",
                      "Cuarenta_y_siete", "Cuarenta_y_ocho",
                      "Cuarenta_y_nueve", "Cincuenta", "Cincuenta_y_uno",
                      "Cincuenta_y_dos", "Cincuenta_y_tres",
                      "Cincuenta_y_cuatro", "Cincuenta_y_cinco",
                      "Cincuenta_y_seis", "Cincuenta_y_siete",
                      "Cincuenta_y_ocho", "Cincuenta_y_nueve", "Sesenta",
                      "Sesenta_y_uno", "Sesenta_y_dos", "Sesenta_y_tres",
                      "Sesenta_y_cuatro", "Sesenta_y_cinco", "Sesenta_y_seis",
                      "Sesenta_y_siete", "Sesenta_y_ocho", "Sesenta_y_nueve",
                      "Setenta", "Setenta_y_uno", "Setenta_y_dos",
                      "Setenta_y_tres", "Setenta_y_cuatro",
                      "Setenta_y_cinco", "Setenta_y_seis", "Setenta_y_siete",
                      "Setenta_y_ocho", "Setenta_y_nueve", "Ochenta",
                      "Ochenta_y_uno", "Ochenta_y_dos", "Ochenta_y_tres",
                      "Ochenta_y_cuatro", "Ochenta_y_cinco", "Ochenta_y_seis",
                      "Ochenta_y_siete", "Ochenta_y_Ocho", "Ochenta_y_nueve",
                      "Noventa", "Noventa_y_uno", "Noventa_y_dos",
                      "Noventa_y_tres", "Noventa_y_cuatro", "Noventa_y_cinco",
                      "Noventa_y_seis", "Noventa_y_siete", "Noventa_y_ocho",
                      "Noventa_y_nueve"]
    # Es una lista que contiene los nombres de los numeros del 0 al 99

    if Entrada.isdigit() and 0 <= int(Entrada) <= 99:
        # Verifica que el mensaje ingresado sea un numero y que se encuentre
        # entre 0 y 99
        i = int(Entrada)
        NumeroTexto = NombresNumeros[i]
        return NumeroTexto

    else:  # Para cualquier otro caso devuelve un mensaje vacio
        error = 1002
        print("ERROR:" + str(error))
        return j
