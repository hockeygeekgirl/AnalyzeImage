# [Computer Vision API](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/)
The [Computer Vision service](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/) analyzes the content of an image. For example, Computer Vision can identify landmarks and celebbrities, determine if an image contains adult or racy content, find all the faces in an image, get handwritten or printed text. This service works with popular image formats, such as JPEG and PNG. The code examples here are in Python but here are Quickstarts for [C#](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts-sdk/csharp-analyze-sdk), [Java](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/QuickStarts/java-analyze). [Node.js](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/QuickStarts/node-analyze), [Python](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/QuickStarts/python-analyze), [Go](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/QuickStarts/go-analyze)

In this repository you will find python examples for the following:
* Retrieve a text description of the image
* Identify landmarks
* Identify celebrities

Code examples are not provided in this repository but here are tutorials for other capabilities
* [Get text from an image](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts-sdk/python-sdk#get-text-from-image)
* [Generate thumbnail](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts-sdk/python-sdk#get-text-from-image)

# Retrieve a text description of the image

* **GetImageInfo.py** - This code example shows you how to analyze an image and return the tags describing the image as well as the caption text describing the image contents
* **TestImages.zip** - This file contains some images you can use as samples

Related resources
* [Analyze an image quickstart](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts-sdk/python-sdk#analyze-an-image)

# Identify landmarks
* **Landmark.py** - This code example shows you how to identify famous landmarks in an image
* **TestImages.zip** - This file contains some images you can use as samples

Related resources
* [Landmarks Python Quickstart](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts/python-domain#create-and-run-the-landmarks-sample)

# Identify celebrities
* **Celebrity.py** - This code example shows you how to identify famous landmarks in an image
* **TestImages.zip** - This file contains some images you can use as samples

Related resources
* [Celebrities Python Quickstart](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts/python-domain#create-and-run-the-celebrities-sample)

The Computer Vision API is a great tool but you may need to identify objects it is not trained to recognize. If the Computer Vision API does not meet your needs, you may need to train a new model using the [Custom Vision Service](https://github.com/hockeygeekgirl/CustomVisionServiceFun/tree/master/Custom%20Vision%20Service)