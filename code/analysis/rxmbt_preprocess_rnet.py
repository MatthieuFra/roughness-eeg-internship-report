# %%
# this script is used to preprocess the data into a usable mne epoch object
import mne
import matplotlib.pyplot as plt
import numpy as np
from mne.preprocessing import (ICA, corrmap, create_ecg_epochs,
                               create_eog_epochs)
%matplotlib widget
###############################################################
#%% Info sys
mne.sys_info()
#
# %% paths

# select data
sub = "BOPYLF"  # subject ID   2021062C003CB
ses = '20230512'  # date of the recording
task = 'roughxp'  # name of the task given in {"roughxp", "roughxprating", "roughxppassive"}
acq = 'rnet'  # name of the device/cap used in {"acticap", "rnet", "qplus"}
run = '001'
modality = 'eeg'  # name of the data modality / BIDS suffix
stim_channel = 'STIM'  # name of the auxiliary channel containing the auditory stimulus
line_freq = 50.

###############################################################
# create a dictionnary to communicate easily between functions
data = dict()
data['sub'] = sub
data['ses'] = ses
data['task'] = task
data['acq'] = acq
data['run'] = run
data['modality'] = modality
data['line_freq'] = line_freq
data['stim_channel'] = stim_channel


#  open data###############################################################

fname = 'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/bids/sub-BOPYLF_ses-20230512_task-Default_acq-rnet_run-001_eeg.fif'

# open .fif data into MNE
raw = mne.io.read_raw(fname, allow_maxshield=False, preload=True, on_split_missing='raise')# %%


channels = {
    'Fp1': 'eog',
    'Fz': 'eeg',
    'F3': 'eeg',
    'F7': 'eeg',
    'F9': 'eeg',
    'FC5': 'eeg',
    'FC1': 'eeg',
    'C3': 'eeg',
    'T7': 'eeg',
    'CP5': 'eeg',
    'CP1': 'eeg',
    'Pz': 'eeg',
    'P3': 'eeg',
    'P7': 'eeg',
    'P9': 'eeg',
    'O1': 'eeg',
    'Oz': 'eeg',
    'O2': 'eeg',
    'P10': 'eeg',
    'P8': 'eeg',
    'P4': 'eeg',
    'CP2': 'eeg',
    'CP6': 'eeg',
    'T8': 'eeg',
    'C4': 'eeg',
    'Cz': 'eeg',
    'FC2': 'eeg',
    'FC6': 'eeg',
    'F10': 'eeg',
    'F8': 'eeg',
    'F4': 'eeg',
    'Fp2': 'eeg',
    'STIM': 'stim',
    'Markers': 'misc',
    'EMG': 'emg',
    'ECG': 'ecg',

     }

raw.set_channel_types(channels)

montage = mne.channels.make_standard_montage('standard_1020')
raw.set_montage(montage, verbose=False)

# %% preprocessing on raw data###############################################################
# filter line noise 50 Hz
freqs_linenoise = (50, 100, 150, 200, 250, 300, 350, 400, 450)
raw = raw.copy().notch_filter(freqs=freqs_linenoise, picks='eeg')
# band pass filter (0.5 - 250 Hz)
raw = raw.copy().filter(l_freq=0.1, h_freq=100, picks='eeg')

#%% AFTER LINE NOISE FILTER

raw.plot(block=True)

# %% drop channels (needs to be automatized for every subject)
#'Fp1', 'Fp2', 'F9', 'F10'
ch_names_to_drop = ['Fp1']

#%%
raw.drop_channels(ch_names=ch_names_to_drop)

# %% ica eog
raw_ica = raw.copy().filter(l_freq=1, h_freq=None, picks='eeg')
ica = ICA()
ica.fit(raw_ica)
# %%
# ica.plot_sources(raw)
# %%
ica.exclude = []
#find which ICs match the EOG patter,
eog_indices, eog_scores = ica.find_bads_eog(raw, ch_name='Fp2')
ica.exclude = eog_indices

#%% barplot of ICA component "EOG match" scores
ica.plot_scores(eog_scores)

# plot diagnostics
# ica.plot_properties(raw, picks=eog_indices)

# plot ICs applied to raw data, with EOG matches highlighted
# ica.plot_sources(raw, show_scrollbars=False)

# plot ICs applied to the averaged EOG epochs, with EOG matches highlighted
# ica.plot_sources(eog_evoked)

#%%
ica.plot_sources(raw_ica)

#%%
ica.plot_components()

#%%
# ica.apply() changes the Raw object in-place, so let's make a copy first:
raw_copy = raw.copy()
ica.apply(raw)

#%% AFTER ICA

raw.plot(block=True)

#%% homemade code to create events with stim 
events_track = mne.find_events(raw, stim_channel = 'Markers', shortest_event=1)


#events_track

#fig, ax = plt.subplots()
#ax.vlines(events_track, ymax=1, ymin=0)
#ax.vlines(event_onsets_of_interest, ymin=0.5, ymax=1.5, color='k')

events_track = events_track[:, 0]
event_onsets_of_interest = []
for index in range(0, len(events_track)-1):
    if events_track[index + 1] - events_track[index] > 1000:
        event_onsets_of_interest.append(events_track[index+1])

events = mne.find_events(raw, stim_channel = 'Markers', shortest_event=1)
events = events[np.isin(events[:, 0],event_onsets_of_interest)]


epochs = mne.Epochs(raw, events, tmin=-0.5, 
    tmax=1.5, baseline=(-0.3, -0.1), preload=True)

#%%
epochs_to_drop = [0, 34, 48, 91, 94, 97, 100, 101, 109, 111, 118, 119, 120, 128, 136, 149, 163, 168, 169, 170, 171, 172, 173, 216]
epochs.drop(epochs_to_drop)





#%%
epochs.drop_channels(ch_names=['Fp2'])

# %% look at the raw data
raw.compute_psd(picks='eeg').plot()
# %%
raw.compute_psd().plot(average=True)

# %%
mne.viz.plot_events(events=events, event_id=event_id, sfreq=raw.info['sfreq'])

#%%
epochs.plot(picks='all', block=True)
# %%
mne.viz.plot_epochs(epochs)
# %% 
epochs.compute_psd().plot()
# %%
epochs.average(picks='eeg').plot(gfp=True)
# %%
epochs.average().plot()

# %%
# create a BIDS compliant filename
filename = f"sub-{data['sub']}_ses-{data['ses']}_task-{data['task']}_acq-{data['acq']}_epoch.fif"
# create a BIDS compliant folder structure
save_path = 'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/epochs'
# save as .fif in a BIDS format
epochs.save(fname=os.path.join(save_path, filename), overwrite=True)
# %%
