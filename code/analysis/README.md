# Code for analysis 


Here you will find the Python Scripts I've been using for the analysis.

I used Visual Studio Code, using a jupyter-like interface, with '#%%' to delimit cells of code. 

You can find : 

## Electroencephalography analysis 

- eeg_analysis_xdf_reader.ipynb

> An old code using Jupyter Notebook to go from XDF files (of LabStreamingLayer) to MNE-compatible FIF files. 

- rxmbt_preprocess_rnet.py

> This code is designed to preprocess the FIF data from the R-Net headset, extract events from the triggers and create epochs of the signal for each participant. 

- rxmbt_preprocess_qplus.py

> This code is designed to preprocess the FIF data from the Q+ headset, extract events from the triggers and create epochs of the signal for each participant. 

- rxmbt_preprocess_evoked_potentials.py

> This code is designed to export MNE Evoked potentials object, for each participant, for both headset.

- rxmbt_preprocess_evoked_potentials_group.py

> This code is designed to concatenate multiple participants together or by conditions and to plot ERPs. 



## Behavioural analysis 

- rxmbt_behavioural_analyses_scrapping.py

> This code is designed to Scrap the PsychoPy data from a .txt file and save it into a CSV. 

- rxmbt_behavioural_analyses_psydat_scrapping.py

> This code is designed to Scrap the PsychoPy data from a .psydat file and save it into a CSV. 

- rxmbt_behavioural_analyses_csv_mean.py

> This code is designed to manipulate and merge different CSV to unified differents datas for each participants.

- rxmbt_behavioural_analyses_plot_figure.py

> This code is designed to plot the figures used in the report, using MatPlotlib.

- rxmbt_behavioural_analyses_plot_figure_regression.py

> This code is designed to plot the regression figures used in the report, using MatPlotlib.





### Required librairies for the code :

- mne
- matplotlib
- numpy
- mne-bids
- sklearn
- re
- os
- glob
- pandas

### MNE System used :  

Platform             Windows-10-10.0.19045-SP0
Python               3.11.3 | packaged by conda-forge | (main, Apr  6 2023, 08:50:54) [MSC v.1934 64 bit (AMD64)]
Executable           c:\Users\mfratice\AppData\Local\anaconda3\envs\mne\python.exe
CPU                  Intel64 Family 6 Model 154 Stepping 3, GenuineIntel (20 cores)
Memory               31.7 GB

#### Core

├☑ mne               1.4.0

├☑ numpy             1.24.3 (MKL 2022.1-Product with 14 threads)

├☑ scipy             1.10.1

├☑ matplotlib        3.7.1 (backend=module://ipympl.backend_nbagg)

├☑ pooch             1.7.0

└☑ jinja2            3.1.2


#### Numerical (optional)

├☑ sklearn           1.2.2

├☑ numba             0.57.0

├☑ nibabel           5.1.0

├☑ nilearn           0.10.1

├☑ dipy              1.7.0

├☑ openmeeg          2.5.6

├☑ pandas            2.0.2

└☐ unavailable       cupy


#### Visualization (optional)

├☑ pyvista           0.39.1 (OpenGL 4.5.0 - Build 31.0.101.3959 via Intel(R) Iris(R) Xe Graphics)

├☑ pyvistaqt         0.0.0

├☑ ipyvtklink        0.2.2

├☑ vtk               9.2.6

├☑ qtpy              2.3.1 (PyQt5=5.15.6)

├☑ ipympl            0.9.3

├☑ pyqtgraph         0.13.3

└☑ mne-qt-browser    0.5.0


#### Ecosystem (optional)

├☑ mne-bids          0.12

└☐ unavailable       mne-nirs, mne-features, mne-connectivity, mne-icalabel, mne-bids-pipeline
