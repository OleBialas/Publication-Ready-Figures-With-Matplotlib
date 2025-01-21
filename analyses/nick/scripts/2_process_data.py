

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

# %%
for session_dir in session_dirs:

# %%
    session_dir = session_dirs[0]
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
    gabor_stims.to_parquet(processed_dir / 'stims.parquet')
    gabor_stims

    # %%  Load Spike Times
    
    spike_times = np.load(list(session_dir.glob('*_spike_times.npy'))[0], allow_pickle=True).item()
    units = pd.read_csv(list(session_dir.glob('*_units.csv'))[0]).set_index('unit_id')
    
    st = pd.Series(data=list(spike_times.values()), index=list(spike_times.keys()), name='spike_times')
    
    units2 = units.copy()
    units2['spike_times'] = st
    units2.to_parquet(processed_dir / 'units.parquet')


# %%
units2




