PROYECTO EDUCATIVO: RASTREADOR DE TECLADO (VERSIÓN SIMPLE)

Este proyecto es una implementación mínima de un rastreador de pulsaciones (keylogger) en Python, diseñado estrictamente con fines educativos y de seguridad informática para demostrar la funcionalidad básica.

DISCLAIMER IMPORTANTE: El uso de este código para monitorear o acceder a información de terceros sin su consentimiento es ilegal y no ético. La responsabilidad de su uso recae enteramente sobre el usuario.

⚙️ Dependencias

Este script requiere la librería de Python keyboard.

pip install keyboard


🚀 Ejecución

Guarde el código seleccionado como keylogger_simple.py y ejecútelo desde su terminal:

python keylogger_simple.py


🛑 Detención del Script

Dado que el código utiliza un bucle while True para mantenerse activo, debe detenerlo manualmente. Presione la combinación:

$$\text{CTRL} + \text{C}$$

💾 Funcionamiento y Archivo de Registro

Creación del Log: La línea open(log_file, 'w').close() asegura que el archivo log.txt se cree (o se vacíe si ya existe) en el mismo directorio donde se ejecuta el script.

Registro de Teclas: El script utiliza una función lambda concisa con keyboard.hook para registrar el nombre de cada tecla presionada (event.name) directamente en el archivo log.txt.

Ubicación: El archivo log.txt se encontrará en la misma carpeta desde donde ejecutó el comando python.
