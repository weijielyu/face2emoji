# Face2emoji

![image](https://github.com/weijielyu/face2emoji/blob/main/img/result.png)

## About

**Contributors**

* Weijie Lyu
* Sirui Wang

The final project for course **CS-445 Computational Photography** at the **University of Illinois, Urbana-Campaign**.

In this project, we detected emotions of human faces and replaced the faces with corresponding emojis. For the faces whose orientations are not forward, we detected the orientations of the faces and applied transformations to emoji images. So that the orientations the emoji images can be the same as the faces.

## Usage

The images you want to process can be put in `img` folder. To run the experiment, simply run the `face2emoji.ipynb`

## Reference

We used [AffectNet dataset from Kaggle](https://www.kaggle.com/datasets/tom99763/affectnethq) to train our emotion classifier.

[1] https://github.com/timesler/facenet-pytorch

[2] Mollahosseini, Ali, Behzad Hasani, and Mohammad H. Mahoor. "Affectnet: A database for facial expression, valence, and arousal computing in the wild." IEEE Transactions on Affective Computing 10.1 (2017): 18-31.

[3] https://www.kaggle.com/datasets/tom99763/affectnethq

[4] https://pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/ 

[5] https://www.linuxtut.com/en/1e68a7572bc5736d474e/. 

