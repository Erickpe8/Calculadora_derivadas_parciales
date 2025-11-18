import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

def parse_funcion(expr):
    x, y, z = sp.symbols("x y z")
    from sympy import E

    return parse_expr(
        expr,
        local_dict={
            "x": x, "y": y, "z": z,
            "e": E, "E": E,
            "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
            "asin": sp.asin, "acos": sp.acos, "atan": sp.atan,
            "sinh": sp.sinh, "cosh": sp.cosh, "tanh": sp.tanh,
            "log": sp.log, "ln": sp.log, 
            "sqrt": sp.sqrt, "abs": sp.Abs,
            "exp": sp.exp
        }
    )
