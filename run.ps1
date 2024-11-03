# Ejecutar en PowerShell

# Activar el entorno virtual para Django
& .\analizador_venv\Scripts\Activate.ps1

# Iniciar el servidor de Django
Start-Process -FilePath "python" -ArgumentList "manage.py runserver" -WorkingDirectory "backend\analizador"

# Iniciar el servidor de Angular
Start-Process -FilePath "ng" -ArgumentList "serve", "--open" -WorkingDirectory "frontend\Analizador"

# Esperar a que ambos procesos terminen
Wait-Process
