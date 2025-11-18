from core.parser import parse_funcion
from core.validator import validar_funcion, funciones_permitidas
from core.derivative import derivar_funcion, detectar_variables
from core.plotter import graficar
from core.utils import limpiar_potencias, menu_principal
from core.pdf_viewer import mostrar_pdf_ayuda


def main():
    while True:
        opcion = menu_principal()

        # ============================================
        # OPCIÓN 1 - Calcular derivada parcial
        # ============================================
        if opcion == "1":
            texto_funcion = input("\nFunción: ").strip()
            texto_funcion = limpiar_potencias(texto_funcion)

            invalida = validar_funcion(texto_funcion)
            if invalida:
                print(f"\n⚠ La función '{invalida}' no está permitida.")
                print(f"Funciones válidas: {', '.join(funciones_permitidas)}")
                continue

            funcion = parse_funcion(texto_funcion)

            variables = detectar_variables(funcion)
            if not variables:
                print("⚠ Debes usar al menos una variable: x, y o z.")
                continue

            print(f"Variables detectadas: {', '.join(variables)}")

            var = input("Variable para derivar: ").strip()
            if var not in variables:
                print(f"⚠ La variable '{var}' no está en la función.")
                continue

            derivada = derivar_funcion(funcion, var)

            print("\n=== RESULTADOS ===")
            print(f"Función:  {funcion}")
            print(f"Derivada parcial ∂f/∂{var}: {derivada}")

            graficar(funcion, derivada, variables, var)

        # ============================================
        # OPCIÓN 2 - Mostrar ayuda o abrir PDF
        # ============================================
        elif opcion == "2":
            print("\n=== AYUDA ===")
            print("¿Desea abrir la guía completa en PDF?")
            print("1. Sí, abrir PDF")
            print("2. No, solo mostrar ayuda rápida")

            eleccion = input("Seleccione una opción: ").strip()

            if eleccion == "1":
                mostrar_pdf_ayuda()
            else:
                print("\n--- Ayuda rápida ---")
                print("• Usa potencias con ** (x**2, y**3)")
                print("• Funciones válidas: sin, cos, exp, log, sqrt, tan...")
                print("• Ejemplos:")
                print("  x**2*y + sin(x)")
                print("  exp(x*y) - z**2")
                print("  ln(x**2 + y**2)")

        # ============================================
        # OPCIÓN 3 - Salir
        # ============================================
        elif opcion == "3":
            print("\nSaliendo...")
            break

        else:
            print("⚠ Opción inválida")


if __name__ == "__main__":
    main()
