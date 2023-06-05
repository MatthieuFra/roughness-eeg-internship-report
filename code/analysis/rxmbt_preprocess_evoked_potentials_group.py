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
sub = "ZAFAUS"  # subject ID   2021062C003CB
ses = '20230516'  # date of the recording
task = 'roughxp'  # name of the task given in {"roughxp", "roughxprating", "roughxppassive"}
acq = 'qplus'  # name of the device/cap used in {"acticap", "qplus", "qplus"}
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

fname = 'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/roughxpmbt/04_roughxpmbt_results/epochs/sub-ZAFAUS_ses-20230516_task-roughxp_acq-qplus_epoch.fif'

# open .fif data into MNE
epochs = mne.read_epochs(fname, preload=True)# %%

#%%

conditions = ['Global']

data_files = [
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-BICUHE_ses-20230515_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-BOPYLF_ses-20230512_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-CCIERR_ses-20230512_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-CMUVBJ_ses-20230516_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-DURJIL_ses-20230517_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-FKCBDA_ses-20230522_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-FMLJCT_ses-20230516_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-FNLVBL_ses-20230515_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-GCYIJW_ses-20230509_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-GWONVA_ses-20230510_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-HYQSWK_ses-20230509_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-KTQRFK_ses-20230515_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-LRSHEM_ses-20230515_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-LWZRSF_ses-20230509_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-QBKAZX_ses-20230522_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-RABIKZ_ses-20230517_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-RSQQVJ_ses-20230512_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-SLIZVT_ses-20230517_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-SQOYJP_ses-20230522_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-TSSJPF_ses-20230511_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-UUPHMI_ses-20230509_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-VCMVJY_ses-20230522_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-WPYIVO_ses-20230522_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-XDFFWN_ses-20230511_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-XOTAFR_ses-20230522_task-roughxp_acq-qplus_evoked.fif',
'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-ZAFAUS_ses-20230516_task-roughxp_acq-qplus_evoked.fif',
]
#evoked.drop_channels(['Fp2'])


#%%

evoked1 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-BICUHE_ses-20230515_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked2 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-BOPYLF_ses-20230512_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked3 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-CCIERR_ses-20230515_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked4 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-CMUVBJ_ses-20230516_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked5 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-DURJIL_ses-20230517_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked6 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-FKCBDA_ses-20230522_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked7 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-FMLJCT_ses-20230516_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked8 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-FNLVBL_ses-20230515_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked9 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-GCYIJW_ses-20230509_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked10 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-GWONVA_ses-20230510_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked11 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-HYQSWK_ses-20230509_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked12 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-KTQRFK_ses-20230515_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked13 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-LRSHEM_ses-20230515_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked14 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-LWZRSF_ses-20230509_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked15 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-QBKAZX_ses-20230522_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked16 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-RABIKZ_ses-20230517_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked17 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-RSQQVJ_ses-20230512_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked18 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-SLIZVT_ses-20230517_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked19 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-SQOYJP_ses-20230522_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked20 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-TSSJPF_ses-20230511_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked21 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-UUPHMI_ses-20230509_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked22 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-VCMVJY_ses-20230522_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked23 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-WPYIVO_ses-20230522_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked24 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-XDFFWN_ses-20230511_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked25 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-XOTAFR_ses-20230522_task-roughxp_acq-qplus_evoked.fif', condition= 0)
evoked26 = mne.read_evokeds('C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked/sub-ZAFAUS_ses-20230516_task-roughxp_acq-qplus_evoked.fif', condition= 0)

#%%

channels_to_pick = ['C3', 'Cz', 'C4', 'P3', 'Pz', 'P4']

evoked1.pick_channels(channels_to_pick)
evoked2.pick_channels(channels_to_pick)
evoked3.pick_channels(channels_to_pick)
evoked4.pick_channels(channels_to_pick)
evoked5.pick_channels(channels_to_pick)
evoked6.pick_channels(channels_to_pick)
evoked7.pick_channels(channels_to_pick)
evoked8.pick_channels(channels_to_pick)
evoked9.pick_channels(channels_to_pick)
evoked10.pick_channels(channels_to_pick)
evoked11.pick_channels(channels_to_pick)
evoked12.pick_channels(channels_to_pick)
evoked13.pick_channels(channels_to_pick)
evoked14.pick_channels(channels_to_pick)
evoked15.pick_channels(channels_to_pick)
evoked16.pick_channels(channels_to_pick)
evoked17.pick_channels(channels_to_pick)
evoked18.pick_channels(channels_to_pick)
evoked19.pick_channels(channels_to_pick)
evoked20.pick_channels(channels_to_pick)
evoked21.pick_channels(channels_to_pick)
evoked22.pick_channels(channels_to_pick)
evoked23.pick_channels(channels_to_pick)
evoked24.pick_channels(channels_to_pick)
evoked25.pick_channels(channels_to_pick)
evoked26.pick_channels(channels_to_pick)


#%%

evoked1.plot()
evoked2.plot()
evoked3.plot()
evoked4.plot()
evoked5.plot()
evoked6.plot()
evoked7.plot()
evoked8.plot()
evoked9.plot()
evoked10.plot()
evoked11.plot()
evoked12.plot()
evoked13.plot()
evoked14.plot()
evoked15.plot()
evoked16.plot()
evoked17.plot()
evoked18.plot()
evoked19.plot()
evoked20.plot()
evoked21.plot()
evoked22.plot()
evoked23.plot()
evoked24.plot()
evoked25.plot()
evoked26.plot()

#%%

all_evoked = [
    evoked1,
    evoked2,
    evoked3,
    evoked4,
    evoked5,
    evoked6,
    evoked7,
    evoked8,
    evoked9,
    evoked10,
    evoked11,
    evoked12,
    evoked13,
    evoked14,
    evoked15,
    evoked16,
    evoked17,
    evoked18,
    evoked19,
    evoked20,
    evoked21,
    evoked22,
    evoked23,
    evoked24,
    evoked25,
    evoked26,
]
#%%
big_evoked = mne.combine_evoked(all_evoked, weights= 'equal')

#%%

big_evoked.filter(l_freq=1, h_freq=30, picks='eeg')
#%%
big_evoked.plot()

#%%

# create a BIDS compliant filename
filename = f"sub-{data['sub']}_ses-{data['ses']}_task-{data['task']}_acq-{data['acq']}_evoked.fif"
# create a BIDS compliant folder structure
save_path = 'C:/Users/mfratice/OneDrive - Institut Pasteur Paris/Documents/IDA_STAGE/DATA/data/data_analyzed/evoked'
# save as .fif in a BIDS format
evoked.save(fname=os.path.join(save_path, filename), overwrite=True)
# %%
