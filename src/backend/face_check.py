import face_recognition
import cv2
import numpy as np
import os
import PIL.Image as Image
import io

IMAGE_DIR = 'media/'

# Load a sample picture and learn how to recognize it.
def recognize(image, photos):
    image_1 = face_recognition.load_image_file(image)
    image_1_encodings = face_recognition.face_encodings(image_1)[0]
    match_index = None
    for i in range(len(photos)):
        if (match_index):
            break
        img_i = face_recognition.load_image_file(photos[i])
        img_i_encodings = face_recognition.face_encodings(img_i)[0]
        result = face_recognition.compare_faces([image_1_encodings], img_i_encodings, tolerance=0.5)
        if result[0]:
            match_index = i + 1
            
    
    return match_index