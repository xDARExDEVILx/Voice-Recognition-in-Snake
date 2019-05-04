SNAKE
-----

This is alpha version of Voice-Recognition-in-Snake.
This work is based on article by Manash Kumar Mandal, 
link: https://blog.manash.me/building-a-dead-simple-word-recognition-engine-using-convnet-in-keras-25e72c19c12b.

Current program features.

The "main.py" file consists of: wav to mfcc format converter (https://en.wikipedia.org/wiki/Mel-frequency_cepstrum), with additonal 
mfcc-matrix padding as CNN model requires all input data to have fixed shape. All files are loaded from "C:\vrAudio" directory, where I 
store sound files downloaded from "https://www.kaggle.com/c/tensorflow-speech-recognition-challenge/data". Among all files, I have chosen 
only those useful for controlling game (direction keys, boosting, slowing). Later, mfccs are saved into .npy files. Data is reshaped and trains model (layers same as in link given at the top), which is saved to json file (with weights) after succesful learning process. 

The "main_recognizer.py" is actually reconstructed Snake game from "snake.py" file with changed controlling, 2 new mechanics features (boosting, slowing) and lack of obstacles (on board). Mentioned change in gameplay controlling includes model loaded from "main.py"; thread in background is responsible for recording sound from microphone, then passes it to an array. The array is read by "translator" function which predicts the command and returns the word when prediction probability is higher than 95%. 

The "snake.py" is simple Snake implementation in pygame.

Future program features/updates.

- base language will be polish - requirement for project as english was for testing; also higher efficiency as polish words (only these used in program) will be probably less difficult to differentiate from each other.
- noise training - improvement of efficiency; in english version background noise happened to be recognized as "up" (popping effect)
- mfcc padding has to be changed to pad zeros at the beginning, not the end (already done in code, but model was learnt with 2nd option)
- possibly one more thread in background for increasing prediction power
- visual representation of recording period (as it lasts 1s)
- fixed translation for case when there are two equal predictions (now returns error)
- longer training period (>50 epochs) as there will be less learning data


