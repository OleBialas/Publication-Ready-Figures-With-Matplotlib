
# %%

import os
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
os.getcwd()

# %%
import pandas as pd


# %% Select a Session
session_dirs = list(Path('data/final').iterdir())
session_dir = session_dirs[0]

session_dir

# %% Load Data
df = pd.read_parquet(session_dir)
df


