import subprocess
import os
import time
import python_speech_features
import scipy.io.wavfile as wav

class SLTK(object):

    def __init__(self, praat_path="Praat.exe"):

        self._praat = praat_path

    def readfile(self, wavfile):
        framerate, signal = wav.read(wavfile)
        return signal, framerate

    def _get_script(self, scriptname):
        _ROOT = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(_ROOT, "praatScripts", scriptname)

    def pitch(self, wavfile, pitch_time, time_step=0, pitch_floor=75, pitch_ceil=600):

        out_file = os.path.join(os.getcwd(), str(time.time())) + "out.txt"

        subprocess.run([self._praat, "--run", self._get_script("pitch.praat"),
                        " ".join([wavfile, str(time_step), str(pitch_floor),
                                  str(pitch_ceil), str(pitch_time), out_file])])
        
        pitch_val = open(out_file).readlines()[0].strip()
        os.remove(out_file)
        if (pitch_val == "--undefined--"):
            return -1

        return float(pitch_val)


    def pitch_interval(self, wavfile, time_step=0, pitch_floor=75, pitch_ceil=600, start_time=0, end_time=0):

        out_file = os.path.join(os.getcwd(), str(time.time())) + "out.txt"

        subprocess.run([self._praat, "--run", self._get_script("pitch_interval.praat"),
                        " ".join([wavfile, str(time_step), str(pitch_floor), str(pitch_ceil),
                                  str(start_time), str(end_time), out_file])])

        pitchvals = open(out_file).readlines()[0].strip().split(',')
        os.remove(out_file)

        return float(pitchvals[0]), float(pitchvals[1]), float(pitchvals[2]), float(pitchvals[3])

    def formant(self, wavfile, formant, formant_time, time_step=0, max_num_formants=5,
                max_formant=5500, window_length=0.025, pre_emphasis=50):

        out_file = os.path.join(os.getcwd(), str(time.time())) + "out.txt"

        subprocess.run([self._praat, "--run", self._get_script("formant.praat"),
                        " ".join([wavfile, str(time_step), str(max_num_formants), str(max_formant),
                                  str(window_length), str(pre_emphasis), str(formant),
                                  str(formant_time), out_file])])

        formant = open(out_file).readlines()[0].strip()
        os.remove(out_file)

        return float(formant)

    def all_formants(self, wavfile, formant_time):

        formants = []

        for f in range(1, 5):
            formants.append(self.formant(wavfile, f, formant_time))

        return formants[0], formants[1], formants[2], formants[3]

    def f1(self, wavfile, formant_time):
        return self.formant(wavfile, 1, formant_time)

    def f2(self, wavfile, formant_time):
        return self.formant(wavfile, 2, formant_time)

    def f3(self, wavfile, formant_time):
        return self.formant(wavfile, 3, formant_time)

    def f4(self, wavfile, formant_time):
        return self.formant(wavfile, 4, formant_time)

    def intensity(self, wavfile, intensity_time, min_freq=100, time_step=0, sub_mean="yes"):

        sub_mean_options = ["yes", "no"]
        assert sub_mean in sub_mean_options

        out_file = os.path.join(os.getcwd(), str(time.time())) + "out.txt"

        subprocess.run([self._praat, "--run", self._get_script("intensity.praat"),
                        " ".join([wavfile, str(intensity_time), str(min_freq),
                                  str(time_step), sub_mean, out_file])])

        intensity_val = open(out_file).readlines()[0].strip()
        os.remove(out_file)
        if (intensity_val == "--undefined--"):
            return -1

        return float(intensity_val)

    def harmonicity(self, wavfile, harmonicity_time, time_step=0.01, min_pitch=75, silence_threshold=0.1, ppw=1):


        out_file = os.path.join(os.getcwd(), str(time.time())) + "out.txt"

        subprocess.run([self._praat, "--run", self._get_script("harmonicity.praat"),
                        " ".join([wavfile, str(harmonicity_time), str(time_step),
                                  str(min_pitch), str(silence_threshold), str(ppw), out_file])])

        harmonicity_val = open(out_file).readlines()[0].strip()
        os.remove(out_file)
        if (harmonicity_val == "--undefined--"):
            return -1

        return float(harmonicity_val)


    def mfcc(self, wavfile, **kwargs):
        signal, framerate = self.readfile(wavfile)
        return python_speech_features.mfcc(signal, framerate, **kwargs)

    def deltas(self, mfcc, distance, **kwargs):
        return python_speech_features.delta(mfcc, distance, **kwargs)

    def fbank(self, wavfile, **kwargs):
        signal, framerate = self.readfile(wavfile)
        return python_speech_features.fbank(signal, framerate, **kwargs)

    def logfbank(self, wavfile, **kwargs):
        signal, framerate = self.readfile(wavfile)
        return python_speech_features.logfbank(signal,framerate, **kwargs)

