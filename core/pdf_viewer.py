import os
import webbrowser

def mostrar_pdf_ayuda():
    ruta = os.path.abspath("docs/Guia_de_Uso.pdf")

    if not os.path.exists(ruta):
        print("\n⚠ No se encontró el archivo 'Guia_de_Uso.pdf' en la carpeta docs/.")
        print("Asegúrate de colocarlo allí.")
        return

    webbrowser.open(f"file:///{ruta}")
    print(f"\n📄 Abriendo documento: {ruta}")
