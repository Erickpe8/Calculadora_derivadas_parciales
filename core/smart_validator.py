import re

FUNCIONES = [
    "sin", "cos", "tan", "asin", "acos", "atan",
    "sinh", "cosh", "tanh", "log", "ln", "exp", "sqrt", "abs"
]

VARIABLES = ["x", "y", "z"]


def corregir_expresion(expr):
    corregida = expr

    # 1. sinx → sin(x), logy → log(y), etc.
    for f in FUNCIONES:
        corregida = re.sub(rf"{f}([xyz])", rf"{f}(\1)", corregida)

    # 2. xy → x*y  (pero NO tocar sin(x), cos(x), log(x)...)
    corregida = re.sub(r"(?<![a-zA-Z])([xyz])([xyz])", r"\1*\2", corregida)

    # 3. 3x → 3*x
    corregida = re.sub(r"(\d)([xyz])", r"\1*\2", corregida)

    # 4. x^2 → x**2
    corregida = re.sub(r"([xyz])\^(\d+)", r"\1**\2", corregida)

    # 5. x(y) → x*(y)
    corregida = re.sub(r"([xyz])\(", r"\1*(", corregida)

    # 6. (x)y → (x)*y
    corregida = re.sub(r"\)([xyz])", r")*\1", corregida)

    # 7. e^x → exp(x)
    corregida = re.sub(r"e\^([xyz])", r"exp(\1)", corregida)

    # 8. e^(x*y) → exp(x*y)
    corregida = re.sub(r"e\^\((.*?)\)", r"exp(\1)", corregida)

    return corregida if corregida != expr else None
