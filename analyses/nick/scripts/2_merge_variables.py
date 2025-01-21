

# %%
import os
from pathlib import Path
from shutil import copy, copytree
from typing import TypedDict
import numpy as np
import pandas as pd
import xarray as xr

os.chdir(Path(__file__).parent.parent)

# %%
Path.cwd()

# %%
session_dirs = list(Path('data/raw').iterdir())
print(session_dirs)
for session_dir in session_dirs:
    session_dir

    # %%
    session_name = session_dir.name.replace('ses_', '')
    session_name

    # %%
    processed_dir = Path(f'data/processed/{session_name}')
    processed_dir.mkdir(exist_ok=True, parents=True)


    # %% Get Stimuli
    stims = pd.read_csv(list(session_dir.glob('*_stimuli.csv'))[0])
    gabor_stims = stims[stims['stimulus_name'] == 'gabors'][['start_time', 'x_position', 'y_position', 'orientation']]
    gabor_stims.to_csv(processed_dir / 'stims.csv', index=False)
    gabor_stims


    # %%  Load Spike Times
    spike_times_path = list(session_dir.glob('*_spike_times.npy'))[0]
    spike_times = np.load(spike_times_path, allow_pickle=True).item()
    spike_times
    print(spike_times.keys())
    list(spike_times.values())[0].shape
    copy(spike_times_path, str(processed_dir / 'spike_times.npy'))
    spike_times



