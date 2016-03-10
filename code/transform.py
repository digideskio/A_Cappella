import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import StringIO
from time import sleep
from train import single_file_featurization


def transform(wav_queue, fingerprint_queue):

    # while True:
    #     if not wav_queue.empty():
    #         fs, data = wavfile.read(wav_queue.get()) # load the data
    #         a = data.T[0] # this is a two channel soundtrack, I get the first track
    #         b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    #         c = fft(b) # calculate fourier transform (complex numbers list)
    #         d = len(c)/2  # you only need half of the fft list (real signal symmetry)
    #         '''TODO: USE STRINGIO'''
    #         # fingerprint_buffer = StringIO.StringIO(buffer)
    #         # fingerprint = open(fingerprint_buffer, 'wb')
    #         # fingerprint.write(abs(c[:(d-1)]))
    #         # fingerprint.close()
    #         fingerprint_queue.put(abs(c[:(d-1)]))
    #     else:
    #         print "Tranform Worker Waiting...\n"
    #         sleep(1)
    while True:
        if not wav_queue.empty():
            fingerprint_queue.put(single_file_featurization(wav_queue.get()))
        else:
            print "Tranform Worker Waiting...\n"
            sleep(1)
