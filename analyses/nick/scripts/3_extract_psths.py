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
bin_centers, counts = compute_psth(spike_times=units, stim_times=stims['start_time'], bin_width=.01)
plt.plot(bin_centers, counts)


# %%
stims

# %%

spikes_rel = units - stims['start_time'][1]
trial_spikes = spikes_rel[(-0.5 <= spikes_rel) & (spikes_rel < 0.7)]
trial_spikes


# %% Get all
trials = {}
for _, stim in stims.iterrows():
    spikes_rel = units - stim['start_time']
    trial_spikes = spikes_rel[(-0.5 <= spikes_rel) & (spikes_rel < 0.7)]
    trial_spikes = trial_spikes.tolist()
    trial = {
        'start_time': stim.start_time,
        'x': stim.x_position,
        'y': stim.y_position,
        'ori': stim.orientation,
        'spikes': trial_spikes
    }

