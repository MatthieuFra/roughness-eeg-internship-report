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
sub = "XOTAFR"  # subject ID   2021062C003CB
ses = '20230522'  # date of the recording
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
data['line_freq'] = line_freq
data['stim_channel'] = stim_channel


#  open data###############################################################

fname = 'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/epochs/sub-XOTAFR_ses-20230522_task-roughxp_acq-qplus_epoch.fif'

# open .fif data into MNE
epochs = mne.read_epochs(fname, preload=True)# %%


#evoked.drop_channels(['Fp2'])

evoked = epochs.average()

evoked.plot()


# create a BIDS compliant filename
filename = f"sub-{data['sub']}_ses-{data['ses']}_task-{data['task']}_acq-{data['acq']}_evoked.fif"
# create a BIDS compliant folder structure
save_path = 'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked'
# save as .fif in a BIDS format
evoked.save(fname=os.path.join(save_path, filename), overwrite=True)
# %%
