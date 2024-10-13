@echo off
REM Navigate to the directory where your MALWWA.py script is located
cd /d %~dp0

REM Run the pyinstaller command
pyinstaller --onefile --noconsole --add-data "config.json;." MALWWA.py

REM Pause to keep the window open in case of errors
pause
