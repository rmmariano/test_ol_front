#!/bin/bash

# Caso uma excecao ocorra antes do "echo", ela eh lancada para o console
set -e  # If occur any error, exit
function to_console {
    echo -e "\n $1 \n"
}

# Create the virtualenv using the python3 in the folder called venv
virtualenv -p python3 venv/
# mkvirtualenv venv  # wrapper

to_console " --> Created the Virtualenv."

source venv/bin/activate
# workon venv  # wrapper
to_console " --> Activated the Virtualenv."

# requirements.txt needs to be in the root folder
pip install -r requirements.txt
to_console " --> Installed the requirements."

python main.py
to_console " --> Running the aplication."


