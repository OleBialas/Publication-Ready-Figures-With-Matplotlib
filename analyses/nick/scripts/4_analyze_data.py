
# %%

import os
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
os.getcwd()


# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% Select a Session
session_dirs = list(Path('data/final').iterdir())
session_dir = session_dirs[2]

session_dir

# %% Load Data
df = pd.read_parquet(session_dir)
df

# %%
df.ecephys_structure_acronym.value_counts()


# %% Plot psth
for group, structure in dff.groupby('ecephys_structure_acronym'):
    plt.figure()
    sns.displot(data=structure, x='spike_time')
    plt.gca().set(title=f'{group} PSTs')