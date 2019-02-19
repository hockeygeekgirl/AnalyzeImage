# This code will call the Computer Vision API to identify celebrities
# How to call the Computer Vision API https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/vision-api-how-to-topics/howtocallvisionapi

# To use Python in Visual Studio Code
# Follow instructions here https://code.visualstudio.com/docs/python/python-tutorial
# You will need to install the python extension for VS Code
# You will need to download and install python on the computer
# You will need to download and install pip in the project directory
# then you can install libraries and run your code

# Use the requests library to simplify calling the API
import requests

# Use the json library to encode and decode JSON
import json

# Replace the subscription key and vision_base_url with the values for your Computer Vision Service
subscription_key = "cf229a23c3054905b5a8ad512edfa9dd"
vision_base_url = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"

# Update the url to indicate you want to identify celebrities
analyze_url = vision_base_url + "models/celebrities/analyze"

#Computer Vision API will accept image as an application/octet stream or as a raw image binary
#File formats JPEG, PNG, GIF, BMP Under 4 MB greater than 50x50 pixels
# URL or path to locally stored image

# Example pointing to a file on the web
# image_url ="https://upload.wikimedia.org/wikipedia/commons/6/66/Don_Cherry_in_2010.jpg"
# headers = {'Ocp-Apim-Subscription-Key': subscription_key }
# params  = {'model': 'celebrities'}
# data    = {'url': image_url}
# response = requests.post(analyze_url, headers=headers, params=params, json=data)
# End Example of pointing to a file on the web

# Example pointing to a local file
#Recognized celebrity
image_path = "./TestImages/WayneGretzky.jpg"
# Unknown celebrity
# image_path = "./TestImages/BostonMarathonWinnerDesLinden.jpg"
image_data = open(image_path, "rb").read()
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}
params  = {'model': 'celebrities'}
response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
# End Example of pointing to a local file

response.raise_for_status()
analysis = response.json()

# Display raw JSON returned
print("Raw JSON")
print(json.dumps(response.json()))

# Display name of the celebrity
# If there is no recognizable celebrity length will be zero
if len(analysis["result"]["celebrities"])==0:
    print("\nCelebrity not recognized")
else:
    celebrity_name = analysis["result"]["celebrities"][0]["name"].capitalize()
    print("\nCelebrity: " + celebrity_name)
input()

# Sample JSON Output
# {"result": 
# {"celebrities": 
# [{"faceRectangle": 
# {"top": 82, "left": 194, "width": 196, "height": 196},
#  "name": "Wayne Gretzky", "confidence": 0.9984371066093445}]}, 
# "requestId": "da35de8a-b77c-4339-976c-1bdc7a56cf93", 
# "metadata": {"width": 696, "height": 458, "format": "Jpeg"}}