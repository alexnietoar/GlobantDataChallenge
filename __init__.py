import subprocess
import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

src_dir = os.path.join(ROOT_DIR, 'src')
sys.path.append(src_dir)

with open(os.path.join(ROOT_DIR, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

def check_installed_libraries():
    missing_libraries = []
    for requirement in requirements:
        try:
            __import__(requirement)
        except ImportError:
            subprocess.check_call(["pip", "install", requirement])

# Ejecutar el código de main.py
from main import main

if __name__ == '__main__':
    main()