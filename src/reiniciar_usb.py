import subprocess
import time
import urllib.request
from datetime import datetime

# ID do dispositivo a ser reiniciado
hwid = "HID\\VID_17EF&PID_6019"

# Tempo entre verificações (em segundos)
tempo = 300  # 5 minutos

# Caminho do arquivo de log
log_path = "log_internet.txt"

def tem_internet():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=5)
        return True
    except:
        return False

def registrar_queda():
    horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensagem = f"[{horario}] 🚫 Internet caiu.\n"
    print(mensagem.strip())
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(mensagem)

def restart_usb(hardware_id, devcon_path="devcon"):
    try:
        print(f"Tentando desativar: {hardware_id}")
        subprocess.run([devcon_path, "disable", hardware_id], check=True)
        time.sleep(2)
        print(f"Tentando ativar: {hardware_id}")
        subprocess.run([devcon_path, "enable", hardware_id], check=True)
        print("✅ Dispositivo reiniciado com sucesso.")
    except:
        try:
            print(f"Tentando reiniciar: {hardware_id}")
            subprocess.run([devcon_path, "restart", hardware_id], check=True)
            time.sleep(2)
        except subprocess.CalledProcessError as e:
            print("❌ Erro ao reiniciar o dispositivo:", e)

def main():
    print("⏳ Verificando conexão com a internet...")
    if tem_internet():
        print("✅ Conectado à internet.")
    else:
        registrar_queda()
        restart_usb(hwid)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(tempo)
