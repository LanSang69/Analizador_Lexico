#!/bin/bash

set -e

# Django Server
(
    source analizador_venv/bin/activate
    cd backend/analizador
    python manage.py runserver || { echo "No se pudo iniciar el servidor Django"; exit 1; }
) &

# Angular Server
(
    cd frontend/Analizador
    ng serve --open || { echo "No se pudo iniciar el servidor Angular"; exit 1; }
) &

wait
