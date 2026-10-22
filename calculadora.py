# Sistema de calculadora básica — Proyecto de práctica Git

def sumar(a, b):
    """Retorna la suma de a y b."""
    return a + b


def restar(a, b):
    """Retorna la diferencia de a y b."""
    return a - b



def multiplicar(a, b):
    """Retorna el producto de a y b."""
    return a * b





def mostrar_menu():
    print("=== CALCULADORA BÁSICA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")



def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
        
        if opcion not in ["1", "2", "3", "4"]:
            print("Opción inválida.")
            continue
            
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        if opcion == "1":
            print(f"Resultado: {sumar(a, b)}")
        elif opcion == "2":
            print(f"Resultado: {restar(a, b)}")
        elif opcion == "3":
           print(f"Resultado: {multiplicar(a, b)}")
        #elif opcion == "4":
           # print(f"Resultado: {dividir(a, b)}")


if __name__ == "__main__":
    main()