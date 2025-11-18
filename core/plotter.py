import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def graficar(funcion, derivada, variables, var_derivar):
    if len(variables) == 1:
        return plot_univariable(funcion, derivada, variables[0])

    if len(variables) == 2:
        return plot_bivariable(funcion, derivada, variables, var_derivar)

    print("\nLa función tiene 3 variables. No se graficará automáticamente.")

def plot_univariable(funcion, derivada, variable):
    f = sp.lambdify(variable, funcion, "numpy")
    d = sp.lambdify(variable, derivada, "numpy")

    xs = np.linspace(-5, 5, 400)

    plt.figure(figsize=(10,6))
    plt.plot(xs, f(xs), label="f(x)")
    plt.plot(xs, d(xs), label=f"df/d{variable}")
    plt.legend()
    plt.grid(True)
    plt.title("Función y derivada")
    plt.show()

def plot_bivariable(funcion, derivada, variables, var_derivar):
    v1, v2 = variables

    f = sp.lambdify((v1, v2), funcion, "numpy")
    d = sp.lambdify((v1, v2), derivada, "numpy")

    x = np.linspace(-5, 5, 40)
    y = np.linspace(-5, 5, 40)
    X, Y = np.meshgrid(x, y)

    Z1 = f(X, Y)
    Z2 = d(X, Y)

    fig = plt.figure(figsize=(14,6))

    ax1 = fig.add_subplot(121, projection="3d")
    ax1.plot_surface(X, Y, Z1, cmap="viridis")
    ax1.set_title("Función original")

    ax2 = fig.add_subplot(122, projection="3d")
    ax2.plot_surface(X, Y, Z2, cmap="inferno")
    ax2.set_title(f"Derivada parcial respecto a {var_derivar}")

    plt.show()
