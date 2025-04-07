@echo off

REM Activate the virtual environment
call .venv\Scripts\activate.bat

REM Run the Python script
python main.py

REM Optional: Keep window open after script finishes
pause
