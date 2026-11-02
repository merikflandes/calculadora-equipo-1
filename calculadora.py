# Código base de la calculadora
# calculadora.py

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    return a / b

    opcion = input ("Elige una opcion (1=suma, 2=resta, 3=multiplicacion, 4=division, 5=salir)")
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            pass # Tu compañero lo conectará
        elif opcion == '2':
            pass # Tu compañero lo conectará
        elif opcion == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == '4':
            print("Resultado:", dividir(num1, num2))
    elif opcion == '5':
        print("Adios")
    else:
        print("Opción no válida")