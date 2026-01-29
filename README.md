# 🤖 RPA Bot - Automatización de Carga de Pólizas

Este proyecto es una solución de **Automatización Robótica de Procesos (RPA)** desarrollada en Python. Simula la carga masiva de pólizas de seguros desde un archivo Excel hacia un portal web de terceros, incluyendo la gestión de archivos adjuntos y resolución híbrida de Captchas.

## 🚀 Características Técnicas

* **Stack Tecnológico:** Python 3.10+, Playwright, Pandas, OpenPyXL.
* **Patrón de Diseño:** Iteración lineal sobre DataFrames con manejo de excepciones.
* **Human-in-the-Loop:** Sistema de pausa inteligente para detección y resolución manual de Captchas/Desafíos de seguridad.
* **Manejo de Archivos:** Lectura dinámica de Excel (.xlsx) y carga automatizada de PDFs en formularios web.

## 🛠️ Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Emapastrana21/RPA-Carga-Polizas.git](https://github.com/Emapastrana21/RPA-Carga-Polizas.git)
   cd RPA-Carga-Polizas

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

3.  **Ejecutar el Bot:**
    ```bash
    python bot.py
    ```

## 📋 Flujo del Proceso

1.  El script lee el archivo `datos.xlsx` usando **Pandas**.
2.  Inicia una instancia de navegador Chromium con **Playwright**.
3.  Navega al portal (simulado en `sitio_aseguradora.html`).
4.  Completa los campos del formulario mapeando los datos del Excel.
5.  Adjunta la documentación respaldatoria (`poliza_demo.pdf`).
6.  **Validación de Seguridad:** Si detecta un Captcha, pausa la ejecución y solicita intervención humana vía consola.
7.  Confirma la transacción y registra el éxito/error en la consola.


**Autor:** Emanuel Pastrana
