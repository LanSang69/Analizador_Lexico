# Ejecutar en PowerShell

# Comprobando si Python está instalado
if (Get-Command python3 -ErrorAction SilentlyContinue) {
    Write-Output "Python3 ya está instalado."
} else {
    Write-Output "Instalando Python3..."
    
    # Python Installer para Windows
    $pythonInstallerUrl = "https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe"
    $pythonInstallerPath = "$env:TEMP\python-installer.exe"
    
    Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $pythonInstallerPath
    Start-Process -FilePath $pythonInstallerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    Remove-Item $pythonInstallerPath
}

# Comprobando si pip está instalado
if (Get-Command pip3 -ErrorAction SilentlyContinue) {
    Write-Output "pip3 ya está instalado."
} else {
    Write-Output "Instalando pip3..."

    # Descargar get-pip.py
    $pipScriptUrl = "https://bootstrap.pypa.io/get-pip.py"
    $pipScriptPath = "$env:TEMP\get-pip.py"
    Invoke-WebRequest -Uri $pipScriptUrl -OutFile $pipScriptPath

    # Ejecutar el script para instalar pip
    python3 $pipScriptPath
    Remove-Item $pipScriptPath
}

# Mostrar versiones de Python y pip
Write-Output "Python version: $(python3 --version)"
Write-Output "pip version: $(pip3 --version)"

# Configurando el entorno virtual para Django
if (Test-Path "analizador_venv") {
    Write-Output "El entorno virtual ya existe."
} else {
    python3 -m venv analizador_venv
}

# Activar el entorno virtual
& .\analizador_venv\Scripts\Activate.ps1

# Instalar paquetes de requirements.txt
if (Test-Path "requirements.txt") {
    Write-Output "Instalando paquetes desde requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Output "El archivo requirements.txt no existe."
    exit 1
}

Write-Output "Instalación de entorno Django completada."

# Verificar si npm está instalado
if (Get-Command npm -ErrorAction SilentlyContinue) {
    Write-Output "npm ya está instalado."
} else {
    Write-Output "Instalando npm..."
    
    # Instalador de Node.js y npm para Windows
    $nodeInstallerUrl = "https://nodejs.org/dist/v20.12.2/node-v20.12.2-x64.msi"
    $nodeInstallerPath = "$env:TEMP\node-installer.msi"
    
    Invoke-WebRequest -Uri $nodeInstallerUrl -OutFile $nodeInstallerPath
    Start-Process -FilePath msiexec.exe -ArgumentList "/i $nodeInstallerPath /quiet /norestart" -Wait
    Remove-Item $nodeInstallerPath
}

Write-Output "Node.js version: $(node -v)"

# Instalar Angular CLI
if (Get-Command ng -ErrorAction SilentlyContinue) {
    Write-Output "Angular ya está instalado."
} else {
    Write-Output "Instalando Angular CLI..."
    npm install -g @angular/cli
}

# Cambiar al directorio y ejecutar npm install
$frontendPath = ".\frontend\Analizador"
if (Test-Path $frontendPath) {
    Set-Location $frontendPath
    Write-Output "Ejecutando npm install..."
    npm install
} else {
    Write-Output "Error: No se encontró el directorio frontend/Analizador."
    exit 1
}
