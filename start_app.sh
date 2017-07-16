#!/bin/bash

# chmod +x start_app.sh

# Caso uma excecao ocorra antes do "echo", ela eh lancada para o console
set -e  # If occur any error, exit
function to_console {
    echo -e "\n $1 \n"
}

source venv/bin/activate
# workon venv  # wrapper
to_console " --> Activated the Virtualenv."

python main.py

deactivate
to_console " --> Deactivated the Virtualenv."
