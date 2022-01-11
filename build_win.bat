rmdir /s /q __pycache__ build dist
del *.spec

pyinstaller --noconfirm --onefile --console  "./switchconfig.py"
