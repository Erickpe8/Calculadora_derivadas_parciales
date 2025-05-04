import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy.parsing.sympy_parser import parse_expr
import re

def validar_funciones(expr, funciones_permitidas):
    # Busca posibles funciones usando expresiones regulares
    funciones_encontradas = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expr)
    for f in funciones_encontradas:
        if f not in funciones_permitidas and not f.isalpha() and not f.isdigit():
            return f  # Función no permitida
    return None  

def main():
    print("=== Calculadora de Derivadas Parciales ===") 
    print("Ingrese una función multivariable (use x, y, z como variables)")
    print("Ejemplos: x**2 * y + sin(x), exp(x*y) - z**2")
    
    # Solicitar la función al usuario
    texto_funcion = input("Función: ")
    
    # Definir símbolos para las variables
    x, y, z = sp.symbols('x y z')
    
    funciones_permitidas = {
        'sin', 'cos', 'tan', 'cot', 'sec', 'csc',
        'asin', 'acos', 'atan',
        'sinh', 'cosh', 'tanh',
        'ln', 'log', 'sqrt', 'abs',
        'exp', 'x', 'y', 'z', 'e', 'E'
    }

    funcion_invalida = validar_funciones(texto_funcion, funciones_permitidas)
    if funcion_invalida:
        print(f"Error: La función '{funcion_invalida}' no está soportada. Revisa tu expresión.")
        return

    try:
        # Interpretar la función ingresada
        from sympy import E  # Asegúrate de importar E si no lo tenías

        funcion = parse_expr(
        texto_funcion,
        local_dict={
        'e': E, 'E': E,
        'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'cot': sp.cot,
        'sec': sp.sec, 'csc': sp.csc,
        'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
        'sinh': sp.sinh, 'cosh': sp.cosh, 'tanh': sp.tanh,
        'ln': sp.log, 'log': sp.log,
        'sqrt': sp.sqrt,
        'abs': sp.Abs
    }
)

        # Determinar qué variables están presentes en la función
        variables_presentes = [var for var in [x, y, z] if var in funcion.free_symbols]
        
        if not variables_presentes:
            print("Error: La función debe contener al menos una variable (x, y, z).")
            return
        
        # Mostrar las variables disponibles
        print(f"Variables detectadas: {', '.join([str(var) for var in variables_presentes])}")
        
        # Solicitar la variable respecto a la cual derivar
        variable_derivacion = input("Variable respecto a la cual derivar: ")
        
        # Verificar que la variable ingresada sea válida
        if variable_derivacion not in ['x', 'y', 'z']:
            print("Error: La variable debe ser x, y o z.")
            return
        
        # Convertir el texto de la variable a símbolo
        var_simbolo = sp.Symbol(variable_derivacion)
        
        # Verificar que la variable esté presente en la función
        if var_simbolo not in funcion.free_symbols:
            print(f"Error: La variable {variable_derivacion} no está presente en la función.")
            return
        
        # Calcular la derivada parcial
        derivada = sp.diff(funcion, var_simbolo)
        
        # Simplificar la derivada para evitar posibles errores con log(e)  
        derivada = sp.simplify(derivada)
        
        # Mostrar resultados con notación tipo código (str)
        print("\n=== Resultados ===")
        print(f"Función original: {str(funcion)}")
        print(f"Derivada parcial respecto a {variable_derivacion}: {str(derivada)}")

        
        # Graficar
        graficar_funciones(funcion, derivada, var_simbolo, variables_presentes)
        
    except Exception as e:
        print(f"Error al procesar la función: {e}")

