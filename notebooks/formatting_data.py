










from pathlib import Path
from typing import List
import pandas as pd
import numpy as np
from pynwb import NWBHDF5IO, NWBFile
from allensdk.brain_observatory.ecephys.ecephys_project_cache import EcephysProjectCache





root = Path('/home/obi/projects/Publication-Ready-Figures-With-Matplotlib')
cache = EcephysProjectCache.from_warehouse(manifest=root/"data"/"raw"/"manifest.json")
SESSION_TYPE="brain_observatory_1.1"
ROI = ["VISpm", "VISrl", "VISam"] # primary, rostrolateral and anteriormedial visual cortex
STIMULI = ["gabors", "flashes", "drift_gratings", "static_gratings", "natural_scenes"]
GENOTYPES = ["wt/wt"]





sessions = cache.get_session_table()
sessions = sessions[sessions.session_type==SESSION_TYPE]
sessions = sessions[sessions.full_genotype.isin(GENOTYPES)]





#| label: session-loop
session_id = sessions.index[0]
for session_id in sessions.index:
    session = cache.get_session_data(session_id)





#| ref.label: subject-loop
    units = session.units
    unit_in_ROI = []
    for i in units.index:
        structure = units.loc[i].ecephys_structure_acronym
        if structure in ROI:
            unit_in_ROI.append(True)
        else:
            unit_in_ROI.append(False)
    units = units[unit_in_ROI]






#| ref.label: subject-loop
    mean_waveforms = session.mean_waveforms
    mean_waveforms_out = {}
    mean_waveforms_out["time"] = mean_waveforms[units.index[0]].time.data
    for i in units.index:
        w = mean_waveforms[i].data
        ptp = w.max(axis=1)-w.min(axis=1)
        idx = np.argmax(ptp) # waveform with largest peak-to-peak ampitude
        mean_waveforms_out[i] = w[idx, :]





#| ref.label: subject-loop
    spike_times = session.spike_times
    spike_times_out = {}
    for i in units.index:
        spike_times_out[i] = spike_times[i]






#| ref.label: subject-loop
    stimuli = session.get_stimulus_table()
    stimuli = stimuli[stimuli.stimulus_name.isin(STIMULI)]






#| ref.label: subject-loop
    out_dir = root/"data"/f"ses_{session_id}"
    if not out_dir.exists():
        out_dir.mkdir()
    units.to_csv(out_dir/f"ses_{session_id}_units.csv")
    stimuli.to_csv(out_dir/f"ses_{session_id}_stimuli.csv")
    np.save(out_dir/f"ses_{session_id}_mean_waveforms.npy", mean_waveforms_out, allow_pickle=True)
    np.save(out_dir/f"ses_{session_id}_spike_times.npy", spike_times_out, allow_pickle=True)
