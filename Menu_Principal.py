import os
import time
from Submenu import SubMenu
from Modulo.funcionesMatemáticas import *
from Paquete.funcionesCadena import contarLetras
from Paquete.funcionesNumericas import *

sub = SubMenu()
lista_menu = ["1) Hola Mundo","2) Variables","3) Conversiones", "4) Operaciones Matemáticas","5) Concatenación","6) Funciones de Cadenas","7) Tuplas","8) Listas","9) Diccionarios","10) Lectura de Datos por Teclado","11) Estructura Condicional IF,ELSE,ELIF","12) Funciones","13) Operadores Lógicos (And - Or -Not)",
              "14) Operador Ternario","15) If con Tuplas & Listas (IF - IN)","16) Función Range","17) Bucle For","18) Factorial","19) Bucle While", "20) Sentencias Break, Continue, Pass","21) Generadores (Cláusula yield)","22) Generadores (Cláusula yield from)","23) Bloque (TRY EXCEPT FINALLY)",
              "24) Sentencia RAISE","25) Módulos","26) Paquetes","27) Clases y Objetos","28) Constructor de Clase","29) Encapsulamiento de Variables de Clase","30) Encapsulamiento de Métodos de Clase", "31) Métodos Accesores (GET - SET)","32) Método de Clase __str__","33) Herencia","34) Método super()","35) Principio de Sustitución entre Clases","36) Herencia Múltiple",
              "37) Polimorfismo", "38) Relaciones entre Clases","39) Salir del Menú"]
alternativa = ""

