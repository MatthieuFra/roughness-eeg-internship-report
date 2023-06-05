# %%
# this script is used to preprocess the data into a usable mne epoch object
import mne
import matplotlib.pyplot as plt
import numpy as np
from mne.preprocessing import (ICA, corrmap, create_ecg_epochs,
                               create_eog_epochs)
%matplotlib widget
###############################################################

# %% paths
PROJECT_PATH = "/mnt/c/Users/educos/OneDrive - Institut Pasteur Paris/Documents/project/rxpaud"
SOURCE_DATA_PATH = os.path.join(PROJECT_PATH, "02_rxpaud_data/02_rxpaud_brainvision")
BIDS_ROOT_PATH = os.path.join(PROJECT_PATH, "02_rxpaud_data/03_rxpaud_bids")
RESULTS_PATH = os.path.join(PROJECT_PATH, "/04_rxpaud_results")
# select data
PROJECT_PATH = 'C:/Users/mfratice/Documents/DATA' #C:/Users/mfratice/Documents/DATA/RESULTS
SOURCE_DATA_PATH = 'C:/Users/mfratice/Documents/DATA/RESULTS'
BIDS_ROOT_PATH = 'C:/Users/mfratice/Documents/DATA/RESULTS' 
#'C:/Users/mfratice/Documents/DATA/BIDS'
RESULTS_PATH = 'C:/Users/mfratice/Documents/DATA/RESULTS_PREPROCESSING'


# select data
sub = "HYQSWK"  # subject ID   2021062C003CB
ses = '20230509'  # date of the recording
task = 'roughxp'  # name of the task given in {"roughxp", "roughxprating", "roughxppassive"}
acq = 'qplus'  # name of the device/cap used in {"acticap", "rnet", "qplus"}
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
data['project_path'] = PROJECT_PATH
data['source_data_path'] = SOURCE_DATA_PATH
data['bids_root_path'] = BIDS_ROOT_PATH
data['line_freq'] = line_freq
data['stim_channel'] = stim_channel
data['results_path'] = RESULTS_PATH

#  open data###############################################################

# BIDS compliant fname
fname_root = f"sub-{data['sub']}_ses-{data['ses']}_task-{data['task']}_acq-{data['acq']}_{data['modality']}"
# BIDS compliant folder path
#bids_path = os.path.join(data['bids_root_path'], f"sub-{data['sub']}", f"ses-{data['ses']}", f"{data['modality']}")

# add the right extension
fname = 'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/bids/sub-HYQSWK_ses-20230509_task-Default_acq-qplus_run-001_eeg.fif'
fname2 = 'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/bids/sub-HYQSWK_ses-20230509_task-Default_acq-rnet_run-001_eeg.fif'
# open .fif data into MNE
raw = mne.io.read_raw(fname, allow_maxshield=False, preload=True, on_split_missing='raise')# %%
#%%

raw.plot(block=True)

#%%
channels = {
    'P3': 'eeg',
    'P4': 'eeg',
    'AF3': 'eeg',
    'AF4': 'eeg',
     }

raw.set_channel_types(channels)

montage = mne.channels.make_standard_montage('standard_1020')
raw.set_montage(montage, verbose=False)

# %% preprocessing on raw data###############################################################
# filter line noise 50 Hz
freqs_linenoise = (50, 100)
raw = raw.copy().notch_filter(freqs=freqs_linenoise, picks='eeg')
# band pass filter (0.5 - 250 Hz)
raw = raw.copy().filter(l_freq=1, h_freq=100, picks='eeg')


# %% drop channels (needs to be automatized for every subject)
#'Fp1', 'Fp2', 'F9', 'F10'
ch_names_to_drop = ['Fp1','Fp2', 'P7', 'P9', 'F10', 'F9', 'F7', 'F3']

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
eog_indices, eog_scores = ica.find_bads_eog(raw, ch_name='Fp1')
ica.exclude = eog_indices

# barplot of ICA component "EOG match" scores
# ica.plot_scores(eog_scores)

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





#%%
# open .fif data into MNE
raw_events = mne.io.read_raw(fname2, allow_maxshield=False, preload=True, on_split_missing='raise')# %%

# homemade code to create events with stim 
events = mne.find_events(raw_events, stim_channel = 'Markers', shortest_event=1)

#
events_track = events[:, 0]
events_track = 250*events_track/(1000)


#
events_track_rounded = []
for index in range(len(events_track)):
    events_track_rounded.append(int(events_track[index]))

#
event_onsets_of_interest = []
for index in range(0, len(events_track)-1):
    if events_track_rounded[index + 1] - events_track_rounded[index] > 250:
        event_onsets_of_interest.append(events_track_rounded[index+1])

#
events_track_rounded = np.array(events_track_rounded)
event_onsets_of_interest = np.array(event_onsets_of_interest)

#
events[:, 0] = events_track
#
events = events[np.isin(events_track_rounded,event_onsets_of_interest)]

#
epochs = mne.Epochs(raw, events, tmin=-0.5, preload=True,
    tmax=1.5, baseline=(-0.3, -0.1), reject=None, proj=False, reject_by_annotation=None)

#%%
epochs_to_drop = [0, 10]
epochs.drop(epochs_to_drop)

#%%
epochs.info
#%%
epochs.drop_log

#%%
raw.info

#%%
epochs.drop_channels(ch_names=ch_names_to_drop)

# %% look at the raw data
raw.compute_psd(picks='eeg').plot()
# %%
raw.compute_psd().plot(average=True)

# %%
mne.viz.plot_events(events=events, event_id=event_id, sfreq=raw.info['sfreq'])

#%%
epochs.plot(picks='eeg', block=True)
# %%
mne.viz.plot_epochs(epochs)
# %% 
epochs.compute_psd().plot()
# %%
epochs.average(picks='eeg').plot(gfp=True)

# 
# create a BIDS compliant filename
filename = f"sub-{data['sub']}_ses-{data['ses']}_task-{data['task']}_acq-{data['acq']}_epoch.fif"
# create a BIDS compliant folder structure
save_path = 'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/epochs'
# save as .fif in a BIDS format
epochs.save(fname=os.path.join(save_path, filename), overwrite=True)
# %%
