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


def compute_cross_correlogram( spikes1, spikes2, bin_size = 0.001, win_size = 0.1, normalize = True):
    n_bins = int(win_size / bin_size)
    if n_bins % 2 == 0:
        n_bins += 1
    bins = np.linspace(-win_size/2, win_size/2, n_bins + 1)
    bin_centers = bins[:-1] + bin_size/2

    counts = np.zeros(n_bins)
    for spike1 in spikes1:
        is_close = np.abs(spikes2 - spike1) <= win_size/2
        differences = spikes2[is_close] - spike1
        hist, _ = np.histogram(differences, bins=bins)
        counts += hist

    if normalize:
        rate = len(spikes2) / (spikes2.max()-spikes2.min())
        counts = counts / (rate * win_size * len(spikes1))

    return bin_centers, counts
