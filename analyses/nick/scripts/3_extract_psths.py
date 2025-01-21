
# %%
from shutil import copy
import numpy as np
import pandas as pd
from pathlib import Path
from src.utils import compute_psth

import os
os.chdir(Path(__file__).parent.parent)
os.getcwd()

# %%
session_dirs = list(Path('data/processed').iterdir())
session_dir = session_dirs[0]
session_dir

# %%
print(list(session_dir.iterdir()))

# %%
