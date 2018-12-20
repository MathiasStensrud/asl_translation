# Live ASL Translation With Flask
## The Project
As a continuation of my previous capstone, I created a Flask app to translate live video from ASL to text. Over 1 million people in North America know ASL as their primary language, and with the technology we have now, a project to ease the onus of translation off their shoulders is entierly possible. The goal was to translate the 26 leeters in the American Sign Language alphabet, as well as recognize when there is not a sign being made. This was accomplished through the use of a neural net that I trained. The model was a convolutional neural net trained on ~6,000 images that I created myself, using openCV and skImage.
## The Challenges
The model could very easily produce predictions for single images, which I took to another level using openCV's ability to read videos. Fome there I assumed it would be an easy leap to webcam translation, but that was not the truth. In fact, I ended up using Javascript and HTML to grab client webcams, rather than openCV as I had assumed. This took some time, with a great deal of work being put into continually grabbing the webcam, rather than a single frame. Once I had that, and got basic predictions, I managed to update live in screen with the current prediction, updated every 200 ms or if the image changed by a significant percentage.
## The app
Once I had the app running, it was smooth sailing. I hosted it on an AWS instance capable of handling rapid image analysis, and input the model I would use. I also set it up to host to https so that it could access client webcams. One very nice thing about my current setup, is that I can easily swap in another model without having to edit my code at all.
## The model and the data
The base model I used was a version of the InceptionV3 image classification neural net from keras. I beheaded it and froze all but a few layers, then trained my own image sets on the end of the model. One issue I had was that the model very rapidly became overfit, likely a result of my small and not terribly varied dataset. This is not a massive deal though, as the model can easily be swapped out for another, better optimized one at any point in time, and I plan on automating that section of the process.
## Results
I achieved what I wanted! I managed to connect a model that reads images from a client-side webcam and predicts a letter based on the image. The model is very easy to replace, and the server runs within a respectable timeframe.

## For the future
I would like to improve my model, as well as utilize client webcams and tests to build out my dataset for that end. Once I have a better model I would also like to setup a script that recognizes words and spaces, potentially along with a spell-check option. Once complete, this could be a truly helpful application, and I would love to see it put into production.


#### Previous Capstone
https://github.com/MathiasStensrud/capstone-2

#### References
http://inimino.org/~inimino/blog/javascript_live_text_input
https://webrtchacks.com/webrtc-cv-tensorflow/
