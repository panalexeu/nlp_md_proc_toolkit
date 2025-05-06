import subprocess
from pathlib import Path

if __name__ == '__main__':
    parent = Path(__file__).resolve().parent
    subprocess.run(['streamlit', 'run', f'{parent}/csv_editor/app.py'])
