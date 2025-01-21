# %%

import os
os.chdir(Path(__file__).parent.parent)
os.getcwd()

# %%
from shutil import copy
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


from src.utils import compute_psth

# %% Select a Sessoin
session_dirs = list(Path('data/processed').iterdir())
session_dir = session_dirs[0]
session_dir


# %% Read Data
stims = pd.read_csv(session_dir / 'stims.csv')
spikes = np.load(session_dir / 'spike_times.npy', allow_pickle=True).item()
stims, spikes

# %%
units = spikes[915957872]

# %%
start_time = stims['start_time']
start_time


bin_centers, counts = compute_psth(spike_times=units, stim_times=start_time, bin_width=.01)
plt.plot(bin_centers, counts)
