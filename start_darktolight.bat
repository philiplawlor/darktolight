@echo off
REM Batch file to activate venv, install requirements, and launch the DarkToLight app

REM Install required libraries (safe to re-run)
venv\Scripts\python.exe -m pip install -r requirements.txt

REM Launch the application using the venv Python
venv\Scripts\python.exe tray_app.py
