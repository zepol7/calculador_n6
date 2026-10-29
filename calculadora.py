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


def dividir(a, b):
    """
    Divide a entre b con validación robusta de errores.
    
    Raises:
        TypeError: si los argumentos no son numéricos
        ZeroDivisionError: si b es cero, con mensaje descriptivo
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"El primer argumento debe ser numérico, recibido: {type(a)}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"El segundo argumento debe ser numérico, recibido: {type(b)}")
    if b == 0:
        raise ZeroDivisionError(
            f"Error: no se puede dividir {a} entre cero. "
            "La división por cero no está definida matemáticamente."
        )
    return a / b

def potencia(base, exponente):
    """
    Calcula base elevado a exponente.
    Maneja exponentes negativos retornando el inverso.
    """
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / (base ** abs(exponente))
    else:
        return base ** exponente

def raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número.
    Lanza ValueError si el número es negativo.
    """
    if numero < 0:
        raise ValueError(f"No se puede calcular raíz cuadrada de {numero}")
    return numero ** 0.5

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
        elif opcion == "4":
           print(f"Resultado: {dividir(a, b)}")


if __name__ == "__main__":
    main()