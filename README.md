# Calculadora de Derivadas Parciales 🔣🧠

La **Calculadora de Derivadas Parciales** es una herramienta en Python diseñada para analizar y derivar funciones multivariables de forma simbólica.  
Permite calcular derivadas parciales respecto a las variables `x`, `y` o `z`, corregir expresiones mal escritas mediante un validador inteligente y visualizar funciones con gráficos automáticos en 2D y 3D.

Su objetivo es facilitar la comprensión de los conceptos del cálculo multivariable y ofrecer una experiencia robusta, clara y educativa.

---

## ✨ Características principales

- 🔢 **Cálculo simbólico de derivadas parciales** usando SymPy.  
- 🧠 **Smart Validator PRO** para corregir errores comunes como:
  - `sinx` → `sin(x)`
  - `3x` → `3*x`
  - `xy` → `x*y`
  - `x^2` → `x**2`
  - `logx` → `log(x)`
  - `e^x` → `exp(x)`
- ✔ **Validación completa** de funciones matemáticas permitidas.
- 📊 **Visualización gráfica automática**:
  - Funciones de 1 variable → gráfico 2D.
  - Funciones de 2 variables → superficie 3D.
  - Funciones de 3 variables → análisis simbólico.
- 🧩 **Arquitectura modular** que facilita mantenimiento y ampliación.
- 📚 **Guía PDF integrada**, accesible desde el menú de ayuda.

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
- Librerías necesarias:
  ```
  sympy
  numpy
  matplotlib
  ```

---

## 📐 Funcionamiento

1. El usuario ingresa una función simbólica.  
2. El Smart Validator PRO analiza la expresión y propone correcciones si es necesario.  
3. La función se valida y se interpreta simbólicamente.  
4. Se detectan automáticamente las variables presentes.  
5. Se solicita la variable respecto a la cual derivar.  
6. Se calcula la derivada parcial.  
7. Se genera una gráfica si la función tiene 1 o 2 variables.

---

## ▶️ Uso de la aplicación

1. Ejecutar el programa con:
   ```
   python main.py
   ```
2. Seleccionar una opción del menú principal.  
3. Ingresar la función cuando sea solicitada.  
4. Elegir la variable respecto a la cual se desea derivar.  
5. Revisar la derivada parcial y, si aplica, la gráfica generada.

---

## 🎥 Video del proyecto

Puedes ver la presentación actual del proyecto en el siguiente enlace.  
En ella se explica su funcionamiento general y el propósito de la herramienta.  
**Próximamente se publicará una versión actualizada del video acorde a la nueva refactorización.**

🔗 **Video en YouTube:**  
https://youtu.be/phOc49ZBe78?si=VyfiGjAS-yPkG5He

<div align="center">
  <a href="https://youtu.be/phOc49ZBe78?si=VyfiGjAS-yPkG5He" target="_blank">
    <img src="https://github.com/user-attachments/assets/4083f0ff-2a6a-40c5-ab05-a08310c623d6" width="800" alt="Video del Proyecto - Calculadora de Derivadas Parciales">
  </a>
</div>

---

## 💬 Gracias por llegar hasta aquí

Si deseas conocer más sobre este proyecto o aprender a instalarlo y ejecutarlo, puedes visitar las redes sociales disponibles en el perfil del repositorio.

- 🎥 YouTube: https://www.youtube.com/@ErickPerez_8  
- 📸 Instagram: https://www.instagram.com/erickperez_8/

¡Gracias por visitar este proyecto! 💻✨

