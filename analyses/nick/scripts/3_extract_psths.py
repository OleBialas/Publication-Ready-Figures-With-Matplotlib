# %%

import os
os.chdir(Path(__file__).parent.parent)
os.getcwd()

# %%
from shutil import copy
import numpy as np
import pandas as pd
from pathlib import Path


from src.utils import compute_psth

# %%
session_dirs = list(Path('data/processed').iterdir())
session_dir = session_dirs[0]
session_dir

# %%
print(list(session_dir.iterdir()))

# %%
stims = pd.read_csv(session_dir / 'stims.csv')
spikes = np.load(session_dir / 'spike_times.npy', allow_pickle=True).item()
stims, spikes

