
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
dfs = []
for session_dir in session_dirs:
    dd = pd.read_parquet(session_dir)
    dfs.append(dd)

df = pd.concat(dfs, ignore_index=True)
df.info()


# %% Load Data

dff = df[(-0.05 <= df['spike_time']) & (df['spike_time'] <= 0.25)]
dff.info()

# %%
df.ecephys_structure_acronym.value_counts()


# %% Plot psth
figs = []
groups = []
for group, structure in dff.groupby('ecephys_structure_acronym'):
    plt.figure()
    sns.displot(data=structure, x='spike_time')
    plt.gca().set(title=f'{group} PSTs')
    fig = plt.gcf()
    fig.savefig(f'../../figures/psth_{group}.png')
    figs.append(fig)
    groups.append(group)
    
# %%
import pickle
for group, fig in zip(groups, figs):
    with open(f'../../figures/psth_{group}.pkl', 'wb') as f:
        pickle.dump(fig, f)
# %%

with open(f'../../figures/psth_VISrl.pkl', 'rb') as f:
    ff = pickle.load(f)

ff
