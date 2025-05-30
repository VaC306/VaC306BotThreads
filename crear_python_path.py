import subprocess
import os
import sys

def encontrar_python():
    try:
        # Intenta encontrar la ruta de python usando 'where' en Windows
        resultado = subprocess.check_output("where python", shell=True, text=True)
        rutas = resultado.strip().splitlines()

        for ruta in rutas:
            try:
                version = subprocess.check_output([ruta, "--version"], text=True)
                print(f"✅ Encontrado: {ruta} → {version.strip()}")
                return ruta  # Devuelve la primera válida
            except Exception:
                continue

        print("❌ No se pudo verificar ninguna instalación válida de Python.")
        return None

    except subprocess.CalledProcessError:
        print("❌ No se encontró 'python' en el PATH.")
        return None

def guardar_ruta(ruta):
    path_txt = os.path.join(os.path.dirname(__file__), "python_path.txt")
    with open(path_txt, "w", encoding="utf-8") as f:
        f.write(ruta)
    print(f"✅ Ruta guardada en '{path_txt}'")

if __name__ == "__main__":
    ruta_python = encontrar_python()
    if ruta_python:
        guardar_ruta(ruta_python)
    else:
        print("⚠️  Instala Python o agrégalo al PATH antes de continuar.")
        sys.exit(1)
