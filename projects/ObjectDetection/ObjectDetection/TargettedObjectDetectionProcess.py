from label_image import main as labelImage
import cv2
import base64
import json
import numpy as np
import sys
sys.path.insert(0, '/home/bt-intern2/French-Flag-Finder/projects/DataTransfer/DataTransfer/')
from kafka_manager import *


graph = "/home/bt-intern2/TfModule/output_graph.pb"
labels = "/home/bt-intern2/TfModule/output_labels.txt"
input_layer = "Placeholder"
output_layer = "final_result"
input_height = 224   # Neccessary input_height for mobilnet model
input_width = 224    # Neccessary input_wifth for mobilenet model
fh = open("/home/bt-intern2/Pictures/testingB64decode.jpeg", "wb")   # used for writing decoded base64 image locally to then be tested against with label_image()


if __name__ == "__main__":
    json_data = Consumer.pull_jsons("framefeeder")
    json_data_parsed = json.loads(json_data)   # loads json data into a parsed string (back to dict)
    frameBase64 = json_data_parsed["imageBase64"]   # extracts base64 string of image (frame)
    frame = base64.b64decode(frameBase64)         # decodes base64 image
    fh.write(frame)        # writes decoded image to file in order to pass filepath to label_Image script
    fh.close()
    labelImage(graph, labels, input_layer, output_layer, input_height, input_width, "/home/bt-intern2/Pictures/testingB64decode.jpeg")    # tests frame for targeted object
