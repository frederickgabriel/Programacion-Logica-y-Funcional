#  Sistema Experto Vocacional (TecNM)

Este proyecto es un **Sistema Experto** diseñado para orientar a los estudiantes en la elección de su carrera universitaria. Utiliza un motor de inferencia lógico desarrollado en **Prolog** para evaluar perfiles, conectado a una interfaz web moderna mediante **Python (Flask)**.

##  Tecnologías Utilizadas
* **Backend:** Python 3, Flask.
* **Motor de Inferencia Lógica:** SWI-Prolog (librería `pyswip`).
* **Frontend:** HTML5, CSS3 (Diseño Glassmorphism y animaciones fluidas).

---

##  Requisitos Previos

Para que el programa funcione correctamente en su computadora, es indispensable contar con el siguiente software instalado:

1. **Python 3.x** (Preferiblemente versión 3.8 o superior).
2. **SWI-Prolog:** Debido a que el sistema utiliza `pyswip`, el motor de SWI-Prolog debe estar instalado en el sistema operativo. 
   * *Nota importante:* Asegúrese de que la arquitectura de SWI-Prolog (32 o 64 bits) coincida con la arquitectura de su instalación de Python.

---

##  Instrucciones de Instalación y Ejecución

Siga estos pasos desde la terminal de su sistema (Símbolo del sistema, PowerShell o terminal de VS Code) para correr el proyecto localmente.

### Paso 1: Abrir el proyecto
Abra la carpeta del proyecto en su editor de código preferido (ej. Visual Studio Code) o navegue hasta ella usando la terminal.

### Paso 2: Crear un entorno virtual (Recomendado)
Para evitar conflictos con otras librerías, cree un entorno virtual ejecutando:
```bash
python -m venv .venv

Paso 3: Activar el entorno virtual

source .venv/bin/activate

Paso 4: Instalar las dependencias
Instale las librerías necesarias (Flask y Pyswip) ejecutando el siguiente comando:

python -m pip install flask pyswip

Paso 5: Iniciar el Servidor
Ejecute el archivo principal para levantar el servidor web de Flask:

python app.py

Paso 6: Abrir la Aplicación
Si la consola muestra un mensaje indicando que el servidor está corriendo (ej. * Running on http://127.0.0.1:5000), abra su navegador web e ingrese a la siguiente dirección:

 http://127.0.0.1:5000

structura del Proyecto
El repositorio está organizado de la siguiente manera para separar la lógica, el servidor y el diseño:
📦 Sistema_Experto_Vocacional
 ┣ 📜 app.py            # Archivo principal de Flask (Enrutamiento y API)
 ┣ 📜 sistema.py        # Lógica intermedia para decodificar datos
 ┣ 📜 carreras.pl       # Base de Conocimientos y Reglas Lógicas (Prolog)
 ┣ 📂 static
 ┃ ┗ 📜 estilos.css     # Hoja de estilos (Diseño moderno e interactivo)
 ┗ 📂 templates
   ┗ 📜 index.html      # Interfaz de usuario principal

Posibles Errores Comunes
Error de existencia carreras.pl: Asegúrese de estar ejecutando python app.py exactamente desde la carpeta raíz del proyecto, no desde subcarpetas.

Error de importación de pyswip: Suele ocurrir si SWI-Prolog no está instalado en la computadora de prueba o si no está agregado a las variables de entorno (PATH) del sistema.