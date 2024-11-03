#!/bin/bash

set -e

if command -v python3 &>/dev/null; then
    echo "Python3 ya está instalado."
else
    echo "Instalando Python3..."

    sudo apt update
    if ! sudo apt install -y python3; then
        echo "Error al instalar Python3."
        exit 1
    fi
fi

if command -v pip3 &>/dev/null; then
    echo "pip3 ya está instalado."
else
    echo "Instalando pip3..."

    if ! curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; then
        echo "Error al descargar get-pip.py."
        exit 1
    fi

    if ! python3 get-pip.py --user; then
        echo "Error al instalar pip3."
        rm get-pip.py
        exit 1
    fi

    rm get-pip.py
fi

echo "Python version: $(python3 --version)"
echo "pip version: $(pip3 --version)"

# Para Django:
# Creando el entorno virtual
if [ -d "analizador_venv" ]; then
    echo "El entorno virtual ya existe."
else
    if ! python3 -m venv analizador_venv; then
        echo "Error al crear el entorno virtual."
        exit 1
    fi
fi

if ! source analizador_venv/bin/activate; then
    echo "Error al activar el entorno virtual."
    exit 1
fi

# Instalando Django
if [ -f "requirements.txt" ]; then
    echo "Instalando paquetes desde requirements.txt..."
    if ! python -m pip install -r requirements.txt; then
        echo "Error al instalar paquetes desde requirements.txt."
        exit 1
    fi
else
    echo "El archivo requirements.txt no existe."
    exit 1
fi

echo "Instalación de entorno Django completada."

# Para Angular
#Instalando npm
if command -v npm &>/dev/null; then
    echo "npm ya está instalado."
else
    echo "Instalando npm..."

    if ! sudo apt-get install -y npm; then
        echo "Error al instalar npm."
        exit 1
    fi
fi

# Instalando Node.js 20.12.2
if command -v node &>/dev/null && [ "$(node -v)" == "v20.12.2" ]; then
    echo "Node.js 20.12.2 ya está instalado."
else
    echo "Instalando Node.js 20.12.2..."

    # Descargar Node.js 20.12.2
    if ! curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -; then
        echo "Error al configurar el repositorio de NodeSource."
        exit 1
    fi

    if ! sudo apt-get install -y nodejs=20.12.2-1nodesource1; then
        echo "Error al instalar Node.js 20.12.2."
        exit 1
    fi
fi

echo "Node.js version: $(node -v)"

#Instalar Angular
if command -v ng &>/dev/null; then
    echo "Angular ya está instalado."
else
    echo "Instalando Angular..."

    if ! npm install -g @angular/cli; then
        echo "Error al instalar Angular."
        exit 1
    fi
fi