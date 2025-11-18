import re

funciones_permitidas = {
    'sin','cos','tan','cot','sec','csc',
    'asin','acos','atan',
    'sinh','cosh','tanh',
    'ln','log','sqrt','abs','exp',
    'x','y','z','e','E'
}

def validar_funcion(expr):
    tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expr)

    for t in tokens:
        if t not in funciones_permitidas:
            return t
    return None
