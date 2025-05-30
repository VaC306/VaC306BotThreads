# 🤖 Threads AutoPoster – Flask Edition

Este proyecto combina un **bot automatizado en Python** para publicar en Instagram Threads con una **interfaz web en Flask**. Ahora puedes:

- Subir tu Excel de mensajes.
- Gestionar cuentas (añadir / eliminar hasta 5).
- Arrancar / detener el bot con un solo clic.
- Ver en tiempo real el **log de publicaciones** y la **cuenta atrás**.

---

## 📌 Descripción

1. **Backend (“bot/”)**  
   - Usa Appium + ADB para controlar emuladores Android y la app `com.instagram.barcelona`.  
   - Lee mensajes de `bot/mensajes.xlsx` y cuentas de `bot/accounts.json`.  
   - Cicla: publica un mensaje por cuenta, espera 10 minutos (mostrable en la web) y repite indefinidamente.  
   - Registra todo en `bot/log_publicaciones.txt` y en `bot/countdown.json` para la cuenta atrás.

2. **Interfaz Flask**  
   - **Index** (`/`): sube Excel, lanza/detiene el bot, muestra estado, cuenta atrás y log en vivo.  
   - **Gestionar cuentas** (`/seleccionar_cuentas`): lista, añade y elimina hasta 5 cuentas.  

---

## ⚙️ Tecnologías

- **Python 3.10+**  
- **Flask 3.x** (templates, static, JSON endpoints)  
- **Appium-Python-Client** (UiAutomator2)  
- **ADB & Android Emulator SDK**  
- **openpyxl** (leer `.xlsx`)  
- **Bootstrap 5** (estilos responsive)

---

## 📁 Estructura

threads-app/
├── app.py ← Servidor Flask
├── requirements.txt ← Dependencias (Flask, Appium,…)
├── templates/
│ ├── index.html ← UI principal
│ └── accounts.html ← Gestión de cuentas
├── static/
│ └── styles.css ← Estilos custom + Bootstrap CDN
└── bot/
├── bot.py ← Lógica de publicación
├── lanzar_appium_multi.py
├── liberar_puerto.py
├── reiniciar_emuladores.py
├── verify.py
├── mensajes.xlsx ← Excel de mensajes
├── accounts.json ← Listado de cuentas (máx. 5)
└── log_publicaciones.txt ← Log de ejecución


---

## 🚀 Instalación & Ejecución

1. **Clona el repositorio**  
   ```bash
   git clone https://github.com/TU_USUARIO/threads-app.git
   cd threads-app

2. **Crea y activa tu virtualenv**
    python -m venv .venv
    # PowerShell:
    . .\.venv\Scripts\Activate.ps1
    # CMD:
    .venv\Scripts\activate.bat

3. **Instala dependencias**
    pip install -r requirements.txt

4. **Configura tus emuladores y appium**
    Asegúrate de tener AVDs creados (por ejemplo Pixel_7) y Appium instalado
    Ajusta nombres de AVD o puertos en bot.py si es necesario.

5. **Arranca el servidor Flask**
    python app.py

    Por defecto escuchará en http://127.0.0.1:5000/.


🍔 Uso

    Sube tu Excel (.xlsx) con los mensajes (una frase por fila, desde la segunda).

    Haz clic en “⚙️ Gestionar cuentas” para añadir o eliminar cuentas (máximo 5).

    Vuelve al Inicio y pulsa “🚀 Lanzar” para arrancar el bot.

    Mira en tiempo real la barra de progreso (cuenta atrás) y el log de publicaciones.

    Para detener el bot, pulsa “✋ Detener”.


🔒 Aviso Legal

Este proyecto es solo con fines educativos y de práctica con Appium y Flask.
El uso de bots en plataformas de terceros puede violar sus TOS.
⚠️ No me responsabilizo de usos indebidos.

Autor: VaC306
