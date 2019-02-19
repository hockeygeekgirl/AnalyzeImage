# This code will show you how to call the Computer Vision API from Python
#How to call the Computer Vision API https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/vision-api-how-to-topics/howtocallvisionapi

# This code was created using Visual Studio Code
# To use Python in Visual Studio Code
# Follow instructions here https://code.visualstudio.com/docs/python/python-tutorial
# You will need to install the python extension for VS Code
# You will need to download and install python on the computer
# You will need to download and install pip in the project directory
# then you can install libraries and run your code

# Use the requests library to simplify the API call from Python 
import requests
# Use the json library for encoding and decoding JSON
import json

# Replace the subscription key and vision_base_url with the values for your Computer vision service
subscription_key = "cf229a23c3054905b5a8ad512edfa9dd"
vision_base_url = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"

analyze_url = vision_base_url + "analyze"
#Computer Vision API will accept image as an application/octet stream or as a raw image binary
#File formats JPEG, PNG, GIF, BMP Under 4 MB greater than 50x50 pixels
# URL or path to locally stored image

# Example pointing to a file on the web
# image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + \
#    "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
# headers = {'Ocp-Apim-Subscription-Key': subscription_key }
# params  = {'visualFeatures': 'Categories,Description,Color'}
# data    = {'url': image_url}
# response = requests.post(analyze_url, headers=headers, params=params, json=data)
# End Example of pointing to a file on the web

# Example pointing to a local file
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}
params  = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
# End Example of pointing to a local file

# Raw JSON returned by Computer Vision API
response.raise_for_status()
analysis = response.json()
print("Here is the raw JSON returned")
print(json.dumps(response.json()))

# Photo description
image_caption = analysis["description"]["captions"][0]["text"].capitalize()
print("\nPhoto description: " + image_caption)

# Dominant color in the photo background
dominantColorBackground = analysis["color"]["dominantColorBackground"]
print("\nDominant background color: " + dominantColorBackground)

# All description tags returned
all_tags = analysis["description"]["tags"]
tag_list = ""
for item in all_tags:
    tag_list = tag_list + item + "; "
print("\nDescription tags: " + tag_list)
input()

# Sample JSON output
# {"categories": [
# 	{"name": "people_group", "score": 0.5390625, 
# 	"detail": {"celebrities": []}
# 	}]
# , "color": {"dominantColorForeground": "Grey",
# 	    "dominantColorBackground": "Grey", 
# 	    "dominantColors": ["Grey", "Black"], 
# 	    "accentColor": "A12A5E", 
# 	    "isBwImg": false, 
# 	    "isBWImg": false}
# , "description": {"tags": ["person", "outdoor", "holding", "man", "standing", "people", "group", "park", "posing", "woman", "red", "hat", "carrying", "older", "wearing", "smiling", "young", "large", "walking", "street", "old", "field", "kite", "frisbee"],
# 		 "captions": [{"text": "a group of people posing for the camera", 
# 				"confidence": 0.9755899758685875}]},
# 		 "requestId": "73355be4-ef81-4eaa-8eb2-c16969856e35",
# 		 "metadata": {"width": 1012, "height": 759, "format": "Jpeg"}}


