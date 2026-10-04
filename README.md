# 🧪 QA Automation Project - Talentotech

Este proyecto contiene un framework de pruebas automatizadas desarrollado para la pre-entrega del curso de **Talentotech**. 

## 🎯 Objetivo del Proyecto

El objetivo de la primera entrega de este proyecto es aplicar los conocimientos adquiridos hasta la mitad del curso, demostrando mi capacidad para automatizar flujos básicos de navegación web utilizando Selenium WebDriver y Python. 

Este proyecto permite poner en práctica lo aprendido sobre interacción con elementos web, estrategias de localización y validación de estados en una página. El sitio objetivo para esta automatización será [saucedemo.com](https://saucedemo.com), una aplicación web demo especialmente diseñada para prácticas de testing.

---

## 🛠️ Tecnologías Utilizadas

* 🐍 **Python** (Lenguaje de programación principal)
* 🚀 **Pytest** (Framework de pruebas)
* 🌐 **Selenium WebDriver** (Herramienta de automatización web)
* 📊 **Pytest-HTML** (Generación de reportes visuales en HTML)
* 🐙 **Git y GitHub** (Control de versiones y repositorio remoto)

---

## 📦 Instalación y Configuración

Sigue estos pasos para clonar el proyecto y configurar tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   cd prelab-automation
   ```

2. **Crear y activar el entorno virtual (VENV):**
   * En Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   * En Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Nota: Asegurate de tener instalado Google Chrome o el navegador de tu preferencia compatible con el WebDriver de tu proyecto)*

---

## 💻 Ejecución de las Pruebas

Para correr las pruebas dispones de los siguientes comandos en tu terminal:

* 🏃‍♂️ **Ejecución estándar:** Corre todos los tests generando el reporte HTML automático.
  ```bash
  pytest
  ```

* 📝 **Ejecución con logs acumulativos (PowerShell):** Ejecuta las pruebas en modo detallado, muestra el progreso en consola y guarda un histórico acumulado en la carpeta de reportes.
  ```powershell
  pytest -v | Tee-Object -FilePath "reports/pruebas_acumuladas.log" -Append
  ```

---

## 📊 Reportes y Resultados

Tras cada ejecución, podrás encontrar los siguientes artefactos en tu proyecto:
* 📂 `reporte.html` - Reporte visual interactivo con el estado final de cada test.
* 📄 `reports/pruebas_acumuladas.log` - Historial de texto con el log acumulado de las ejecuciones realizadas.

