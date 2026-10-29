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
    Divide a entre b con soporte para números complejos.
    
    Soporta:
    - Números enteros
    - Números flotantes
    - Números complejos (complex)
    
    Returns:
        El cociente a / b
    """
    tipos_soportados = (int, float, complex)
    if not isinstance(a, tipos_soportados):
        raise TypeError(f"Tipo no soportado para dividendo: {type(a)}")
    if not isinstance(b, tipos_soportados):
        raise TypeError(f"Tipo no soportado para divisor: {type(b)}")
    
    # Para números complejos, b == 0 es b == 0+0j
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    
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