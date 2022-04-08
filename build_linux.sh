rm -rf __pycache__ build dist *.spec

pyinstaller --noconfirm --onefile --console --name "vlc-switch-config" "./switchconfig.py"