os.system("cls")
while alternativa != "39":
    alternativa = sub.menu_main(lista_menu,"Menú Principal de Ejercicios en PYTHON")
    os.system("cls")
    if alternativa == "1":
        alternativa1 = ""
        while alternativa1 != "2":
            os.system("cls") 
            alternativa1 = sub.menu(["1) Imprimir Mensaje","2) Salir..."],"Mensaje")
            os.system("cls") 
            if alternativa1 == "1":
                print("-"*10,"Hola Mundo","-"*10)
                time.sleep(1.2)
        
            elif alternativa1 == "2":
                print("Saliendo de la opción 1...")
                time.sleep(1.5)
                os.system("cls")
                
                
        
       
    elif alternativa == "2":
        os.system("cls")
        alternativa1 = ""
        while alternativa1 != "5":
            os.system("cls")
            alternativa1 = sub.menu(["1) Presentar Nombre","2) Presentar Edad","3) Presentar Valor Booleano","4) Presentar Sueldo","5) Salir..."],"Variables")
            os.system("cls")
            if alternativa1 == "1":
                nombre = "Carlos Molina"
                print("Mi nombre es: {}".format(nombre))
                time.sleep(1.3)
              
            elif alternativa1 == "2":
                edad = 20
                print("Mi edad es: {}".format(edad))
                time.sleep(1.3)
               
            elif alternativa1 == "3":
                edad = True
                print("Valor: {}".format(edad))
                time.sleep(1.3)
                os.system("cls")
                
            elif alternativa1 == "4":
                sueldo = 425.45
                print("El sueldo es de: ${}".format(sueldo))
                time.sleep(1.3)
                os.system("cls")
                
            elif alternativa1 == "5":
                print("Saliendo de la opción 2...")
                time.sleep(1.5)
                os.system("cls")
    
    elif alternativa == "3":
        alternativa1 = ""
        os.system("cls")
        while alternativa1 != "6":
            alternativa1 = sub.menu(["1) Concatenación","2) Conversión de String a Int","3) Conversión de Float a Int","4) Conversión de String a Float","5) Longitud de una Cadena de Caracteres","6) Salir..."],"Conversiones")
            os.system("cls")
            if alternativa1 == "1":
                a = "Buenos Días, "
                b = "Andrea."
                print("La concatenación es: {}".format(a+b))
                time.sleep(2)
                os.system("cls")
               
            elif alternativa1 == "2":
                num1 = "40"
                num2 = "35"
                print("El valor concatenado es: {}".format(num1+num2))
            
                número1 = int(num1)
                número2 = int(num2)
                print("Al convertir los string a int, el resultado de la suma es: {}".format(número1 + número2))
                time.sleep(2)
                os.system("cls")
            
            elif alternativa1 == "3":
                sueldo = 340.34
                print("El sueldo es: ${}".format(sueldo))

                sueldo1 = int(sueldo)
                print("Al convertir de float a int, el sueldo sería: ${}".format(sueldo1))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "4":
                valor = "876.67"
                print("El tipo de dato de {} es: {}".format(valor, type(valor)))
                valordecimal = float(valor)
                print("Al realizar la conversión, {} ahora es del tipo: {}".format(valor,type(valordecimal)))
                time.sleep(2)
                os.system("cls")

            elif alternativa1 == "5":
                frase = "Hola, soy admin"
                print("La longitud de la frase '{}' es de: {}".format(frase,len(frase)),"caracteres")
                time.sleep(2)
                os.system("cls")
            
            elif alternativa1 == "6":
                print("Saliendo de la opción 3...")
                time.sleep(1.5)
                os.system("cls")
                
    
    elif alternativa == "4":
        alternativa1 = ""
        os.system("cls")
        while alternativa1 != "8":
            alternativa1 = sub.menu(["1) Presentación de Distintos Datos Numéricos","2) Suma","3) Resta","4) Multiplicación","5) División Entera","6) División Exacta","7) Potencia","8) Salir..."],"Operaciones Matemáticas")
            os.system("cls")
            if alternativa1 == "1":
                entero = 10
                print("El valor entero es: {}".format(entero))
                decimal = 20.30
                print("El valor decimal es: {}".format(decimal))
                complejo = 14 + 6j
                print("El valor complejo es: {}".format(complejo))
                booleano = True
                print("El valor booleano es: {}".format(booleano))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "2":
                a = 40
                b = 65
                suma = a + b
                print("La suma de {} + {} es: {}".format(a,b,suma))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "3":
                a = 56
                b = 12
                resta = a - b
                print("La resta de {} - {} es: {}".format(a,b,resta))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "4":
                c = 12
                d = 12
                mult = c * d
                print("La multiplicación entre {} * {} es: {}".format(c,d,mult))
                time.sleep(2)
                os.system("cls")
            
            elif alternativa1 == "5":
                c = 35
                d = 5
                div_ent = c / d
                print("La división entera entre {} y {} es: {}".format(c,d,div_ent))
                time.sleep(2)
                os.system("cls")
            
            elif alternativa1 == "6":
                var1 = 35
                var2 = 5
                div_ent = c // d
                print("La división exacta entre {} y {} es: {}".format(c,d,div_ent))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "7":
                base = 3
                exponente = 4
                potencia = base ** exponente
                print("La potencia de elevar {} a la {} es: {}".format(base,exponente,potencia))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "8":
                print("Saliendo de la opción 4...")
                time.sleep(1.5)
                os.system("cls")
                
    
    elif alternativa == "5":
        texto1 = "Hola,"
        texto2 = "buenas noches."
        alternativa1 = ""
        os.system("cls")
        while alternativa1 != "5":
            alternativa1 = sub.menu(["1) Primera Forma de Concatenar","2) Uso de Comodines","3) Uso de la función format","4) Mediante Alias o Asignación de Variable","5) Salir..."],"Formas de Concatenar Cadenas")
            os.system("cls")
            if alternativa1 == "1":
                textfinal = texto1 + " " + texto2
                print(textfinal)
                time.sleep(2)
                os.system("cls")

            elif alternativa1 == "2":
                print("La frase concatenada mediante comodines es: %s %s" % (texto1,texto2))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "3":
                saludoFinal = "La frase concatenada mediante format es: {} {} ".format(texto1,texto2)
                print(saludoFinal)
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "4":
                saludoFinal2 = "La frase concatenada mediante alias o asignación de variable es: {x} {y}".format(x=texto1,y=texto2)
                print(saludoFinal2)
                time.sleep(2)
                os.system("cls")
            
            elif alternativa1 == "5":
                print("Saliendo de la opción 5...")
                time.sleep(1.5)
                os.system("cls")
                
                
    elif alternativa == "6":
        texto = "O mueres como un héroe o vives lo suficiente para verte convertido en un villano"
        alternativa1 = ""
        os.system("cls")
        while alternativa1 != "10":
            alternativa1 = sub.menu(["1) Cadena","2) Función .lower()","3) Función .upper()","4) Función .title()","5) Función .find()","6) Función .count()","7) Función .replace()","8) Función .isnumeric()","9) Función .split()","10) Salir..."],"Funciones de Cadenas")
            os.system("cls")
            if alternativa1 == "1":
                print("La cadena es: {}".format(texto)) 
                time.sleep(2)
                os.system("cls")
            elif alternativa1 == "2":
                print("Cadena en minúscula: {}".format(texto.lower()))
                time.sleep(2)
                os.system("cls")
            elif alternativa1 == "3":
                print("Cadena en mayúscula: {}".format(texto.upper()))
                time.sleep(2)
                os.system("cls")
            elif alternativa1 == "4":
                print("Cadena usando la función title(): {}".format(texto.title()))
                time.sleep(2)
                os.system("cls")
            elif alternativa1 == "5":
                print("La posición en que se encuentra la palabra 'como' en el texto es: Posición {}".format(texto.find("como")))
                time.sleep(2)
                os.system("cls")
            elif alternativa1 == "6":
                print("Las veces que se repite la vocal 'o' es de: {} veces".format(texto.count("o")))
                time.sleep(2)
                os.system("cls")
                   
            elif alternativa1 == "7":
                textfinal = texto.replace("O", "o")
                print("El texto modificado es: {}".format(textfinal))
                time.sleep(2)
                os.system("cls")
            
            elif alternativa1 == "8":
                valor = texto.isnumeric()
                print("¿El texto es numérico?: {}".format(valor))
                time.sleep(2)
                os.system("cls")
            
            elif alternativa1 == "9":
                separate = texto.split(" ")
                print(separate)
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "10":
                print("Saliendo de la opción 6...")
                time.sleep(1.5)
                os.system("cls")

    elif alternativa == "7":
        alternativa1 = ""
        os.system("cls")
        while alternativa1 != "10":
            alternativa1 = sub.menu(["1) Presentar una Tupla","2) Datos de distintos tipos en una tupla","3) Tupla dentro de otra tupla","4) Acceder a los elementos de una tupla","5) Obtener un rango de elemento específico","6) Tuple Unpacking (Desempaquetado de una tupla)",
                                     "7) Concatenar Tuplas","8) Función .count()","9) Función .index()","10) Salir..."],"Manejo de Tuplas")
            os.system("cls")
            if alternativa1 == "1":
                tupla = (1,2,3)
                print("La tupla es: {}".format(tupla))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "2":
                tupla2 = (45,"Andrés",False,["a","b","c"],367.89)
                print("La tupla 2 es: {}".format(tupla2))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "3":
                tupla3 = (3,6,9,("a","b","c"))
                print("La tupla 3 es: {}".format(tupla3))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "4":
                tupla4 = ("manzana","pera","uva")
                print("La tupla 4 es: {}".format(tupla4))
                ind = tupla4[0]
                print("El elemento que se encuentra en la posición 0 de la tupla es: {}".format(ind))
                ind2 = tupla4[-1]
                print("El último elemento de la tupla es: {}".format(ind2))
                ind3 = tupla4[-2]
                print("El penúltimo elemento de la tupla es: {}".format(ind3))
                time.sleep(4)
                os.system("cls")
                
            elif alternativa1 == "5":
                tupla5 = (50,"Fernanda",True,["a","b","c"],367.89,"sandía")
                print("La tupla original es: {}".format(tupla5))
                ind4 = tupla5[0:4]
                print("Los elementos de la tupla que se encuentran en el rango de [0:4] es: {}".format(ind4))
                time.sleep(4)
                os.system("cls")
                
            elif alternativa1 == "6":
                tupla6 = ("agua","café","batido")
                a,b,c = tupla6
                print("A la variable 'a' se le asigna el elemento *{}* de la tupla.".format(a))               
                print("A la variable 'b' se le asigna el elemento *{}* de la tupla.".format(b))                
                print("A la variable 'c' se le asigna el elemento *{}* de la tupla.".format(c))                
                time.sleep(5)
                os.system("cls")
                
            elif alternativa1 == "7":
                tupla6 = ("agua","café","batido")
                tupla4 = ("manzana","pera","uva")
                
                tuplafinal = tupla4 + tupla6
                print("La tupla4 es: {}".format(tupla4))
                print("La tupla6 es: {}".format(tupla6))
                print("La nueva tupla ahora es: {}".format(tuplafinal))
                time.sleep(4)
                os.system("cls")
                
            elif alternativa1 == "8":
                tupla6 = ("agua","café","batido")
                tupla4 = ("manzana","pera","uva")
                
                tuplafinal = tupla4 + tupla6
                print("¿Cuántas veces aparece el elemento 2 en la tupla?: {} veces".format(tuplafinal.count(2)))
                time.sleep(2)
                os.system("cls")
                
            elif alternativa1 == "9":
                tupla6 = ("agua","café","batido","jugo")
                tupla4 = ("manzana","pera","uva","manzana")
                
                tuplafinal = tupla4 + tupla6
                print("La tupla es: {}".format(tuplafinal))
                print("El índice de la primera ocurrencia del elemento 'manzana' es: {}".format(tuplafinal.index("manzana")))
                time.sleep(3)
                os.system("cls")
                
            elif alternativa1 == "10":
                print("Saliendo de la opción 7...")
                time.sleep(1.5)
                os.system("cls")
                
    
    elif alternativa == "8":
        lista = ["a","b","c","fresa",456.89,("c","d","e"),True]
        alternativa1 = ""
        os.system("cls")
        while alternativa1 !="13":
                alternativa1 = sub.menu(["1) Presentar una Lista","2) Acceder a los elementos de una lista","3) Obtener un rango de elemento específico","4) Función .append()","5) Función .insert()","6) Función .extend()",
                                         "7) Función .index()","8) Función .remove()","9) Función .pop()","10) Concatenar Listas","11) Operar una lista","12) Comprobar si un elemento se encuentra en la lista",
                                         "13) Salir..."],"Manejo de Listas")
                os.system("cls")
                if alternativa1 == "1":
                    print("La lista es: {}".format(lista))
                    time.sleep(2)
                    os.system("cls")      
                           
                elif alternativa1 == "2": 
                    print("Los elementos de la lista que van del rango [:] es: {}".format(lista[:]))
                    print("El elemento que se encuentra en la posición 2 es: {}".format(lista[2])) 
                    print("El último elemento de la lista es: {}".format(lista[-1]))
                    time.sleep(4)
                    os.system("cls")
                    
                elif alternativa1 == "3":
                    print("Los elementos de la lista que van del rango [0:4] son: {}".format(lista[0:4]))
                    print("Los elementos de la lista que van del rango [:5] son: {}".format(lista[:5]))
                    print("Los elementos de la lista que van del rango [3:] son: {}".format(lista[3:]))
                    time.sleep(4)
                    os.system("cls")
                    
                elif alternativa1 == "4":
                    print("Lista original: {}".format(lista))
                    lista.append("Carlos Molina")
                    print("La lista una vez añadido un nuevo elemento: {}".format(lista))
                    time.sleep(3)
                    os.system("cls")
                    
                elif alternativa1 == "5":
                    print("Lista original: {}".format(lista))
                    lista.insert(3,'Ecuador')
                    print("Nueva lista: {}".format(lista))
                    time.sleep(2)
                    os.system("cls")
                    
                elif alternativa1 == "6":
                    print("Lista original: {}".format(lista))
                    lista.extend(["1","2","3"])
                    print("Lista nueva: {}".format(lista))
                    time.sleep(3)
                    os.system("cls")
                    
                elif alternativa1 == "7":
                    print("Lista original: {}".format(lista))
                   
                    if "Ecuador" in lista:
                        print("El índice del elemento 'Ecuador' es: {}".format(lista.index("Ecuador")))
                        time.sleep(2)
                        os.system("cls")
                    else:
                        print("El elemento 'Ecuador' no se encuentra en la lista.")
                        time.sleep(3)
                        os.system("cls")
                        
                elif alternativa1 == "8":
                    print("Lista original: {}".format(lista))
                    if True in lista:
                        lista.remove(True)
                        print("Nueva lista: {}".format(lista))
                        time.sleep(2)
                        os.system("cls")
                    else:
                        print("El elemento 'True' no se encuentra en la lista")
                        time.sleep(2)
                        os.system("cls")    
                                        
                elif alternativa1 == "9":
                    print("Lista original: {}".format(lista))
                    print("Elemento eliminado: {}".format(lista.pop()))
                    print("Lista nueva: {}".format(lista))
                    time.sleep(2.5)
                    os.system("cls")
                    
                elif alternativa1 == "10":
                    lista1 = ["a","b","c"]
                    lista2 = ["c","d","e"]
                    print("Lista 1: {}".format(lista1))
                    print("Lista 2: {}".format(lista2))
                    lista3 = lista1 + lista2
                    print("La lista concatenada es: {}".format(lista3))
                    time.sleep(3)
                    os.system("cls")
                    
                elif alternativa1 == "11":
                    lista1 = ["a","b","c"]
                    print("La lista multiplicada por 3: {}".format(lista1 * 3))
                    time.sleep(2)
                    os.system("cls")
                    
                elif alternativa1 == "12":
                    print("Lista original: {}".format(lista))
                    a = "fresa" in lista
                    print("¿El elemento 'fresa' se encuentra en la lista?: {}".format(a))
                    time.sleep(2)
                    os.system("cls")                
                    
                elif alternativa1 == "13":
                    print("Saliendo de la opción 8...")
                    time.sleep(1.5)
                    os.system("cls")                
                    
                    
    elif alternativa == "9":
        dic = {"Marca1":"Ford","Modelo":"Mustang","Año":1964}
        alternativa1 = ""
        os.system("cls")
        while alternativa1 !="14":
                alternativa1 = sub.menu(["1) Presentar un Diccionario","2) Acceder a los elementos de un diccionario","3) Añadir elementos a un diccionario","4) Modificar elementos de un diccionario","5) Eliminar un elemento del diccionario (cláusula del)","6) Diccionario con claves y valores de distintos tipos de datos",
                                         "7) Definir claves del diccionario en una tupla","8) Diccionario dentro de otro diccionario","9) Función .get()","10) Método .keys()","11) Método .values()","12) Convertir en lista lo que se obtenga de .values()",
                                         "13) Convertir a tupla lo que se obtenga de .values()","14) Salir..."],"Manejo de Diccionarios")
                os.system("cls")
                if alternativa1 == "1":
                    dic = {"Marca1":"Ford","Modelo":"Mustang","Año":1964}
                    print("El diccionario es: {}".format(dic))
                    time.sleep(2)
                    os.system("cls")  
                
                elif alternativa1 == "2":
                    print("Diccionario: {}".format(dic))   
                    x = dic["Marca1"]
                    print("La marca es: {}".format(x))    
                    time.sleep(2)
                    os.system("cls") 
                
                elif alternativa1 == "3":   
                    print("Diccionario: {}".format(dic))   
                    dic["Marca2"] = "Ferrari"
                    print("Nuevo diccionario: {}".format(dic))
                    time.sleep(2)
                    os.system("cls")
                       
                elif alternativa1 == "4":      
                    print("Diccionario: {}".format(dic))   
                    dic["Año"] = 2019
                    print("Nuevo diccionario: {}".format(dic))
                    time.sleep(3)
                    os.system("cls")
                    
                elif alternativa1 == "5":   
                    print("Diccionario: {}".format(dic))   
                    if "Marca1" in dic:
                        del dic["Marca1"]
                        print("Nuevo diccionario: {}".format(dic))
                        time.sleep(2)
                        os.system("cls")
                    else:
                        print("El elemento no se encuentra en el diccionario.")
                        time.sleep(2)
                        os.system("cls")
                       
                    
                elif alternativa1 == "6":      
                    dic2 = {"Moreno":"Manuel",30:True,"Sueldo":220.4}
                    print("Diccionario: {}".format(dic2))
                    time.sleep(2)
                    os.system("cls")
                    
                elif alternativa1 == "7":      
                    clave = ("Marca","Modelo","Año")
                    dic3 = {clave[0]:"Chevrolet",clave[1]:"Camaro",clave[2]:2020}
                    print("Diccionario: {}".format(dic3))
                    time.sleep(2)
                    os.system("cls")
                    
                elif alternativa1 == "8":
                    datospersonales = {"Apellido":"Molina","Años":{1:2020,2:2021,3:2022}}
                    print("Diccionario: {}".format(datospersonales))
                    print("Años: {}".format(datospersonales["Años"]))
                    time.sleep(2)
                    os.system("cls")
                    
                elif alternativa1 == "9":
                    datospersonales = {"Apellido":"Molina","Años":{1:2020,2:2021,3:2022}}
                    print("Apellido: {}".format(datospersonales.get("Apellido","No existe")))
                    time.sleep(2)
                    os.system("cls")
                          
                elif alternativa1 == "10":
                    datospersonales = {"Apellido":"Molina","Años":{1:2020,2:2021,3:2022}}
                    print("Claves: {}".format(datospersonales.keys()))
                    time.sleep(2)
                    os.system("cls")
                    
                elif alternativa1 == "11":
                    datospersonales = {"Apellido":"Molina","Años":{1:2020,2:2021,3:2022}}
                    print("Valores: {}".format(datospersonales.values()))
                    time.sleep(2)
                    os.system("cls")
                    
                elif alternativa1 == "12":
                    datospersonales = {"Apellido":"Molina","Años":{1:2020,2:2021,3:2022}}
                    valores = list(datospersonales.values())
                    print("Valores: {}".format(valores))
                    time.sleep(2)
                    os.system("cls")
                
                elif alternativa1 == "13":
                    datospersonales = {"Apellido":"Molina","Años":{1:2020,2:2021,3:2022}}
                    valores = tuple(datospersonales.values())
                    print("Valores: {}".format(valores))
                    time.sleep(2)
                    os.system("cls")
                
                elif alternativa1 == "14":
                    print("Saliendo de la opción 9...")
                    time.sleep(1.5)
                    os.system("cls")                    
                          
    elif alternativa == "10":
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        sueldo = float(input("Ingresar sueldo: "))
        
        print("Hola, {}.".format(nombre))
        edadfutura = edad + 20
        print("Mi edad actual es: {} años.".format(edad))
        print("Mi edad (dentro de 20 años) será: {} años.".format(edadfutura))
        print("El sueldo es: {}".format(sueldo))
        time.sleep(5)
        os.system("cls")
        print("Saliendo de la opción 10...")
        time.sleep(1.5)
        os.system("cls")
    
    elif alternativa == "11":
        edad = int(input("Ingresar edad: "))
        if edad > 18:
            print("Eres mayor de edad.")
            time.sleep(2)         
            os.system("cls")
            
        elif edad == 18:
            print("Tienes 18 años.")
            time.sleep(2)    
            os.system("cls")
            
        else:
            print("Eres menor de edad.")
            time.sleep(2)    
            os.system("cls")
        
        print("Saliendo de la opción 11...")
        time.sleep(2)
    
        os.system("cls")
    
    elif alternativa == "12":
        alternativa1 = ""
        os.system("cls")
        while alternativa1 != "3":
            alternativa1 = sub.menu(["1) Funciones sin Parámetros","2) Funciones con Parámetros","3) Salir..."],"Funciones")
            os.system("cls")
            if alternativa1 == "1":
                def saludar():
                    print("Molina")
                    print("Carlos")
                    print("cmolinaj")
                    return "Hola"
                
                print(saludar())
                time.sleep(3)
                os.system("cls")
            
            elif alternativa1 == "2":
                def evaluarSueldoMinimo(sueldo):
                    if sueldo >= 425:
                        print("Cumples con el sueldo.")
                        time.sleep(1.5)
                        os.system("cls")
                    else:
                        print("Ganas menos que el sueldo mínimo.")  
                        time.sleep(1.5)
                        os.system("cls")
                         
                evaluarSueldoMinimo(500)
               
            elif alternativa1 == "3":   
                print("Saliendo de la opción 12...")
                time.sleep(1.5)
                os.system("cls")
    
    elif alternativa == "13":
        A = 140
        B = A
        C = 200
        
       
        if (A < 200 and B == A) or C < 300:
            x = "Es una condición verdadera."
        print("{}".format(x))
        time.sleep(3)
        os.system("cls")
        
        if (45 < 50 and 38 < 90) and (76 < 22):
            print("La condición es verdadera.")
            time.sleep(2)
            os.system("cls")
        else:
            print("La condición es falsa.")
            time.sleep(2)
            os.system("cls")
        
        print("Saliendo de la opción 13...")
        time.sleep(1.5)
        os.system("cls")
    
    elif alternativa == "14":
        sexo = ("Hombre","Mujer")
        indice = True
        sexo1 = sexo[indice]
        print("El sexo es: {}".format(sexo1))
        time.sleep(2)
       
        sexo2 = sexo[not indice]
        print("El sexo es: {}".format(sexo2))
        time.sleep(2)
        os.system("cls")
        
        print("Saliendo de la opción 14...")
        time.sleep(1.5)
        os.system("cls")
    
    elif alternativa == "15":
        print("--- Cursos ---")
        tupla = "Matematica - Biología - Lenguaje - Ciencias"
        print(tupla)

        curso = input("Ingrese el curso deseado: ")

        os.system("cls")
        if curso in ("Matemáticas - Biología - Lenguaje - Ciencias"):
            print("Curso {} seleccionado.".format(curso))
        else:
            print("No existe este curso.")
        time.sleep(2)
        os.system("cls")
        
        print("Saliendo de la opción 15...")
        time.sleep(1.5)
        os.system("cls")
    
    elif alternativa == "16":
        dato = range(7)  # [0,1,2,3,4]
        print("El elemento en la posición 0 es: {}".format(dato[0]))

        dato1 = range(2, 11) #[2,3,4,5,6,7,8,9,10]
        print("El elemento en la posición 3 es: {}".format(dato1[3]))

        dato2 = range(0, 11, 2) #[0,2,4,6,8,10]
        print("El elemento en la posición 5 es: {}".format(dato2[5]))
        time.sleep(3)
        os.system("cls")
        
        print("Saliendo de la opción 16...")
        time.sleep(1.5)
        os.system("cls")
    
    elif alternativa == "17":
        os.system("cls")
        lista = []
        for num in range(0, 15):
            lista.append(num)
        print("Los valores del ciclo1 son: {}".format(lista))
        
       
        for num in range(0, 40, 3):
            lista.append(num)
        print("Los valores del ciclo2 son: {}".format(lista))
        time.sleep(5)
        os.system("cls")

        for i in range(1, 9):
            print("-"*10,"Tabla de Multiplicar del {}".format(i),"-"*10)
            for j in range(1,11): 
                print("El producto entre {} x {} es : {}".format(i, j, (i * j)))
        time.sleep(15)
        os.system("cls")
        
        #Recorrer una tupla, len muestra la longitud
        for nom in ["Genny", "Kristel", "Marcelo", "César", "Leonidas"]:
            print("La cantidad de caracteres de '{}' es: {}".format(nom, len(nom)))
        time.sleep(5)
        os.system("cls")
        
        print("Saliendo de la opción 17...")
        time.sleep(1.5)
        os.system("cls")
        
    elif alternativa == "18":
        # num = int(input("Ingrese un número: "))
        # factorial = 1
        # for i in range(1, (num + 1)):
        #     factorial = factorial * i
        # print("El factorial de {} es: {}".format(num, factorial))
        # time.sleep(1)
        
    
        while True:      
            num = int(input("Ingresar un número: "))
            if num < 0:
                print("No existe factorial.")
                time.sleep(2)
                os.system("cls")
            elif num == 0: 
                print("El factorial es 1.")
                time.sleep(2)
                os.system("cls")
            else:
                resultado1 = num - 1
                while resultado1 > 0:
                    num = num * resultado1
                    resultado1 = resultado1 - 1               
                print("El factorial es: {} ".format(num))
                time.sleep(3)
                break
        
        os.system("cls")
        print("Saliendo de la opción 18...")
        time.sleep(1.5)
        os.system("cls")
            
    elif alternativa == "19":
        alternativa1 = ""
        while alternativa1 != "3":
            os.system("cls")
            alternativa1 = sub.menu(["1) Bucle While (Ejercicio 1)","2) Bucle While (Ejercicio 2)","3) Salir..."],"Manejo de Ciclo While")
            os.system("cls")
            if alternativa1 == "1":
                indice = 1
                while indice < 10:
                    print("Valor actual: {}".format(indice))
                    indice += 1
                print("*"*5,"Hemos terminado el bucle","*"*5,)
                time.sleep(5)
                os.system("cls")
            
            elif alternativa1 == "2":
                inicio = 3
                lista = []
                while inicio < 50:
                    lista.append(inicio)
                    inicio += 3
                print("Los valores de la iteración son: {}".format(lista))
                time.sleep(5)
                os.system("cls")
            
            elif alternativa1 == "3":
                print("Saliendo de la opción 19...")
                time.sleep(1.5)
                os.system("cls")
                
    elif alternativa == "20":
        alternativa1 = ""
        while alternativa1 != "4":
            os.system("cls")
            alternativa1 = sub.menu(["1) Instrucción Break","2) Instrucción Continue","3) Instrucción Pass","4) Salir..."],"Manejo de sentencias para bucles")
            os.system("cls")
            if alternativa1 == "1":
                for num in range(1,6):
                    if num == 4:
                        break #Permite salir de un bucle cuando se cumple una condición (interrumpe el ciclo y finaliza su ejecución)
                    print("El número es: {}".format(num))
                    time.sleep(2)
                print("El bucle ha finalizado.")
                time.sleep(2)
                os.system("cls")
            
            elif alternativa1 == "2":
                for num in range(1,6):
                    if num == 4:
                        continue # Omite una parte del bucle cuando se cumple una condición y continúa con el resto del bucle
                    print("El número es: {}".format(num))
                    time.sleep(2)
                print("El bucle ha finalizado.")
                time.sleep(2)
                os.system("cls")
            
            elif alternativa1 == "3":
                for num in range(1,10):
                    if num <= 5:
                        pass # Permite continuar con una sentencia o función que ya no tiene o todavía no tiene un bloque de código
                    
                    print("El número es: {}".format(num))
                    time.sleep(1)
                    
                print("El bucle ha finalizado.")
                time.sleep(2)
                os.system("cls")
            
            elif alternativa1 == "4":
                print("Saliendo de la opción 20...")
                time.sleep(1.5)
                os.system("cls")
                
                 
    elif alternativa == "21":
        alternativa1 = ""
        while alternativa1 != "4":
            os.system("cls")
            alternativa1 = sub.menu(["1) Ejemplo práctico para partir al uso de generadores","2) Instrucción yield","3) Instrucción next()","4) Salir..."],"Uso de Generadores")
            os.system("cls")
            if alternativa1 == "1":
                def generaMultiplos6(limite):
                    num = 1
                    lista = []
                    
                    while num <= limite:
                        lista.append(num * 6)
                        num = num + 1
                    return lista
                
                x = generaMultiplos6(10)
                print("La lista de múltiplos de 6 es: {}".format(x))
                time.sleep(4)
                os.system("cls")
                
            elif alternativa1 == "2":
                def generadorMultiplo7(limite):
                    num = 1
                    while num <= limite:
                        yield num * 7 #La instrucción yield genera un objeto iterable
                        num = num + 1


                y = generadorMultiplo7(10)
                
                for i in y:
                    print("El elemento es: {}".format(i))
                    time.sleep(1)
            
            elif alternativa1 == "3":
                def generadorMultiplo7(limite):
                    num = 1
                    while num <= limite:
                        yield num * 7 #La instrucción yield genera un objeto iterable
                        num = num + 1


                y = generadorMultiplo7(10)
                # next(): Retorna el siguiente elemento de un objeto iterable
                print("El primer elemento es: {}".format(next(y)))
                print("El siguiente elemento es: {}".format(next(y)))
                print("El siguiente elemento es: {}".format(next(y)))
                print("El siguiente elemento es: {}".format(next(y)))
                print("El siguiente elemento es: {}".format(next(y)))
                print("El siguiente elemento es: {}".format(next(y)))
                print("El siguiente elemento es: {}".format(next(y)))
                time.sleep(3)
                
                #Un generador me permite obtener los valores uno a uno, sin tener que almancenar todo de golpe. Así, podremos
                #trabajar de manera individual con los elementos.
                #Entre llamada y llamada, el objeto iterable entra en un estado de pausa.
            
            elif alternativa1 == "4":
                print("Saliendo de la opción 21...")
                time.sleep(1.5)
                os.system("cls")
    
    elif alternativa == "22":
        #Cuando indicamos un * adelante del parámetro de una función, estamos indicando que se va a recibir un número
        #indeterminado de parámetros. Además, esos parámetros se recibirán en forma de tupla
        def devuelveLenguajes(*lenguajes):
            for leng in lenguajes:
                yield from leng
                
        m = devuelveLenguajes("Python","Java","PhP","Ruby","JavaScript")
        print(next(m))
        print(next(m))
        time.sleep(2)
        os.system("cls")
        
        print("Saliendo de la opción 22...")
        time.sleep(1.5)
        os.system("cls")
    
    elif alternativa == "23":
        alternativa1 = ""
        while alternativa1 != "3":
            os.system("cls")
            alternativa1 = sub.menu(["1) Ejemplo 1 de uso de excepciones","2) Ejemplo 2 de uso de excepciones","3) Salir..."],"Excepciones")
            os.system("cls")
            if alternativa1 == "1":
                num = 30
                num2 = 0
                try:
                    resultado = num / num2   
                except:
                    print("Error en el programa...")
                    time.sleep(2)
            
            elif alternativa1 == "2":
                num = 44
                num2 = 2
                try:
                    resultado = num / num2
                    print("El resultado de dividir {} entre {} es: {}".format(num,num2,resultado))
                    time.sleep(2)
                except ZeroDivisionError:
                    print("No se puede dividir entre 0...")
                    time.sleep(2)
                finally: # Siempre se va a ejecutar
                    print("Siempre me ejecuto.")
                    time.sleep(2)
                
            elif alternativa1 == "3":
                print("Saliendo de la opción 23...")
                time.sleep(1.5)
                os.system("cls")
                    
    elif alternativa == "24":
        
        #Raise: Sirve para lanzar (de forma intencional) excepciones en Python
        
        def evaluarNota(nota):
            if nota < 0:
                raise ZeroDivisionError("No se permite valores negativos.")
            elif nota >= 16:
                os.system("cls")
                print("Excelente.")
                time.sleep(2)
            elif nota >= 11 and nota < 16:
                os.system("cls")
                print("Aprobado.")
                time.sleep(2)
            else:
                os.system("cls")
                print("Reprobado.")
                time.sleep(2)
        
        evaluarNota(int(input("Ingresar nota del 0 al 20: ")))

        os.system("cls")
        print("Saliendo de la opción 24...")
        time.sleep(1.5)

    
    elif alternativa == "25":
        print("La suma es: {}".format(sumar(4,8)))
        print("La multiplicación es: {}".format(multiplicar(4,4)))
        time.sleep(2.5)
        os.system("cls")
        
        print("Saliendo de la opción 25...")
        time.sleep(1.5)
        os.system("cls")

    elif alternativa == "26":
        print("La multiplicación es: {}".format(multiplicar(5,4)))
        print("La longitud de la cadena es: {}".format(contarLetras("No confundas mi silencio con falta de duelo. Llora a tu manera, yo lo haré a la mía")))
        time.sleep(3)
        os.system("cls")
        
        print("Saliendo de la opción 26...")
        time.sleep(1.5)
    
    
    elif alternativa == "27": 
        class Persona:
            apellidos = ""
            nombres = ""
            edad = 0

            def despertar(self):     
                print("Buen día.")


        persona1 = Persona()
        persona1.apellidos = "Márquez Manuel"
        print("Los apellidos son: {}".format(persona1.apellidos))
        persona1.despertar()
    

        persona2 = Persona()
        persona2.apellidos = "Molina Carlos"
        print("Los apellidos son: {}".format(persona2.apellidos))
        persona2.despertar()
        time.sleep(2)
        os.system("cls")
        
       
        print("Saliendo de la opción 27...")
        time.sleep(1.5)
    
    
    elif alternativa == "28":
        class Curso:
            def __init__(self, nom, cred, prof):
                self.nombre = nom
                self.creditos = cred
                self.profesion = prof


        curso1 = Curso("Física", 5, "Ingeniería Civil")
        x = curso1.nombre
        y = curso1.profesion
        print(x,"-",y)

        curso2 = Curso("POO", 5, "Ingeniería en Software")
        c = curso2.nombre
        d = curso2.profesion
        print(c,"-",d)
        time.sleep(2)
        os.system("cls")
        
        print("Saliendo de la opción 28...")
        time.sleep(1.5)
        
    
    elif alternativa == "29":
        class Curso:
            def __init__(self, nom, cred, prof):
                self.nombre = nom
                self.creditos = cred
                self.profesion = prof
                self.__imparticion = "Presencial"

            def mostrar(self):
                dat = "Nombre: {} - Créditos: {} - Modo de impartición: {}"
                print(dat.format(self.nombre,self.creditos,self .__imparticion))


        curso1 = Curso("Base de Datos", 5, "Ingeniería en Software")
        curso1.mostrar()
        time.sleep(2)
        os.system("cls")
        
        print("Saliendo de la opción 29...")
        time.sleep(1.5)
        
    
    
    elif alternativa == "30":
        class Curso:
            def __init__(self, nom, cred, prof):
                self.nombre = nom
                self.creditos = cred
                self.profesion = prof
                self.__imparticion = "Presencial"

            def mostrar(self):
                dat = "Nombre: {} - Créditos: {} - Modo de impartición: {}"
                print(dat.format(self.nombre,self.creditos,self .__imparticion))
                docenteAsignado = self.__verificarDocente()
                if docenteAsignado:
                    print("Docente asignado.")
                else:
                    print("No es necesario asignar un docente.")
    
                
            def __verificarDocente(self):
                print("Verificando si existe docente asignado...")
                time.sleep(2)
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

        
        
        curso = Curso("Termodinámica",6,"Ingeniería Química") 
        curso.mostrar()
        time.sleep(2.5)
        os.system("cls")
        
        print("Saliendo de la opción 30...")
        time.sleep(1.5)
        
        
    
    elif alternativa == "31":
        
        class Cuenta:
            
            def __init__(self, prop, saldo, mon):
                self.__propietario = prop
                self.__saldo = saldo
                self.__moneda = mon
        
        #Getters (métodos GET) --> obtener valores
            def get_saldo(self):
                return self.__saldo
            
            def get_propietario(self):
                return self.__propietario
            
            def get_moneda(self):
                return self.__moneda
        #Setters (métodos SET)  --> modificar los valores
            def set_moneda(self,moneda):
                self.__moneda = moneda
                
                
                
        cuenta = Cuenta("Carlos Molina",5200,"Dólares")
        print(cuenta.get_saldo())
        time.sleep(1.5)
        print(cuenta.get_moneda())
        time.sleep(1.5)
        cuenta.set_moneda("Pesos")
        print(cuenta.get_moneda())
        time.sleep(1.5)
        os.system("cls")


        print("Saliendo de la opción 31...")
        time.sleep(1.5)
        
    
    elif alternativa == "32":
        class Curso:
            def __init__(self, nom, cred, prof):
                self.nombre = nom
                self.creditos = cred
                self.profesion = prof
                self.__imparticion = "Presencial"

            def mostrar(self):
                dat = "Nombre: {} - Créditos: {} - Modo de impartición: {}"
                print(dat.format(self.nombre,self.creditos,self .__imparticion))
                docenteAsignado = self.__verificarDocente()
                if docenteAsignado:
                    print("Docente asignado.")
                    time.sleep(2)
                else:
                    print("No es necesario asignar un docente.")
    
                
            def __verificarDocente(self):
                print("Verificando si existe docente asignado...")
                time.sleep(2)
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

            def __str__(self):  #Se define lo que se va a mostrar cuando se llame a imprimir un objeto o instancia de una clase
                texto = "Nombre: {} - Créditos: {}"
                return texto.format(self.nombre,self.creditos)
        
        curso = Curso("Termodinámica",6,"Ingeniería Química") 
        print(curso)
        print(curso.mostrar())
        os.system("cls")
        
        print("Saliendo de la opción 32...")
        time.sleep(1.5)
        
    
    elif alternativa == "33":
        class Persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombre = nom

            def mostrarNombreCompleto(self):
                txt = "{} {}, {}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)


        class Estudiante(Persona):
            def __init__(self, apePat, apeMat, nom, prof):
                super().__init__(apePat, apeMat, nom)
                self.profesion = prof


        estudiante = Estudiante("García", "Mendoza", "Luis", "Ingeniero Mecánico")
        print(estudiante.mostrarNombreCompleto(),"-",estudiante.profesion)
        time.sleep(2)
        os.system("cls")
        
        print("Saliendo de la opción 33...")
        time.sleep(1.5)        
        
    elif alternativa == "34":
        
        class Persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombre = nom

            def mostrarNombreCompleto(self):
                txt = "{} {}, {}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

            def datos(self):
                print(self.mostrarNombreCompleto())

        class Estudiante(Persona):
            def __init__(self, apePat, apeMat, nom, prof):
                super().__init__(apePat, apeMat, nom)
                self.profesion = prof


            def datos(self):
                super().datos()
                print("Profesión: {}".format(self.profesion))
                time.sleep(2)
        
        estudiante = Estudiante("García", "Mendoza", "Luis", "Ingeniero Mecánico")
        estudiante.datos()
        os.system("cls")
        
        print("Saliendo de la opción 34...")
        time.sleep(1.5)        
        
    elif alternativa == "35":
        class Persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombre = nom

            def mostrarNombreCompleto(self):
                txt = "{} {}, {}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

            def datos(self):
                print(self.mostrarNombreCompleto())

        class Estudiante(Persona):
            def __init__(self, apePat, apeMat, nom, prof):
                super().__init__(apePat, apeMat, nom)
                self.profesion = prof


            def datos(self):
                super().datos()
                print("Profesión: {}".format(self.profesion))
                time.sleep(2)
        
        estudiante = Estudiante  ("García", "Mendoza", "Luis", "Ingeniero Mecánico")
        print("Valor: {}".format(isinstance(estudiante,Estudiante)))
       
        persona = Persona("García", "Mendoza", "Luis")
        print("Valor 2: {}".format(isinstance(persona,Estudiante)))
        time.sleep(2)
        os.system("cls")
        
        
        print("Saliendo de la opción 35...")
        time.sleep(1.5)        
    
    elif alternativa == "36":
        class ClaseA():
            def __init__(self, par1, par2):
                self.parametro1 = par1
                self.parametro2 = par2


        class ClaseB():
            def __init__(self, par3, par4, par5):
                self.parametro3 = par3
                self.parametro4 = par4
                self.parametro5 = par5


        class claseC(ClaseA, ClaseB):
            pass
        claC = claseC("Hola,", "buenos días.")
        x = claC.parametro1 + " " + claC.parametro2
        print(x)
        time.sleep(2)
        
        os.system("cls")
        print("Saliendo de la opción 35...")
        time.sleep(1.5)   

    
    elif alternativa == "37":
        class Estudiante():
            def describir(self):
                print("Soy un buen estudiante.")
                time.sleep(1.3)

        class Docente():
            def describir(self):
                print("Me dedico a enseñar cursos.")
                time.sleep(1.3)

        class Trabajador():
            def describir(self):
                print("Trabajo dentro de una gran empresa.")
                time.sleep(1.3)

        def describirPersona(persona):
            persona.describir()


        docente = Docente()
        describirPersona(docente)
        
        estudiante = Estudiante()
        describirPersona(estudiante)
        
        trabajador = Trabajador()
        describirPersona(trabajador) 
        
        time.sleep(1.2)
        
        os.system("cls")
        print("Saliendo de la opción 37...")
        time.sleep(1.5)
    
    elif alternativa == "38":
        class Pais():
            def __init__(self, nom, pre):
                self.nombre = nom
                self.presidente = pre
                
            def __str__(self):
                txt = "País: {} - Presidente: {}"
                return txt.format(self.nombre,self.presidente)
        
        class Ciudad():
            def __init__(self, nom, hab, pais):
                self.nombre = nom
                self.habitantes = hab
                self.pais = pais
                
            def __str__(self):
                txt = "Ciudad: {} - N° Habitantes: {} - ({})"
                return txt.format(self.nombre, self.habitantes,self.pais)
        
        class Urbanizacion():
            def __init__(self, nom, ciu):
                self.nombre = nom
                self.ciudad = ciu

            def __str__(self):
                txt = "Urbanización: {} ({})"
                return txt.format(self.nombre, self.ciudad)
    
           
        pais = Pais("Ecuador","Guillermo Lasso")
        print(pais)
        
        ciudad = Ciudad("Guayaquil",2698000,pais)
        print(ciudad)
        
        urbanización = Urbanizacion("Urbanización La Perla",ciudad)
        print(urbanización)
        
    
        time.sleep(4)
        os.system("cls")
        
        print("Saliendo de la opción 38...")
        time.sleep(1.5)
        
    elif alternativa == "39":
        print("Gracias por su recibimiento...")
        time.sleep(1.2)
        print("Vuelva pronto.")
        time.sleep(1.5)
        
