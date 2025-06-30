import subprocess
import time
import urllib.request

def tem_internet():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=5)
        return True
    except:
        return False

def restart_usb(hardware_id, devcon_path="devcon"):
    try:
        print(f"Tentando desativar: {hardware_id}")
        subprocess.run([devcon_path, "disable", hardware_id], check=True)
        time.sleep(2)
        print(f"Tentando ativar: {hardware_id}")
        subprocess.run([devcon_path, "enable", hardware_id], check=True)
        print("✅ Dispositivo reiniciado com sucesso.")
    except subprocess.CalledProcessError as e:
        print("❌ Erro ao reiniciar o dispositivo:", e)

def main():
    print("⏳ Verificando conexão com a internet...")
    if tem_internet():
        print("✅ Conectado à internet.")
    else:
        print("🚫 Sem conexão com a internet.")
        hwid = input("Digite o hardware ID do dispositivo USB a reiniciar (ex: @HID\\VID_17EF&PID_6019*): ")
        restart_usb(hwid)

if __name__ == "__main__":
    main()