def graficar_funciones(funcion, derivada, var_derivacion, variables_presentes):
    """Grafica la función original y su derivada parcial."""
    
    num_variables = len(variables_presentes)
    
    if num_variables == 1:
        # Caso de una variable: gráfica 2D simple
        graficar_funcion_univariable(funcion, derivada, variables_presentes[0])
    elif num_variables == 2:
        # Caso de dos variables: gráfica 3D
        graficar_funcion_bivariable(funcion, derivada, variables_presentes, var_derivacion)
    else:
        # Caso de tres variables: fijar una variable y hacer gráfica 3D
        print("\nLa función tiene tres variables. Se fijará una variable para la gráfica.")
        variables_fijas = [var for var in variables_presentes if var != var_derivacion]
        var_fijar = variables_fijas[0]
        valor = float(input(f"Valor para fijar {var_fijar}: "))
        
        # Sustituir la variable fijada en las funciones
        funcion_reducida = funcion.subs(var_fijar, valor)
        derivada_reducida = derivada.subs(var_fijar, valor)
        
        # Determinar las variables restantes
        vars_restantes = [var for var in variables_presentes if var != var_fijar]
        
        if len(vars_restantes) == 1:
            graficar_funcion_univariable(funcion_reducida, derivada_reducida, vars_restantes[0])
        else:
            graficar_funcion_bivariable(funcion_reducida, derivada_reducida, vars_restantes, var_derivacion)

def graficar_funcion_univariable(funcion, derivada, variable):
    """Grafica una función de una variable y su derivada."""
    
    # Convertir expresiones simbólicas a funciones numéricas
    f_lambda = sp.lambdify(variable, funcion, "numpy")
    d_lambda = sp.lambdify(variable, derivada, "numpy")
    
    # Crear puntos para la gráfica
    x_vals = np.linspace(-5, 5, 1000)
    
    try:
        # Calcular valores de las funciones
        y_vals = f_lambda(x_vals)
        dy_vals = d_lambda(x_vals)
        
        # Crear la figura con dos subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Graficar función original
        ax1.plot(x_vals, y_vals, 'b-', label=f'f({variable})')
        ax1.set_title(f'Función original: {funcion}')
        ax1.grid(True)
        ax1.legend()
        
        # Graficar derivada
        ax2.plot(x_vals, dy_vals, 'r-', label=f'df/d{variable}')
        ax2.set_title(f'Derivada parcial: {derivada}')
        ax2.grid(True)
        ax2.legend()
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error al graficar: {e}")
        print("Es posible que la función o su derivada tengan valores no graficables en el rango seleccionado.")

def graficar_funcion_bivariable(funcion, derivada, variables, var_derivacion):
    """Grafica una función de dos variables y su derivada parcial."""
    
    # Identificar las dos variables
    var1, var2 = variables
    
    # Convertir expresiones simbólicas a funciones numéricas
    f_lambda = sp.lambdify((var1, var2), funcion, "numpy")
    d_lambda = sp.lambdify((var1, var2), derivada, "numpy")
    
    # Crear malla de puntos
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    
    try:
        # Calcular valores de las funciones
        Z_f = f_lambda(X, Y)  # Usar X, Y en ese orden para las funciones
        Z_d = d_lambda(X, Y)  # Usar X, Y en ese orden para las derivadas

        # Verificar que no haya NaN o inf en los resultados
        if np.any(np.isnan(Z_f)) or np.any(np.isnan(Z_d)):
            print("Advertencia: Los valores de la función o su derivada no son válidos para el rango dado.")
            return
        
        # Crear figura con dos subplots 3D
        fig = plt.figure(figsize=(14, 6))
        
        # Graficar función original
        ax1 = fig.add_subplot(121, projection='3d')
        surf1 = ax1.plot_surface(X, Y, Z_f, cmap='viridis', alpha=0.8)
        ax1.set_title(f'Función: {funcion}')
        ax1.set_xlabel(f'{var1}')
        ax1.set_ylabel(f'{var2}')
        ax1.set_zlabel('f(x, y)')
        fig.colorbar(surf1)
        
        # Graficar derivada
        ax2 = fig.add_subplot(122, projection='3d')
        surf2 = ax2.plot_surface(X, Y, Z_d, cmap='inferno', alpha=0.8)
        ax2.set_title(f'Derivada parcial respecto a {var_derivacion}')
        ax2.set_xlabel(f'{var1}')
        ax2.set_ylabel(f'{var2}')
        ax2.set_zlabel(f'df/d{var_derivacion}')
        fig.colorbar(surf2)
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error al graficar: {e}")
        print("Es posible que la función o su derivada no sean gráficas en el rango seleccionado.")


if __name__ == "__main__":
    main()
