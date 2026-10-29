class HistorialOperaciones:
    """
    Registra el historial de operaciones realizadas en la calculadora.
    """
    
    def __init__(self):
        self._historial = []
    
    def registrar(self, operacion: str, a: float, b: float, resultado: float):
        """
        Registra una operación en el historial.
        
        Args:
            operacion: nombre de la operación ('suma', 'resta', etc.)
            a: primer operando
            b: segundo operando
            resultado: resultado de la operación
        """
        entrada = {
            "operacion": operacion,
            "a": a,
            "b": b,
            "resultado": resultado
        }
        self._historial.append(entrada)
    
    def obtener_historial(self):
        """Retorna una copia del historial de operaciones."""
        return self._historial.copy()
    
    def mostrar_historial(self):
        """Imprime el historial de operaciones en formato legible."""
        if not self._historial:
            print("No hay operaciones en el historial.")
            return
        
        print("\n=== HISTORIAL DE OPERACIONES ===")
        for i, op in enumerate(self._historial, 1):
            print(f"{i}. {op['operacion'].capitalize()}: "
                  f"{op['a']} y {op['b']} = {op['resultado']}")
    
    def limpiar(self):
        """Elimina todas las entradas del historial."""
        self._historial.clear()
        print("Historial limpiado.")
    
    def __len__(self):
        return len(self._historial)