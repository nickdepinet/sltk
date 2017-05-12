
======================
Spoken Language Toolkit
======================

This library provides simple access to many common Praat speach feature information, and a wrapper around
the python_speech_features library from https://github.com/jameslyons/python_speech_features.

Installation
============

This `project is on pypi <https://pypi.python.org/pypi/sltk>`_

To install from pypi:: 

	pip install sltk

	
From this repository::

	git clone https://github.com/nickdepinet/sltk
	python setup.py develop


Usage
=====

Supported features:

- Pitch
- Intensity
- Formants
- Harmonicity

Features from python_speech_features

- Mel Frequency Cepstral Coefficients
- MFCC deltas
- Filterbank Energies
- Log Filterbank Energies


Initialization
==============

You need to initialize the SLTK object with the path of your Praat binary:

    python
    from sltk import SLTK
    sltk = SLTK("/path/to/praat")

If Praat is already in your path, you can leave this blank:

    python
    sltk = SLTK()

For these functions, I've provided the default parameters as Praat provides them,
so you can usually just run with the bare minimum required arguments and get what you want

Pitch Features
==============

You can easily get the pitch values over an interval of time.
The default start and end give the values for the whole file

    python
    min, mean, max, stdev = sltk.pitch_interval(wavfile, time_step=0, pitch_floor=75, pitch_ceil=600, start_time=0, end_time=0)

=============	===========
Parameter 		Description
=============	===========
wavfile         the wavfile to read from
time_step       the window size, default is a multiple of the pitch floor
pitch_floor     the lowest pitch to consider
pitch_ceil      the highest pitch to consider
start_time      the start of the analysis time (default is the whole file)
start_time      the end of the analysis time (default is the whole file)
returns         the minimum, mean, maximum, and standard deviation for pitch during the interval
=============	===========

If you want a pitch value at a specific time, that is easy to do as well.
This will return -1 if the pitch at the specified time is undefined.

    python
    pitch_val = sltk.pitch(wavfile, pitch_time, time_step=0, pitch_floor=75, pitch_ceil=600)

=============	===========
Parameter 		Description
=============	===========
wavfile         the wavfile to read from
pitch_time      the time to get the pitch at
time_step       the window size, default is a multiple of the pitch floor
pitch_floor     the lowest pitch to consider
pitch_ceil      the highest pitch to consider
returns         the pitch value at the specified time, or -1 if the pitch is undefined (the frame is unvoiced)
=============	===========

Formant Features
================

Most of the time, you just want a formant or formants at a specific time in the file.

    python
    f1 = sltk.f1(wavfile, formant_time)
    f2 = sltk.f2(wavfile, formant_time)
    f3 = sltk.f3(wavfile, formant_time)
    f4 = sltk.f4(wavfile, formant_time)
    f1, f2, f3, f4 = sltk.all_formants(wavfile, formant_time)

=============	===========
Parameter 		Description
=============	===========
wavfile         the wavfile to read from
formant_time    the time to get the formant at
returns         the formant at the specified time
=============	===========

In some cases, you want more detailed information than this. 
In these cases, you can use the function that all of those wrap:

    python
    formant_val = sltk.formant(wavfile, formant, formant_time, time_step=0, max_num_formants=5,
                               max_formant=5500, window_length=0.025, pre_emphasis=50))

=============	    ===========
Parameter 		    Description
=============	    ===========
wavfile             the wavfile to read from
formant             the formant number to get
formant_time        the time to get the formant at
time_step           used by Praat to calculate the window size
max_num_formants    the highest formant to find
max_formant         the highest Frequency to considered a formant at
window_length       the length of the windows for calculation
pre_emphasis        the pre_emphasis strength to apply before calculation 
returns             the formant at the specified time
=============	    ===========


MFCC Features
=============

The default parameters should work fairly well for most cases, 
if you want to change the MFCC parameters, the following parameters are supported::

	python
	mfcc_arr = sltk.mfcc(wavfile,winlen=0.025,winstep=0.01,numcep=13,
			 nfilt=26,nfft=512,lowfreq=0,highfreq=None,preemph=0.97,
             ceplifter=22,appendEnergy=True)

=============	===========
Parameter 		Description
=============	===========
wavfile			the wavfile to read from
winlen 			the length of the analysis window in seconds. Default is 0.025s (25 milliseconds)
winstep 		the step between successive windows in seconds. Default is 0.01s (10 milliseconds)
numcep			the number of cepstrum to return, default 13
nfilt			the number of filters in the filterbank, default 26.
nfft			the FFT size. Default is 512
lowfreq			lowest band edge of mel filters. In Hz, default is 0
highfreq		highest band edge of mel filters. In Hz, default is samplerate/2
preemph			apply preemphasis filter with preemph as coefficient. 0 is no filter. Default is 0.97
ceplifter		apply a lifter to final cepstral coefficients. 0 is no lifter. Default is 22
appendEnergy	if this is true, the zeroth cepstral coefficient is replaced with the log of the total frame energy.
returns			A numpy array of size (NUMFRAMES by numcep) containing features. Each row holds 1 feature vector.
=============	===========

MFCC Deltas
===========

Using the mfcc array returned by the above function, you can pretty easily get the deltas

    python
    deltas = sltk.deltas(mfcc_arr, distance)

=============	===========
Parameter 		Description
=============	===========
mfcc_arr        the mfcc numpy array
distance        the distance in either direction to compare
returns         A numpy array of the mfcc deltas
=============	===========


Filterbank Features
===================

These filters are raw filterbank energies. 
For most applications you will want the logarithm of these features.
The default parameters should work fairly well for most cases. 
If you want to change the fbank parameters, the following parameters are supported::

	python
	fbank_arr = sltk.fbank(wavfile,winlen=0.025,winstep=0.01,
              nfilt=26,nfft=512,lowfreq=0,highfreq=None,preemph=0.97)

=============	===========
Parameter 		Description
=============	===========
wavfile			the wavfile to read from
winlen			the length of the analysis window in seconds. Default is 0.025s (25 milliseconds)
winstep			the step between seccessive windows in seconds. Default is 0.01s (10 milliseconds)
nfilt			the number of filters in the filterbank, default 26.
nfft			the FFT size. Default is 512.
lowfreq			lowest band edge of mel filters. In Hz, default is 0
highfreq		highest band edge of mel filters. In Hz, default is samplerate/2
preemph			apply preemphasis filter with preemph as coefficient. 0 is no filter. Default is 0.97
returns			A numpy array of size (NUMFRAMES by nfilt) containing features. Each row holds 1 feature vector. The second return value is the energy in each frame (total energy, unwindowed)
=============	===========