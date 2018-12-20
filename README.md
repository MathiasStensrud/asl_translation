# Live ASL Translation With Flask
## The Project
As a continuation of my previous capstone, I created a Flask app to translate live video from ASL to text. The more focused goal was to translate the 26 ASL letters, as well as recognize when there is not a sign being made. This was accomplished through the use of a neural net that I trained. The model was a convolutional neural net trained on ~6,000 images that I created myself, using openCV and skImage. 
## The Challenges
The model could very easily produce predictions for single images, which I took to another level upsing openCV's ability to read videos. Frome there I assumed it would be an easy leap to webcam translation, but that was not the truth. In fact, I ended up using Javascript and HTML to grab client webcams, rather than openCV as I had assumed. This took some time, with a great deal of work being put into continually grabbing the webcam, rather than a single frame. Once I had that, and got basic predictions, I managed to update live in screen with the current prediction, updated every 200 ms or if the image changed by a significant percentage.
## The app
Once I had the app running, it was smooth sailing. I hosted it on an AWS instance capable of handling rapid image analysis, and input the model I woud use. I also set it up to host to https so that it could acsess client webcams.
## The model and the data
The base model I used was a version of the InceptionV3 image classification neural net from keras. I beheaded it and froze all but a few layers, then trained my own image sets on the end of the model. One issue I had was that the model very rapidly became overfit, likely a result of my small and not terribly varied dataset. 
## Results




#### Previous Capstone
https://github.com/MathiasStensrud/capstone_2

#### References
http://inimino.org/~inimino/blog/javascript_live_text_input
https://webrtchacks.com/webrtc-cv-tensorflow/
