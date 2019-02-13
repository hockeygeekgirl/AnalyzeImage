# You can train a Custom Vision Service model using the GUI at http://customvision.ai 
# OR you can train a Custom Vision Service model programmatically 
# The code in this program will train the model programmatically
# This code was written referencing the code samples here
#  Python SDK Samples https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/tree/master/samples
#
# If you wish to use the GUI for training instead check out the tutorial here
# https://docs.microsoft.com/en-us/azure/cognitive-services/Custom-Vision-Service/getting-started-build-a-classifier
#  
# Use the code in MakePrediction.py to call the trained model 
#
# Pre-requisites
# Install Custom Vision Service SDK
# pip install azure-cognitiveservices-vision-customvision
#
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import time
import os

# You will need to sign in to CustomVision.ai with your account
# Go to settings (the gear in the top right corner)
# replace the ENDPOINT, training_endpoint, prediction_endpoint, training_key, and prediciton_key
# with the values from your custom vision service settings
#
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
# training_endpoint = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.2/Training/"
# prediction_endpoint = "https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction/"

# Replace with a valid key
training_key = "6ea9a9db31724efd90b9bfe886ea108f"
# prediction_key = "4708b2d271e04f8a8e5453839f4e4921"

trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)

# Create a new project
print("Creating project...")
project = trainer.create_project("ElephantNoElephant")
print("Project created")
print("Creating tags")

# Make two tags in the new project
elephant_tag = trainer.create_tag(project.id, "Elephant")
giraffe_tag = trainer.create_tag(project.id, "Giraffe")

print("Adding images...")
# Add all images in elephants folder as images tagged elephant
IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
elephant_dir = os.path.join(IMAGES_FOLDER, "Elephant")
for image in os.listdir(elephant_dir):
    with open(os.path.join(elephant_dir, image), mode="rb") as img_data:
        trainer.create_images_from_data(project.id, img_data.read(), [elephant_tag.id ])
print("added elephants")

# Add all images in giraffe folder as images tagged giraffe
IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
giraffe_dir = os.path.join(IMAGES_FOLDER, "Giraffe")
for image in os.listdir(giraffe_dir):
    with open(os.path.join(giraffe_dir, image), mode="rb") as img_data:
        trainer.create_images_from_data(project.id, img_data.read(), [giraffe_tag.id ])
print("added giraffes")

print("Training...")

iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print("Training status: " + iteration.status)
    time.sleep(1)

# The iteration is now trained. Make it the default project endpoint
trainer.update_iteration(project.id, iteration.id, is_default=True)
print("Done!")
input()

# Now there is a trained endpoint that can be used to make a prediction

# print("Make prediction")
# IMAGES_FOLDER = os.path.dirname(os.path.realpath(__file__))
# predictor = CustomVisionPredictionClient(prediction_key, endpoint=prediction_endpoint)
# try:
#     with open(os.path.join(IMAGES_FOLDER, "TestImages", "testelephant2.jpg"), mode="rb") as test_data:
#         results = predictor.predict_image(project.id, test_data.read())
# except Exception as e:
#     print(str(e))
#     input()
# # Display the results.
# for prediction in results.predictions:
#     print(prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
#     input()
# predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)
# base_image_url = "C:/Users/sibach/Documents/AIFun/CustomVisionService/images/TestImages/"
# test_img_url = base_image_url + "testelephant2.jpg"
# results = predictor.predict_image_url(project.id, iteration.id, url=test_img_url)

# # Display the results.
# for prediction in results.predictions:
#     print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
#     input()