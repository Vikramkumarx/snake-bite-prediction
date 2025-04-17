# Texas-Snake-classifier-with-ResNet-18-CNN-machine-learning
Identify snakes using machine learning. Snakes have been framed as the devil throughout our culture and history. Studie suggests that the fear of snakes is hardwired as a part of our evolution. People can get scared over a harmless dekay brown snakes thinking it will bite and kill them. Many people kill rat snakes or harmless water snakes because they misclassify them as the deadly "water moccasin" snake.  Without snakes, the number of prey species would increase to unnatural levels and destroy the stability of the ecosystem. Similarly, if a large number of snakes are killed, the predators that eat snakes will struggle to find food. Snakes are thus an important component of the natural environment. 
# Special Thanks 
Thank you [Jawakar](https://medium.com/@jawakarselvavinayagam) - a data scientist from India for useful articles about fastai, flask and preprocessing data.

Thank you [Sameeha Rahman](https://www.kaggle.com/sameeharahman/preprocessed-snake-images) for the pre-processed snakes image dataset.

# Note:
I apologize in advance for all the typos in the demo. They will be fixed when I retrain the model. 
# Result
Training 6 types (about 5500 pictures) yields 87% accuracy
![Accuracy](https://github.com/Hanh-hub/Texas-Snake-classifier-with-ResNet-18-CNN-machine-learning/blob/main/accuracy%20log.PNG)
![Confustion matrix](https://github.com/Hanh-hub/Texas-Snake-classifier-with-ResNet-18-CNN-machine-learning/blob/main/confusion%20matrix.png)

As we trained more classes, there are more misclassifications between species, and the accuracy is thus reduced. 
Training 2000 pictures of rattlesnakes and harmless water snakes give 97% accuracy. 
![Accuracy when there are only two classes ](https://github.com/Hanh-hub/Texas-Snake-classifier-with-ResNet-18-CNN-machine-learning/blob/main/accuracy%20log%202%20classes.PNG)


![Testing results -black rat snake](https://github.com/Vikramkumarx/snake-bite-prediction/blob/main/Testing%20result%201.PNG)
![Testing result - dekay brown snake ](https://github.com/Hanh-hub/Texas-Snake-classifier-with-ResNet-18-CNN-machine-learning/blob/main/Testing%20result%202.PNG)
![Testing result - rattle snake ](https://github.com/Hanh-hub/Texas-Snake-classifier-with-ResNet-18-CNN-machine-learning/blob/main/Testing%20result%203.PNG)
![Testing result - cottonmouth ](https://github.com/Hanh-hub/Texas-Snake-classifier-with-ResNet-18-CNN-machine-learning/blob/main/Testing%20result%204.PNG)
