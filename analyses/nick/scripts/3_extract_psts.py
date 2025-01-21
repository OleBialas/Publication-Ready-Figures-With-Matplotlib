# %%

import os
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
os.getcwd()

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tqdm import tqdm

# %% Select a Sessoin
session_dirs = list(Path('data/processed').iterdir())

for session_dir in session_dirs[1:]:
# session_dir = session_dirs[0]
    session_dir


    # %% Read Stimulus Data
    stims = pd.read_parquet(session_dir / 'stims.parquet')
    stims

    # %% Read Units Data

    units = pd.read_parquet(session_dir / 'units.parquet')
    units

    #

    # %% Make sure you have spike times

    unit = units.iloc[0]
    unit.spike_times
    unit['ecephys_structure_acronym']
    # %%
    stims

    # %%

    responses = []
    # for unit_id, unit in units.iterrows():
    for stim_id, stim in tqdm(stims.iterrows(), total=len(stims)):
        for unit_id, unit in units.iterrows():
            spikes_rel = unit.spike_times - stim.start_time
            spikes_rel[(-0.5 <= spikes_rel) & (spikes_rel < 0.7)]
            trial_spikes = spikes_rel[(-1.5 <= spikes_rel) & (spikes_rel < 1.5)]
            trial_spikes

            for ts in trial_spikes:
                response = {
                    'session_id': int(session_dir.name),
                    'unit_id': unit_id,
                    'ecephys_structure_acronym': unit['ecephys_structure_acronym'],
                    'stim_id': stim_id,
                    'stim_x': stim['x_position'],
                    'stim_y': stim['y_position'],
                    'stim_ori': stim['orientation'],
                    'spike_time': ts,
                }
                responses.append(response)

    final = pd.DataFrame(responses)

    final_dir = Path('data/final')
    final_dir.mkdir(parents=True, exist_ok=True)
    final.to_parquet(final_dir / f"{session_dir.name}.parquet")



# %% Get all
