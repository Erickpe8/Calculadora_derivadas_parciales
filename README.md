
# Calculadora de Derivadas Parciales 🔣🧠

La **Calculadora de Derivadas Parciales** es una herramienta en Python para trabajar con funciones multivariables de manera simbólica.  
Permite:

- Ingresar funciones en términos de `x`, `y` y `z`.
- Calcular derivadas parciales respecto a una variable específica.
- Visualizar el comportamiento de la función y de su derivada mediante gráficos 2D y 3D.
- Corregir automáticamente expresiones mal escritas gracias a un validador inteligente.

Está pensada como apoyo al estudio de **cálculo multivariable**, derivadas parciales y análisis de funciones.

---

## ✨ Características principales

- 🔢 **Cálculo simbólico de derivadas parciales**  
  - Derivadas respecto a `x`, `y` o `z`.  
  - Uso de **SymPy** para interpretar y simplificar expresiones.

- 🧠 **Smart Validator PRO (corrección inteligente)**  
  Corrige errores de escritura frecuentes en las funciones, como:
  - `sinx` → `sin(x)`
  - `3x` → `3*x`
  - `xy` → `x*y`
  - `x^2` → `x**2`
  - `logx` → `log(x)`
  - `e^x` o `e**x` → `exp(x)`

- ✅ **Validación de funciones y sintaxis**
  - Verificación de funciones permitidas (`sin`, `cos`, `exp`, `log`, `sqrt`, etc.).
  - Mensajes claros cuando se usa algo no permitido o mal escrito.

- 📊 **Visualización gráfica**
  - Funciones de **una variable** → gráfico 2D.
  - Funciones de **dos variables** → superficie 3D (función y derivada).
  - Funciones de **tres variables** → análisis simbólico.

- 📚 **Guía de uso integrada en PDF**
  - Disponible en la carpeta `docs/`.
  - Se puede abrir directamente desde el menú de ayuda.

- 🧩 **Arquitectura modular**
  - Código organizado en módulos: parser, validador, derivadas, gráficos, utilidades, smart validator y visor PDF.

---

## 🗂 Estructura del proyecto

```
Calculadora_derivadas_parciales/
├── main.py
├── core/
│   ├── parser.py
│   ├── validator.py
│   ├── derivative.py
│   ├── plotter.py
│   ├── smart_validator.py
│   ├── utils.py
│   └── pdf_viewer.py
└── docs/
    └── Guia_de_Uso.pdf
```

---

## ⚙️ Requisitos

- Python 3.10+
- Librerías:
  ```
  sympy
  numpy
  matplotlib
  ```

---

## 📐 Sintaxis de funciones

### Variables:
`x`, `y`, `z`

### Operadores:
- Potencias: `x**2`
- Multiplicación explícita: `x*y`, `3*x*y`

### Funciones:
```
sin, cos, tan
asin, acos, atan
sinh, cosh, tanh
log, ln, exp
sqrt, abs
```

---

## 🧠 Smart Validator PRO

Corrige errores típicos como:

```
sinx → sin(x)
3x → 3*x
xy → x*y
x^2 → x**2
logx → log(x)
e^x → exp(x)
```

Ejemplo:

Entrada:
```
sinx + 3x - xy + x^2 + logy
```

Corrección sugerida:
```
sin(x) + 3*x - x*y + x**2 + log(y)
```

---

## 📐 Funcionamiento general

1. El usuario ingresa una función.
2. El Smart Validator PRO sugiere correcciones si detecta errores.
3. La función se valida y se interpreta simbólicamente.
4. Se detectan variables presentes.
5. El usuario elige la variable a derivar.
6. Se calcula la derivada parcial.
7. Se muestran resultados y gráficos (si corresponde).

---

## 🧪 Ejemplos de prueba

**Función válida:**

Entrada:
```
x**2*y + 3*x*y**3 - 5*x + 4
```

Derivada respecto a `x`:
```
2*x*y + 3*y**3 - 5
```

---

**Función con errores corregidos:**

Entrada:
```
cosx + 4y + 2xz + e^x + logx + x(y) + 3xy^2
```

Corrección sugerida:
```
cos(x) + 4*y + 2*x*z + exp(x) + log(x) + x*(y) + 3*x*y**2
```

---

## ▶️ Uso

1. Ejecutar:
```
python main.py
```
2. Elegir opción del menú.
3. Ingresar función cuando se solicite.
4. Seleccionar variable de derivación.
5. Revisar resultados y gráficos.

