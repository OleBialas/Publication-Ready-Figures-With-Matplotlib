
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

# %%
dff = df[(-0.1 < df['spike_time']) & (df['spike_time'] < 0.2)]
dff

# %%
structure = dff.groupby('ecephys_structure_acronym').get_group('VISam')
sns.displot(data=structure, x='spike_time')
ax = plt.gca()
ax.set(title='VISpm PSTs')
