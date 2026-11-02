# Código base de la calculadora
# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    pass 

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def main():
    print("\n--- Calculadora del Equipo 1 ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Elige una opción (1/2/3/4/5): ")
    
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            print("Resultado:", sumar(num1, num2))
        elif opcion == '2':
            print("Resultado:", restar(num1, num2))
        elif opcion == '3':
            pass 
        elif opcion == '4':
            print("Resultado:", dividir(num1, num2))
    elif opcion == '5':
        print("Saliendo...")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
