import pandas as pd
import os
import time
from playwright.sync_api import sync_playwright

# --- CONFIGURACIÓN ---
# Buscamos la ruta de tu archivo HTML (asegurate que se llame igual)
ruta_html = os.path.abspath("sitio_aseguradora.html")
url_local = f"file:///{ruta_html}"

print("Leyendo Excel...")
# Leemos el archivo usando el motor openpyxl
df = pd.read_excel("datos.xlsx", engine="openpyxl")

# --- INICIO DEL BOT ---
with sync_playwright() as p:
    # Lanzamos el navegador en modo visible (headless=False)
    # slow_mo=500 hace que el bot espere medio segundo entre acciones (para que lo veas)
    browser = p.chromium.launch(headless=False, slow_mo=2000) 
    page = browser.new_page()

    print("\n--- INICIANDO CARGA ROBOTIZADA ---")

    for indice, fila in df.iterrows():
        print(f"Procesando a: {fila['Nombre']}")

        # 1. Navegar al sitio
        page.goto(url_local)

        # 2. Llenar campos
        page.fill('#aseguradora', str(fila['Aseguradora']))
        page.fill('#poliza', str(fila['Poliza']))
        
        # Manejo del Select (convertimos a minúsculas para coincidir con el HTML)
        barrio = str(fila['Barrio']).lower()
        page.select_option('#barrio', barrio)

        page.fill('#dni', str(fila['DNI']))
        page.fill('#nombre_completo', str(fila['Nombre']))

        # Fechas (formato año-mes-día)
        fecha_inicio = fila['Inicio'].strftime('%Y-%m-%d')
        fecha_fin = fila['Fin'].strftime('%Y-%m-%d')
        page.fill('#fecha_inicio', fecha_inicio)
        # ... (código anterior de las fechas)
        page.fill('#fecha_fin', fecha_fin)

        # --- NUEVO: CARGA DE ARCHIVO ---
        print("Adjuntando PDF...")
        # Buscamos el input que tiene id="documentacion" y le cargamos el archivo
        # Nota: Asumimos que el archivo 'poliza_demo.pdf' está en la misma carpeta
        path_pdf = os.path.abspath("poliza_demo.pdf") 
        page.set_input_files('#documentacion', path_pdf)
        
        # 3. Click en Enviar
        print("Enviando formulario...")
        # ...
        # 3. Click en Enviar
        print("Enviando formulario...")
        page.click('button[type="submit"]')

        # 4. Esperar confirmación
        try:
            page.wait_for_selector('#mensaje-exito', state='visible', timeout=5000)
            print("✅ Carga exitosa.")
        except:
            print("❌ Error: Tiempo de espera agotado.")

        time.sleep(1) # Pausa breve

    print("\n--- FIN DEL PROCESO ---")
    browser.close()