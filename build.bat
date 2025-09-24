@echo off
echo === Building PDF Tool EXE ===
pip install -r requirements.txt
pyinstaller --onefile --noconsole pdf_tool.py
echo.
echo Done! Check the "dist" folder for pdf_tool.exe
pause
