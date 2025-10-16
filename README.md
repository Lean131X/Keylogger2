# ⌨️ Keylogger Básico - Práctica de Ciberseguridad Educacional

## (Uso Ético y Legal)

Este proyecto fue desarrollado **exclusivamente con fines educativos** para comprender la mecánica interna de un keylogger. Su objetivo es la investigación de seguridad y el desarrollo de contramedidas en entornos controlados y autorizados.

**El uso de este código para actividades no éticas, ilegales o sin el consentimiento explícito y previo de los usuarios y/o propietarios del sistema está estrictamente prohibido y es responsabilidad exclusiva del usuario.**

---

## Objetivo de la Actividad

Implementar un keylogger simple en Python, utilizando la librería `keyboard`, para registrar las pulsaciones de teclas en un sistema operativo y almacenarlas en un archivo de registro (`log.txt`).

##  Requisitos

* **Python:** Versión 3.10 o superior (recomendado).
* **Librería:** `keyboard` (instalada a través de `requirements.txt`).

##  Instalación

1.  **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/Lean131X/Keylogger2.git
    cd [nombre-del-repositorio]
    ```

2.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Ejemplos de Ejecución

### 1. Iniciar el Keylogger

Ejecuta el script principal desde tu terminal:

```bash
python main.py
```
2. Detener la Grabación
Para detener el keylogger y finalizar la sesión de registro, presiona
```
Ctrl + C en la terminal.
```
4. Revisar el Archivo de Registro (log.txt)
El script guardará automáticamente todas las pulsaciones de teclas en el archivo log.txt.

Contenido de log.txt (Ejemplo de pulsaciones):

Si el usuario escribió "Hola Mundo [Enter] 123 [Tab]", el archivo log.txt registrará:
```
h o l a space m u n d o space enter 1 2 3 tab [SHIFT] [CTRL] [ALT] space
```
(Nota: La librería keyboard registra las teclas especiales con su nombre, lo cual facilita la identificación de acciones como enter, space, tab, ctrl, etc.)

 Estructura del Proyecto
```
.
├── main.py             # Código principal del keylogger.
├── requirements.txt    # Lista de dependencias (keyboard).
├── README.md           # Este archivo de documentación.
└── log.txt             # (Generado al ejecutar) Archivo de registro de logs.
```
