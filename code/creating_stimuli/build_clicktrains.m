% initialisation des variables
fmod = [10, 20, 30, 40, 70, 80, 90]; % in Hz
sr = 48000; % sampling rate (in Hz)
dur = 1   ; % duration of the sound (in s)
clickdur = 100; % duration of the click (in ms)
ramp_ms = 0; % ramp at onset only (in ms)

dC = clickdur*1e-6; % duration of the click
nSampC = round(sr*dC); % length of click in frames

directoryname = uigetdir(' ','Pick an output Directory');

figure;
% create stims ;
for fm = 1:length(fmod)
    
    % create sound for duration
    t = linspace(0,dur,sr*dur);
    st = zeros(size(t));
    
    % determine click onset place
    id = 1;
    while id+nSampC<length(st)
        st(1,id:id+nSampC-1) = ones(1,nSampC);
        id = id+round(1./fmod(fm)*sr);
    end
    
    wds = round(2*ramp_ms/1000 * sr);
    w=linspace(-1*(pi/2),1.5*pi,wds);
    w=(sin(w)+1)/2;
    st(1,1:round(wds/2))=st(1,1:round(wds/2)).*w(1:round(wds/2));
    
    st = [0.9*st',0.9*st'];
    
    subplot(length(fmod),1,fm); plot(1/sr:1/sr:size(st,1)/sr,st(:,1)')
    
    if fm<10; id = ['0' num2str(fm)]; else id = num2str(fm); end
    savename = [directoryname '/' num2str(fmod(fm)) 'Hz.wav'];
    audiowrite(savename,st,sr,'BitsPerSample',16)
end
%close all