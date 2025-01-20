import numpy as np

def compute_psth(spike_times, stim_times, window=(-0.05, 0.25), bin_width=0.01):
    bins = np.arange(window[0], window[1] + bin_width, bin_width)
    bin_centers = bins[:-1] + bin_width/2
    counts = np.zeros(len(bins) - 1)
    for stim in stim_times:
        relative_times = spike_times - stim
        trial_counts, _ = np.histogram(relative_times, bins=bins)
        counts += trial_counts
    psth = counts / (bin_width * len(stim_times))
    return bin_centers, psth
