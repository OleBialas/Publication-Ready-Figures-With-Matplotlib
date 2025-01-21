# %%
import os
from pathlib import Path
from shutil import copy
os.chdir(Path(__file__).parent.parent)
os.getcwd()


os.makedirs('src', exist_ok=True)
copy('../../utils.py', 'src/utils.py')