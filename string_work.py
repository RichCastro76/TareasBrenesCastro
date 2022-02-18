"""
RICARDO CASTRO BARRENECHEA
JOSE MAURICIO BRENES SILES

TAREA 1

Tipos de Error Globales

*ERROR 1001: Falla interna del programa

*ERROR 1002: El tipo de dato ingresado no es soportado
por el programa

*ERROR 1003: El dato ingresado contiene caracteres
numericos y/o especiales no especificados
en el programa

*ERROR 1004: El dato ingresado resulta fuera del rango

INICIO EJERCICIO 1

se define la funcion la cual se encargará de verificar el tipo de entrada
si esta se compone de unicamente letras, invertira los caracteres
entre mayuscula y minuscula segun corresponda

"""


def string_work(x):
    """
    Se definen los strings correspondientes al abecedario
    Se definen dos contadores:
    *** cont se utilizara en los ciclos para analizar caracter
    por caracter la frase ingresada
    *** cont1 se utilizara en los ciclos para analizar los
    abecedarios caracter por caracter segun sea requerido
    """
    Mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    Minusculas = "abcdefghijklmnñopqrstuvwxyz"
    cont = 0
    cont1 = 0
    Error = ""
    """
    *** correcto es una variable que aumentará si se encuentra
    que una letra fue invertida entre mayuscula y minuscula o
    viceversa segun corresponda
    """
    correcto = 0

    """
    Se inicia un condicional para verificar que el
    input sea un string con la funcion type
    """
    if type(x) == str:
        """
        Se inicia un condicional para verificar que el input
        sea unicamente letras con la funcion isalpha
        """
        if x.isalpha():
            """
            #Se invierten los caracteres del input ingresado como
            variable x y se guardan en la variable y
            """
            y = x.swapcase()
            """
            ***se inicializa un ciclo while para verificar que
            la funcion swapcase haya funcionado correctamente
            ***se utiliza el contador cont y se compara contra
            el largo del string original para evitar que el ciclo
            se vuelva infinito
            """
            while cont < len(x):

                """
                ***se inicializa un ciclo para verificar el estado de
                los caracteres del input inicial "x" y de su hipotetica
                inversion "y"
                ***se utiliza el contador cont1 y las 27 letras del
                abecedario en espanol como condiciones del ciclo
                """
                while cont1 < 27:
                    if x[cont] == Mayusculas[cont1]:
                        """
                        #Se compara cada letra del string ingresado con el
                        abecedario mayusculas
                        #se utiliza la posicion de donde se hallo
                        la mayuscula para comparar el hipotetico "y"
                        con el abecedario en minusculas
                        #Si se encuentra coincidencia
                        se aumenta la variable correcto
                        """
                        if y[cont] == Minusculas[cont1]:
                            correcto = correcto+1
                            cont1 = cont1+1
                            print(x[cont], "->", y[cont])
                    elif x[cont] == Minusculas[cont1]:
                        """
                        Se compara cada letra del string ingresado
                        con el abecedario minusculas
                        se utiliza la posicion de donde se hallo
                        la minuscula para comparar el hipotetico "y"
                        con el abecedario en mayusculas
                        Si se encuentra coincidencia
                        se aumenta la variable correcto
                        """
                        if y[cont] == Mayusculas[cont1]:
                            correcto = correcto + 1
                            cont1 = cont1 + 1
                            print(x[cont], "->", y[cont])
                    else:
                        cont1 = cont1+1
                cont = cont+1
                """
                se resetea el cont1
                """
                cont1 = 0
                """
                Una vez acabada la revision de caracteres,
                si la cantidad de datos correctamente invertidos
                es igual al largo de la frase ingresada retornara
                un "Completo" y la frase traducida
                """
            if correcto == len(y):
                print("Completo")
                print(correcto)
                print(y)
                return True
            else:
                """
                En caso de que la frase salga erroneamente traducida,
                retornará un resultado de "Error
                """
                Error = 1001
                print("ERROR N°", Error)
                return False
        else:
            Error = 1002
            print("ERROR CODE N°", Error)
            return False
    else:
        Error = 1003
        print("ERROR CODE N°", Error)
        return False
