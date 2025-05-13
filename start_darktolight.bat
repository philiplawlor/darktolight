@echo off
REM Batch file to activate venv, install requirements, and launch the DarkToLight app

REM Activate the virtual environment
call "venv\Scripts\activate.bat"

REM Install required libraries (safe to re-run)
pip install -r requirements.txt

REM Launch the application
python tray_app.py
