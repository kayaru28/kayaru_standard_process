###############################################################
#
# version
#  1.0 2018/11/01
#
###############################################################

import numpy as np
import kayaru_standard_process as kstd
import os
import glob
import wave as Wave
from scipy import signal
import librosa

class DataWave():
    def __init__(self,file_path,n_mfcc=12):
        self.file_path = ""

        if kstd.checkPathExist(file_path) == kstd.NORMAL_CODE:
            self.file_path = file_path
            y,sr = librosa.audio.load(file_path)
            
            self.raw_data      = y
            self.sampling_rate = sr
            self.audio_frame   = len(self.raw_data)
            self.recorded_time = librosa.samples_to_time(self.audio_frame,self.sampling_rate)
            self.mfcc          = librosa.feature.mfcc(y,sr=sr,n_mfcc=n_mfcc)
            self.mfcc_length   = self.mfcc.shape[1]

    def isFileOpend(self):
        if self.file_path == "":
            return False
        return True

"""

class DataWave():
    def __init__(self,file_path):
        self.file_path = ""

        if kstd.checkPathExist(file_path) == kstd.NORMAL_CODE:
            self.file_path = file_path
            self.wave_raw  = Wave.open(file_path)
            data = self.wave_raw.readframes( self.getAudioFrame() )
            self.wave_np   = np.frombuffer(data,dtype = "int16")
            self.wave_np_normalized = self.wave_np / 32768.0
            y,sr = librosa.audio.load(file_path)
            self.wave_mspec = librosa.feature.mfcc(y,sr=sr,n_mfcc=12)

    def isFileOpend(self):
        if self.file_path == "":
            return False
        return True

    def getNumChannel(self):
        return self.wave_raw.getnchannels()

    def getSamplingSize(self):
        return self.wave_raw.getsampwidth()

    def getSamplingRate(self):
        return self.wave_raw.getframerate()

    def getAudioFrame(self):
        return self.wave_raw.getnframes()

    def getRecorededTime(self):
        recorded_time = ( self.getAudioFrame() / self.getSamplingRate() )
        return float(recorded_time)

    def getMFCC(self)


"""















