import sympy as sp

def detectar_variables(funcion):
    return [str(v) for v in funcion.free_symbols]

def derivar_funcion(funcion, variable):
    var = sp.Symbol(variable)
    return sp.simplify(sp.diff(funcion, var))
