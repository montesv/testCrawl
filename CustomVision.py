import requests as requests
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import requests


class Endpoint_class:

    ENDPOINT = "https://usflogodetector-prediction.cognitiveservices.azure.com/"
    prediction_key = "139023d87b174213ab54f4c6db9ff98b"
    # prediction_resource_id = "/subscriptions/f294215e-1528-4d11-a41c-2c5eb70966a0/resourceGroups/USFCapstoneSpring2023/providers/Microsoft.CognitiveServices/accounts/usflogodetector"
    ProjectID = "2c5d2353-119b-4244-9dd8-754a81b4bae3"
    ModelName = "firstpythontest"

    def Azure_endpoint(self, imageurl,count):
        credentials = ApiKeyCredentials(in_headers={"Prediction-key": self.prediction_key})
        prediction_client = CustomVisionPredictionClient(endpoint=self.ENDPOINT, credentials=credentials)

        # image_file = 'testing/silvertest.JPG'
        print('Detecting objects in image')
        # image = Image.open(image_file)

        image_url = imageurl
        # with open(image_file, mode="rb") as image_data:
        # results = prediction_client.detect_image(ProjectID,ModelName,image_data)

        results = prediction_client.detect_image_url(self.ProjectID, self.ModelName, image_url)

        fig = plt.figure(figsize=(8, 8))
        plt.axis('off')

        color = 'magenta'


        imgout = "output"
        imgcount = count

        for prediction in results.predictions:
            fileout = imgout+ str(imgcount) + ".jpg"
            if (prediction.probability * 100) > 30:
                url_image = requests.get(image_url).content
                with open(fileout, 'wb') as handler:
                    handler.write(url_image)
                image_file = fileout
                image = Image.open(image_file)
                h, w, ch = np.array(image).shape
                lineWidth = int(w / 100)
                draw = ImageDraw.Draw(image)

                left = prediction.bounding_box.left * w
                top = prediction.bounding_box.top * h
                height = prediction.bounding_box.height * h
                width = prediction.bounding_box.width * w

                points = ((left, top), (left + width, top), (left + width, top + height), (left, top + height), (left, top))
                draw.line(points, fill=color, width=lineWidth)
                plt.annotate(prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100), xy=(left, top))
                plt.imshow(image)
                outputfile = fileout
                fig.savefig(outputfile)
                print('Results saved in ', outputfile)
                imgcount = imgcount+1