<div align="center">
  <a href="https://discord.com/users/elpursi_306_" target="_blank">
    <img src="https://img.shields.io/badge/🗨️_Contáctame_en_Discord_-elpursi_306_-7289da?style=for-the-badge&logo=discord&logoColor=white"/>
  </a>
</div>


# 🤖 Threads AutoPoster – Desktop Edition (PyWebView)

Este proyecto combina un **bot automatizado en Python** para publicar en Instagram Threads con una **interfaz de escritorio embebida usando PyWebView**. Ya no necesitas abrir tu navegador: todo está integrado en una app GUI nativa.

---

## ✨ Características

- Subida de archivo `.xlsx` con frases.
- Gestión visual de hasta 5 cuentas Threads (añadir / eliminar).
- Publicación automática y cíclica cada 10 minutos.
- Compatible con múltiples **dispositivos físicos Android** vía USB.
- Log de publicaciones en tiempo real y cuenta atrás visual.
- Tema claro/oscuro y diseño responsive con Bootstrap.

---

## 📌 Descripción Técnica

1. **Bot (“bot/”)**
   - Usa Appium + ADB para controlar dispositivos Android físicos conectados por USB.
   - Lee mensajes desde `bot/mensajes.xlsx` y las cuentas desde `bot/accounts.json`.
   - Ejecuta publicaciones en cada cuenta conectada → espera 10 minutos → repite.
   - Todo se guarda en `bot/log_publicaciones.txt` y `bot/countdown.json`.

2. **Interfaz de Escritorio con PyWebView**
   - Renderiza los archivos `index.html` y `accounts.html` como si fuera una app web.
   - La lógica del backend (subidas, estado del bot, logs, etc.) se ejecuta con Flask embebido.
   - El backend usa hilos y subprocesses para lanzar el bot y manejar los puertos Appium.

---

## ⚙️ Tecnologías Usadas

- **Python 3.10+**
- **PyWebView** (para la GUI)
- **Flask** (embebido en segundo plano, sin navegador)
- **Appium-Python-Client** (UiAutomator2)
- **ADB** (Android Debug Bridge)
- **openpyxl** (para leer archivos `.xlsx`)
- **Bootstrap 5** (estilo visual)
- **cryptography** (licencias)

---

## 📁 Estructura del Proyecto

threads-app/
├── app.py ← Lanza la GUI con PyWebView
├── requirements.txt ← Dependencias
├── templates/
│ ├── index.html ← Pantalla principal (subida, estado, log)
│ └── accounts.html ← Pantalla de gestión de cuentas
├── static/
│ └── styles.css ← Tema claro/oscuro + estilo Bootstrap
├── license.key ← Licencia de uso
├── public_key.pem ← Clave pública para validación de licencia
├── python_path.txt ← Ruta del ejecutable de Python
├── bot/
│ ├── bot.py ← Lógica principal del bot
│ ├── lanzar_appium_multi.py
│ ├── liberar_puerto.py
│ ├── reiniciar_emuladores.py
│ ├── verify.py
│ ├── mensajes.xlsx ← Archivo con frases (una por fila)
│ ├── accounts.json ← Hasta 5 cuentas Threads
│ ├── log_publicaciones.txt
│ └── countdown.json ← Tiempo restante (actualizado por el bot)


---

## 🚀 Instalación & Ejecución

### 1. Clona el repositorio:
Descargar los archivos del release mas actual

### 2. Configura entorno Android

    Instala Node.js + npm

    Instala Appium globalmente:

npm install -g appium
appium driver install uiautomator2

Asegúrate de que tienes ANDROID_HOME y ANDROID_SDK_ROOT configurados.

Verifica con:

    verificar_entorno.py

### 3. Ejecuta la app

haz click en VaC306BotThreads.exe


🧠 Uso

    En la interfaz:

        Sube tu Excel .xlsx con las frases desde la segunda fila.

        Añade hasta 5 cuentas Threads desde el apartado ⚙️ “Gestionar cuentas”.

        Pulsa 🚀 Lanzar para comenzar.

        Observa en vivo el log y la cuenta atrás.

        Pulsa ✋ Detener para parar el ciclo de publicación.

🔐 Licencia

Este software requiere una licencia válida (license.key) firmada con tu clave privada. La licencia se valida al inicio con public_key.pem.
⚠️ Aviso Legal

Este proyecto es solo con fines educativos y de práctica con automatización móvil.
El uso de bots en redes sociales puede violar sus términos de uso.

Autor: VaC306
