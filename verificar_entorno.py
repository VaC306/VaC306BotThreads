import subprocess
import shutil
import os
import time
import signal
import psutil

def comprobar_comando(nombre):
    ruta = shutil.which(nombre)
    if ruta:
        print(f"✅ '{nombre}' está instalado en: {ruta}")
        return True
    else:
        print(f"❌ '{nombre}' no está disponible en el PATH del sistema.")
        return False

def version_comando(nombre):
    try:
        resultado = subprocess.run(f"{nombre} --version", capture_output=True, text=True, shell=True)
        if resultado.returncode == 0:
            print(f"ℹ️  {nombre} versión: {resultado.stdout.strip()}")
        else:
            print(f"⚠️  Error ejecutando '{nombre} --version'")
    except Exception as e:
        print(f"⚠️  No se pudo verificar la versión de '{nombre}': {e}'")

def comprobar_uiautomator2_driver():
    try:
        resultado = subprocess.run(
            "appium driver list",
            capture_output=True,
            text=True,
            shell=True
        )
        output = (resultado.stdout + resultado.stderr).lower()
        lines = output.splitlines()

        for line in lines:
            if "uiautomator2" in line and "installed" in line:
                print("✅ appium-uiautomator2-driver está instalado correctamente.")
                return
        print("❌ appium-uiautomator2-driver no está instalado o no se detecta.")
        print("💡 Instálalo con: appium driver install uiautomator2")
    except Exception as e:
        print(f"⚠️ No se pudo verificar appium-uiautomator2-driver: {e}")





def comprobar_vars_entorno():
    android_home = os.environ.get("ANDROID_HOME")
    sdk_root = os.environ.get("ANDROID_SDK_ROOT")

    if android_home:
        print(f"✅ ANDROID_HOME = {android_home}")
    else:
        print("❌ Variable ANDROID_HOME no está definida. Crea la variable de entorno!")

    if sdk_root:
        print(f"✅ ANDROID_SDK_ROOT = {sdk_root}")
    else:
        print("❌ Variable ANDROID_SDK_ROOT no está definida. Crea la variable de entorno!")

    adb_path = shutil.which("adb")
    if adb_path:
        print(f"✅ adb está en el PATH: {adb_path}")
    else:
        print("❌ adb no encontrado en el PATH")

    emulator_path = shutil.which("emulator")
    if emulator_path:
        print(f"✅ emulator está en el PATH: {emulator_path}")
    else:
        print("❌ emulator no encontrado en el PATH")

def cerrar_ventanas_appium_emuladores():
    print("\n🧹 Cerrando procesos abiertos de Appium y emuladores...\n")
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['cmdline']:
                cmd = " ".join(proc.info['cmdline']).lower()
                if "appium" in cmd or "emulator" in cmd:
                    print(f"⛔ Cerrando proceso PID {proc.pid}: {proc.name()}")
                    proc.send_signal(signal.SIGTERM)
        except Exception:
            continue
    time.sleep(1)
    print("✅ Limpieza completada.\n")

def main():
    print("🔍 Verificando entorno para dispositivo USB con Appium:\n")

    todo_ok = True

    cerrar_ventanas_appium_emuladores()

    # Verificar Node.js / npm
    if comprobar_comando("npm"):
        version_comando("npm")
    else:
        todo_ok = False
        print("💡 Instala Node.js desde: https://nodejs.org/")

    # Verificar Appium
    if comprobar_comando("appium"):
        version_comando("appium")
        comprobar_uiautomator2_driver()
    else:
        todo_ok = False
        print("💡 Instala Appium con: npm install -g appium")

    comprobar_vars_entorno()

    if todo_ok:
        print("\n✅ Todo listo para usar Appium con USB.")
    else:
        print("\n⚠️  Faltan dependencias para usar el modo USB.")

if __name__ == "__main__":
    main()
