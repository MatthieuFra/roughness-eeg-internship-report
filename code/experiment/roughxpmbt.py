#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on March 21, 2023, at 13:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.1.0')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from oddball
from random import sample, randint
# Run 'Before Experiment' code from lsl
from pylsl import StreamInfo, StreamOutlet


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'roughxp'  # from the Builder filename that created this script
expInfo = {
    'subject': '',
    'serial port': 'COM',
    'trial number': '30',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'../01_raw/02_output-psychopy/%s_%s_%s/%s_%s_%s' % (expName, expInfo['date'], expInfo['subject'], expName, expInfo['date'], expInfo['subject'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\educos\\OneDrive - Institut Pasteur Paris\\Documents\\project\\roughxpmbt\\00_setup\\roughxpmbt.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "start" ---
instruction_text = visual.TextStim(win=win, name='instruction_text',
    text='Pour commencez, \nfaites un clic droit \nsur la souris',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# --- Initialize components for Routine "set_volume" ---
# Run 'Begin Experiment' code from changeVol
thisVol = .2
sound_test = sound.Sound('02_stimuli/90Hz.wav', secs=1.0, stereo=True, hamming=False,
    name='sound_test')
sound_test.setVolume(1.0)
upButton = visual.TextStim(win=win, name='upButton',
    text='cliquer ici\npour augmenter \nle volume ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
submitButton = visual.TextStim(win=win, name='submitButton',
    text='cliquez ici si le volume est supportable',
    font='Arial',
    pos=(0,-.4), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
replay = visual.TextStim(win=win, name='replay',
    text='cliquez ici \npour réécouter',
    font='Arial',
    pos=(0.6, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "instructions" ---
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Vous allez entendre des sons.\nLorsqu\'une échelle apparaît,\nveuillez noter les sons que vous avez entendus parmis : \n"neutre", "acceptable", "gênant", "insupportable", "horrible"\n\nLorsque vous êtes prêts, \nfaites un clic droit avec la souris',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "trial" ---
# Run 'Begin Experiment' code from oddball
nb_conditions = 9
nb_trials = nb_conditions * int(expInfo["trial number"])
percentage_oddballs = 20

nb_oddballs = round(percentage_oddballs/100 * nb_trials)

oddball_index_2n = sorted(sample(range(nb_trials), 2*nb_oddballs))
selection = list(range(randint(0,1), 2 * nb_oddballs, 2))
oddball_index = [oddball_index_2n[index] for index in selection]

oddballs = [False] * nb_trials
for index in oddball_index :
    oddballs[index] = True

# Run 'Begin Experiment' code from lsl
# Creating the LSL stream:
info = StreamInfo(name='TriggerStream', type='Markers', channel_count=1, channel_format='int32', source_id='BP_MI_Marker_stream_001') #Initialize LSL stream for markers
outlet = StreamOutlet(info)  # Broadcast the stream.
isi1 = visual.TextStim(win=win, name='isi1',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
sound1 = sound.Sound('A', secs=1.0, stereo=True, hamming=False,
    name='sound1')
sound1.setVolume(thisVol)
fix1 = visual.TextStim(win=win, name='fix1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
isi2 = visual.TextStim(win=win, name='isi2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
sound2 = sound.Sound('A', secs=1.0, stereo=True, hamming=False,
    name='sound2')
sound2.setVolume(thisVol)
fix2 = visual.TextStim(win=win, name='fix2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.05), pos=(0, 0), units=win.units,
    labels=["neutre", "acceptable", "gênant", "insupportable", "horrible"], ticks=(1, 2, 3, 4, 5), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, ori=0.0, depth=-8, readOnly=False)

# --- Initialize components for Routine "end" ---
end_key_resp = keyboard.Keyboard()
end_text = visual.TextStim(win=win, name='end_text',
    text='Merci pour votre participation',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "start" ---
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
startComponents = [instruction_text, mouse_2]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text* updates
    
    # if instruction_text is starting this frame...
    if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text.frameNStart = frameN  # exact frame index
        instruction_text.tStart = t  # local t and not account for scr refresh
        instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        instruction_text.status = STARTED
        instruction_text.setAutoDraw(True)
    
    # if instruction_text is active this frame...
    if instruction_text.status == STARTED:
        # update params
        pass
    # *mouse_2* updates
    
    # if mouse_2 is starting this frame...
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # end routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start" ---
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
volume_check_loop = data.TrialHandler(nReps=100.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='volume_check_loop')
thisExp.addLoop(volume_check_loop)  # add the loop to the experiment
thisVolume_check_loop = volume_check_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVolume_check_loop.rgb)
if thisVolume_check_loop != None:
    for paramName in thisVolume_check_loop:
        exec('{} = thisVolume_check_loop[paramName]'.format(paramName))

for thisVolume_check_loop in volume_check_loop:
    currentLoop = volume_check_loop
    # abbreviate parameter names if possible (e.g. rgb = thisVolume_check_loop.rgb)
    if thisVolume_check_loop != None:
        for paramName in thisVolume_check_loop:
            exec('{} = thisVolume_check_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "set_volume" ---
    continueRoutine = True
    # update component parameters for each repeat
    sound_test.setSound('02_stimuli/90Hz.wav', secs=1.0, hamming=False)
    sound_test.setVolume(thisVol, log=False)
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    set_volumeComponents = [sound_test, upButton, mouse, submitButton, replay]
    for thisComponent in set_volumeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "set_volume" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_test
        
        # if sound_test is starting this frame...
        if sound_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_test.frameNStart = frameN  # exact frame index
            sound_test.tStart = t  # local t and not account for scr refresh
            sound_test.tStartRefresh = tThisFlipGlobal  # on global time
            # update status
            sound_test.status = STARTED
            sound_test.play(when=win)  # sync with win flip
        
        # if sound_test is stopping this frame...
        if sound_test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_test.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_test.tStop = t  # not accounting for scr refresh
                sound_test.frameNStop = frameN  # exact frame index
                # update status
                sound_test.status = FINISHED
                sound_test.stop()
        
        # *upButton* updates
        
        # if upButton is starting this frame...
        if upButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            upButton.frameNStart = frameN  # exact frame index
            upButton.tStart = t  # local t and not account for scr refresh
            upButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(upButton, 'tStartRefresh')  # time at next scr refresh
            # update status
            upButton.status = STARTED
            upButton.setAutoDraw(True)
        
        # if upButton is active this frame...
        if upButton.status == STARTED:
            # update params
            pass
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = core.getFromNames([upButton, submitButton, replay])
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *submitButton* updates
        
        # if submitButton is starting this frame...
        if submitButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            submitButton.frameNStart = frameN  # exact frame index
            submitButton.tStart = t  # local t and not account for scr refresh
            submitButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submitButton, 'tStartRefresh')  # time at next scr refresh
            # update status
            submitButton.status = STARTED
            submitButton.setAutoDraw(True)
        
        # if submitButton is active this frame...
        if submitButton.status == STARTED:
            # update params
            pass
        
        # *replay* updates
        
        # if replay is starting this frame...
        if replay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            replay.frameNStart = frameN  # exact frame index
            replay.tStart = t  # local t and not account for scr refresh
            replay.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(replay, 'tStartRefresh')  # time at next scr refresh
            # update status
            replay.status = STARTED
            replay.setAutoDraw(True)
        
        # if replay is active this frame...
        if replay.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in set_volumeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "set_volume" ---
    for thisComponent in set_volumeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from changeVol
    maxVol = 1
    minVol = 0
    stepSize = .1
    
    if mouse.clicked_name[0]=='upButton':
        if thisVol + stepSize >= maxVol:
            thisVol = maxVol
        else:
            thisVol += stepSize
    
    elif mouse.clicked_name[0]=='submitButton':
        print('psychopy volume set to ', thisVol)
        volume_check_loop.finished = True # end this loop
    
    thisExp.addData('thisVol', thisVol)
    sound_test.stop()  # ensure sound has stopped at end of routine
    # store data for volume_check_loop (TrialHandler)
    # the Routine "set_volume" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 100.0 repeats of 'volume_check_loop'


# --- Prepare to start Routine "instructions" ---
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionsComponents = [mouse_3, text]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse_3* updates
    
    # if mouse_3 is starting this frame...
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        # update status
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # end routine on response    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_loop = data.TrialHandler(nReps=expInfo['trial number'], method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('01_setup-code/trials_loop_conditionsfile_6cond.xlsx'),
    seed=None, name='trials_loop')
thisExp.addLoop(trials_loop)  # add the loop to the experiment
thisTrials_loop = trials_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
if thisTrials_loop != None:
    for paramName in thisTrials_loop:
        exec('{} = thisTrials_loop[paramName]'.format(paramName))

for thisTrials_loop in trials_loop:
    currentLoop = trials_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
    if thisTrials_loop != None:
        for paramName in thisTrials_loop:
            exec('{} = thisTrials_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from oddball
    print("trial number: ", trials_loop.thisN)
    
    oddball = oddballs.pop()
    print("is it an oddball ? ", oddball)
    
    if oddball is True:
        oddball_sound_file = sample(trials_loop.trialList, 1)[0]['sound_file']
        while oddball_sound_file == sound_file:
            oddball_sound_file = sample(trials_loop.trialList, 1)[0]['sound_file']
    else:
        oddball_sound_file = sound_file
    
    print("sound1: ", sound_file)
    print("sound2: ", oddball_sound_file)
    # Run 'Begin Routine' code from lsl
    # trigger managment
    trigger1 = str(sound_file)[11:13]
    print("trigger1: ", trigger1)
    
    trigger2 = str(oddball_sound_file)[11:13]
    print("trigger2: ", trigger2)
    sound1.setSound(sound_file, secs=1.0, hamming=False)
    sound1.setVolume(thisVol, log=False)
    sound2.setSound(oddball_sound_file, secs=1.0, hamming=False)
    sound2.setVolume(thisVol, log=False)
    slider.reset()
    # keep track of which components have finished
    trialComponents = [isi1, sound1, fix1, isi2, sound2, fix2, slider]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from lsl
        # trigger managment
        if sound1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            win.callOnFlip(outlet.push_sample, [int(trigger1)])
        
        # trigger managment
        if sound2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            win.callOnFlip(outlet.push_sample, [int(trigger2)])
        
        # *isi1* updates
        
        # if isi1 is starting this frame...
        if isi1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi1.frameNStart = frameN  # exact frame index
            isi1.tStart = t  # local t and not account for scr refresh
            isi1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi1, 'tStartRefresh')  # time at next scr refresh
            # update status
            isi1.status = STARTED
            isi1.setAutoDraw(True)
        
        # if isi1 is active this frame...
        if isi1.status == STARTED:
            # update params
            pass
        
        # if isi1 is stopping this frame...
        if isi1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                isi1.tStop = t  # not accounting for scr refresh
                isi1.frameNStop = frameN  # exact frame index
                # update status
                isi1.status = FINISHED
                isi1.setAutoDraw(False)
        # start/stop sound1
        
        # if sound1 is starting this frame...
        if sound1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            sound1.frameNStart = frameN  # exact frame index
            sound1.tStart = t  # local t and not account for scr refresh
            sound1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound1.started', tThisFlipGlobal)
            # update status
            sound1.status = STARTED
            sound1.play(when=win)  # sync with win flip
        
        # if sound1 is stopping this frame...
        if sound1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound1.tStop = t  # not accounting for scr refresh
                sound1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound1.stopped')
                # update status
                sound1.status = FINISHED
                sound1.stop()
        
        # *fix1* updates
        
        # if fix1 is starting this frame...
        if fix1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            fix1.frameNStart = frameN  # exact frame index
            fix1.tStart = t  # local t and not account for scr refresh
            fix1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix1.status = STARTED
            fix1.setAutoDraw(True)
        
        # if fix1 is active this frame...
        if fix1.status == STARTED:
            # update params
            pass
        
        # if fix1 is stopping this frame...
        if fix1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix1.tStop = t  # not accounting for scr refresh
                fix1.frameNStop = frameN  # exact frame index
                # update status
                fix1.status = FINISHED
                fix1.setAutoDraw(False)
        
        # *isi2* updates
        
        # if isi2 is starting this frame...
        if isi2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            isi2.frameNStart = frameN  # exact frame index
            isi2.tStart = t  # local t and not account for scr refresh
            isi2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi2, 'tStartRefresh')  # time at next scr refresh
            # update status
            isi2.status = STARTED
            isi2.setAutoDraw(True)
        
        # if isi2 is active this frame...
        if isi2.status == STARTED:
            # update params
            pass
        
        # if isi2 is stopping this frame...
        if isi2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                isi2.tStop = t  # not accounting for scr refresh
                isi2.frameNStop = frameN  # exact frame index
                # update status
                isi2.status = FINISHED
                isi2.setAutoDraw(False)
        # start/stop sound2
        
        # if sound2 is starting this frame...
        if sound2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            sound2.frameNStart = frameN  # exact frame index
            sound2.tStart = t  # local t and not account for scr refresh
            sound2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound2.started', tThisFlipGlobal)
            # update status
            sound2.status = STARTED
            sound2.play(when=win)  # sync with win flip
        
        # if sound2 is stopping this frame...
        if sound2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound2.tStop = t  # not accounting for scr refresh
                sound2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound2.stopped')
                # update status
                sound2.status = FINISHED
                sound2.stop()
        
        # *fix2* updates
        
        # if fix2 is starting this frame...
        if fix2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            fix2.frameNStart = frameN  # exact frame index
            fix2.tStart = t  # local t and not account for scr refresh
            fix2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix2.status = STARTED
            fix2.setAutoDraw(True)
        
        # if fix2 is active this frame...
        if fix2.status == STARTED:
            # update params
            pass
        
        # if fix2 is stopping this frame...
        if fix2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix2.tStop = t  # not accounting for scr refresh
                fix2.frameNStop = frameN  # exact frame index
                # update status
                fix2.status = FINISHED
                fix2.setAutoDraw(False)
        
        # *slider* updates
        
        # if slider is starting this frame...
        if slider.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider.started')
            # update status
            slider.status = STARTED
            slider.setAutoDraw(True)
        
        # if slider is active this frame...
        if slider.status == STARTED:
            # update params
            pass
        
        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from oddball
    thisExp.addData('sound1', sound_file)
    thisExp.addData('sound2', oddball_sound_file)
    thisExp.addData('is_oddball', oddball)
    sound1.stop()  # ensure sound has stopped at end of routine
    sound2.stop()  # ensure sound has stopped at end of routine
    trials_loop.addData('slider.response', slider.getRating())
    trials_loop.addData('slider.rt', slider.getRT())
    trials_loop.addData('slider.history', slider.getHistory())
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed expInfo['trial number'] repeats of 'trials_loop'

# get names of stimulus parameters
if trials_loop.trialList in ([], [None], None):
    params = []
else:
    params = trials_loop.trialList[0].keys()
# save data for this loop
trials_loop.saveAsExcel(filename + '.xlsx', sheetName='trials_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_loop.saveAsText(filename + 'trials_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "end" ---
continueRoutine = True
# update component parameters for each repeat
end_key_resp.keys = []
end_key_resp.rt = []
_end_key_resp_allKeys = []
# keep track of which components have finished
endComponents = [end_key_resp, end_text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_key_resp* updates
    
    # if end_key_resp is starting this frame...
    if end_key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key_resp.frameNStart = frameN  # exact frame index
        end_key_resp.tStart = t  # local t and not account for scr refresh
        end_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        end_key_resp.status = STARTED
        # keyboard checking is just starting
        end_key_resp.clock.reset()  # now t=0
    if end_key_resp.status == STARTED:
        theseKeys = end_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _end_key_resp_allKeys.extend(theseKeys)
        if len(_end_key_resp_allKeys):
            end_key_resp.keys = _end_key_resp_allKeys[-1].name  # just the last key pressed
            end_key_resp.rt = _end_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *end_text* updates
    
    # if end_text is starting this frame...
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        end_text.status = STARTED
        end_text.setAutoDraw(True)
    
    # if end_text is active this frame...
    if end_text.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
