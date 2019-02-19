# How to call the Computer Vision API https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/vision-api-how-to-topics/howtocallvisionapi

# To use Python in Visual Studio Code
# Follow instructions here https://code.visualstudio.com/docs/python/python-tutorial
# You will need to install the python extension for VS Code
# You will need to download and install python on the computer
# You will need to download and install pip in the project directory
# Then you can install libraries and run your code

# Import requests library to simplify calling API
import requests
# Import json library for encoding and decoding JSON
import json

subscription_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
vision_base_url = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"

analyze_url = vision_base_url + "models/landmarks/analyze"

#Computer Vision API will accept image as an application/octet stream or as a raw image binary
#File formats JPEG, PNG, GIF, BMP Under 4 MB greater than 50x50 pixels
# URL or path to locally stored image

# Example pointing to a file on the web
# image_url ="https://upload.wikimedia.org/wikipedia/commons/a/a0/Parliamenthill.jpg"
# headers = {'Ocp-Apim-Subscription-Key': subscription_key }
# params  = {'model': 'landmarks'}
# data    = {'url': image_url}
# print (data)
# input()
# response = requests.post(analyze_url, headers=headers, params=params, json=data)
# End Example of pointing to a file on the web

#Example pointing to a local file
image_path = "./TestImages/Parliament_Hill.jpg"
image_data = open(image_path, "rb").read()
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}
params  = {'model': 'landmarks'}
response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
#End Example of pointing to a local file

response.raise_for_status()
analysis = response.json()

# Raw JSON returned
print("Raw JSON file")
print(json.dumps(response.json()))

# What is the landmark
# If there is no recognized landmark then the length of the landmark tag will be zero

if len(analysis["result"]["landmarks"])==0:
    print("\nLandmark not recognized")
else:
    landmark_name = analysis["result"]["landmarks"][0]["name"].capitalize()
    print("\nLandmark: " + landmark_name)
input()

