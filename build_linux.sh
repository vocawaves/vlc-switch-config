rm -rf __pycache__ build dist *.spec

pyinstaller --noconfirm --onefile --console  "./switchconfig.py"
