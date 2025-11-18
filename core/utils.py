def limpiar_potencias(expr):
    return expr.replace("^", "**")

def menu_principal():
    print("\n=== CALCULADORA DE DERIVADAS PARCIALES ===")
    print("1. Calcular derivada parcial")
    print("2. Ayuda y sintaxis")
    print("3. Salir")
    return input("Seleccione una opción: ").strip()
