from core.parser import parse_funcion
from core.validator import validar_funcion, funciones_permitidas
from core.derivative import derivar_funcion, detectar_variables
from core.plotter import graficar
from core.utils import limpiar_potencias, menu_principal
from core.pdf_viewer import mostrar_pdf_ayuda
from core.smart_validator import corregir_expresion


def main():
    while True:
        opcion = menu_principal()

        # =====================================================
        # OPCIÓN 1 — Calcular derivada parcial
        # =====================================================
        if opcion == "1":
            texto_funcion = input("\nIngrese la función: ").strip()
            texto_funcion = limpiar_potencias(texto_funcion)

            # ---------- SMART VALIDATOR PRO ----------
            correccion = corregir_expresion(texto_funcion)

            if correccion:
                print("\n⚠ Se detectaron errores en la expresión ingresada.")
                print(f"Sugerencia de corrección: {correccion}")
                usar = input("¿Desea usar esta corrección? (s/n): ").strip().lower()

                if usar == "s":
                    texto_funcion = correccion
                    print(f"\n✔ Usando expresión corregida: {texto_funcion}")

            # ---------- VALIDACIÓN DE FUNCIONES ----------
            invalida = validar_funcion(texto_funcion)
            if invalida:
                print(f"\n⚠ La función '{invalida}' no está permitida.")
                print(f"Funciones válidas: {', '.join(funciones_permitidas)}")
                continue

            # ---------- PARSEO ----------
            try:
                funcion = parse_funcion(texto_funcion)
            except Exception as e:
                print(f"\n⚠ Error al interpretar la función: {e}")
                continue

            # ---------- DETECTAR VARIABLES ----------
            variables = detectar_variables(funcion)
            if not variables:
                print("⚠ Debes usar al menos una variable: x, y o z.")
                continue

            print(f"Variables detectadas: {', '.join(variables)}")

            # ---------- PEDIR VARIABLE A DERIVAR ----------
            var = input("Variable para derivar (x, y o z): ").strip()
            if var not in variables:
                print(f"⚠ La variable '{var}' no está presente en la función.")
                continue

            # ---------- CALCULAR DERIVADA ----------
            derivada = derivar_funcion(funcion, var)

            print("\n=== RESULTADOS ===")
            print(f"Función original:  {funcion}")
            print(f"Derivada parcial ∂f/∂{var}:  {derivada}")

            # ---------- GRAFICAR ----------
            graficar(funcion, derivada, variables, var)

        # =====================================================
        # OPCIÓN 2 — Ayuda + PDF
        # =====================================================
        elif opcion == "2":
            print("\n=== AYUDA ===")
            print("¿Desea abrir la guía completa en PDF?")
            print("1. Sí, abrir PDF")
            print("2. No, mostrar ayuda rápida aquí")

            eleccion = input("Seleccione una opción: ").strip()

            if eleccion == "1":
                mostrar_pdf_ayuda()
            else:
                print("\n--- Ayuda rápida ---")
                print("• Potencias: usar ** → x**2, y**3")
                print("• Multiplicación explícita → x*y, 3*x*y")
                print("• Funciones válidas: sin, cos, exp, log, sqrt, tan...")
                print("• Ejemplos válidos:")
                print("  x**2*y + sin(x)")
                print("  exp(x*y) - z**2")
                print("  ln(x**2 + y**2)")

        # =====================================================
        # OPCIÓN 3 — Salir
        # =====================================================
        elif opcion == "3":
            print("\nSaliendo de la calculadora...")
            break

        else:
            print("⚠ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
