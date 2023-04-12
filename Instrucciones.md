## Miercoles 12 de Abril

## Crear el entorno de python

1 - Manual

- Windows

​		`py -m venv env` (3.11.2)

​		`~\AppData\local\Programs\Python\Python39\python -m venv env` (3.9.10)

- MacOS y Linux

  `python3 -m venv env`

2 - Automatica con el IDE

`vs code`

- View -> Command Pallet Ctrl+Shift+P
  - Python:Create enviroment
    - Seleccionar: venv
    - Version de Python del entorno virtual

## Activar el entorno virtual de Pythoon

1 - Manual

- Windows power shell	

​		`env\Scripts\activate.ps1`

- Windows command line

  `env\scripts\activate.bat`

- MacOS y Linux

  `source nombrecarpeta/bin/activate`

2- Automatica con el IDE

	- En cuanto el IDE detecta un venv, o env o .venv activara el entorno en la carpeta de trabajo.

## Desactivar el entorno virtual de Python

1 - Manual 

`deactivate ` (Válido para Windows y MacOS o Linux)

2 - Automática con el IDE

​	Cerrando la carpeta de trabajo

## Generar el fichero de requirements

Desde la linea de comandos y con entorno activo

`pip freeze > requirements.txt` 

## Añadir al Readme

- Instrucciones de instalación
  - Clonar el repositorio
    - git clone url del proyecto
  - Crear y activar el entorno virtual
    - Version de Python que esta realizado el proyecto (Instalar si no esta presente)
    - Instrucciones (py -m venv env ) tanto para windows como para MacOs
  - Instalar las librerias
    - `pip install -r requirements.txt`

- Instrucciones de ejecución
  - py menu1.py