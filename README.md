This is alpha version of Voice-Recognition-in-Snake.
This work is based on article by Manash Kumar Mandal, 
link: https://blog.manash.me/building-a-dead-simple-word-recognition-engine-using-convnet-in-keras-25e72c19c12b

Current program features.
The "main.py" file consists of: wav to mfcc format converter (https://en.wikipedia.org/wiki/Mel-frequency_cepstrum), with additonal 
mfcc-matrix padding as CNN model requires all input data to have fixed shape. All files are loaded from "C:\vrAudio" directory, where I 
store sound files downloaded from "https://www.kaggle.com/c/tensorflow-speech-recognition-challenge/data". Among all files, I have chosen 
only those useful for controlling game. TO BE CONTINUED
