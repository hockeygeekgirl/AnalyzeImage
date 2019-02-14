# Custom Vision Service
The custom vision service allows you to easily customize computer vision models for your own use case. Upload your training images, tag them, and let Custom Vision Service train the models.

You need to:
1. Decide what images you want to classify
2. Build a classifer
3. Test your model
4. Improve your classifier
5. Use the trained model from your code

# 1. Decide what images you want to classify
This folder contains .zip files for three different use cases
* **Bears.zip** - hiking in Canada and meet a bear? What type of bear is dangerous?  Train a model to recognize if the bear you see is a black bear (not dangerous), grizzly bear (dangerous) or polar bear (dangerous)
* **Fire.zip** - Forest fires are on the rise in Canada, anaylze aerial images of forest to help us detect smoke and fire so we can detect and deal with forest fires quickly
* **PoutineNoPoutine.zip** - Help tourists in Canada figure out if that that snack is Poutine or Not Poutine

# 2. Build a classifier 
Follow the [tutorial](https://docs.microsoft.com/en-us/azure/cognitive-services/Custom-Vision-Service/getting-started-build-a-classifier) to 
* Create a new project
* Upload and tag images for your selected use case
* Train your model

## What project settings and tags should I use?
### Bears
Project Settings
* **Project Type** : Classification
* **Classification Types**: Multilabel
* **Domains** : General

 Tagging
 * Tag all images in the *PolarBearTrainingImages* folder with **Polar Bear** and **Dangerous**
 * Tag all images in the *BrownBearTrainingImages* folder with **Grizzly Bear** and **Dangerous**
 * Tag all images in the *BlackBearTrainingImages* folder with **Black Bear** and **Not as dangerous**

### Fire
Project Settings
* **Project Type** : Classification
* **Classification Types**: Multilabel
* **Domains** : General

 Tagging
 * Tag all images in the *FireAndSmokeTrainingImages* folder with **Fire** and **Smoke**
 * Tag all images in the *SmokeTrainingImages* folder with **Smoke** 
 * Tag all images in the *NoSmokeTrainingImages* folder with **Negative** to indicate that none of the other tags exist in these images

### Poutine
Project Settings
* **Project Type** : Classification
* **Classification Types**: Multiclass
* **Domains** : Food

 Tagging
 * Tag all images in the *PoutineTrainingImages* folder with **Poutine**
 * Tag all images in the *NotPoutineTrainingImages* folder with **Negative** to indicate that they do not have the Poutine tag 

# 3. Test your model
After you complete the steps in the tutorial for yrou images and train the model you are ready to test. Follow the [tutorial](https://docs.microsoft.com/en-us/azure/cognitive-services/Custom-Vision-Service/test-your-model) to test your model

Test your model with an image from the *TestImages* folder

# 4. Improve your classifier
What happens if you upload a panda bear to the Bears model? What happens if you upload a picture with a lot of houses or a lake to the fire model? Did you try testing the chicken wings picture on the Poutine model? It incorrectly identifies the chicken wings as Poutine

Your model will **only** recognize the tags and images you train. The quality of your trained model depends on the amount of images, the quality of images, and the variety of labels you provide. For mroe ifnormation check out the article [How to improve your classifier](https://docs.microsoft.com/en-us/azure/cognitive-services/Custom-Vision-Service/getting-started-improving-your-classifier)

Try adding additional images to improve your model. If you are using the PoutineNoPoutine images try adding the WingsAreNotPoutineTrainingImages adn tagging them as **negative** retrain the model and see if results improve for the chieckn wings picture in the *TestImages* folder

# 5. Use the trained model from your code
The file *MakePrediction.py* is a Python program which shows you how to call a trained model from your code. It does not matter whether you trained the model using the web site or programmatically. 

The file *ClassifyImages.py* is a Python program which creates a Custom Vision Service Project, uploads and tags images, and trains a model. 

Here are the Quickstart tutorials for
* [C#](https://docs.microsoft.com/en-us/azure/cognitive-services/Custom-Vision-Service/csharp-tutorial)
* [Python](https://docs.microsoft.com/en-us/azure/cognitive-services/Custom-Vision-Service/python-tutorial)
* [Java](https://docs.microsoft.com/en-us/azure/cognitive-services/Custom-Vision-Service/java-tutorial)




