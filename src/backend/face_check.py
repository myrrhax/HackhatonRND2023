import face_recognition
import cv2
import numpy as np
import os
import PIL.Image as Image
import io

IMAGE_DIR = 'media/'

# Load a sample picture and learn how to recognize it.
'''def recognize(image, photos):
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
            
    
    return match_index '''

IMAGE_DIR = 'media/'

# Load a sample picture and learn how to recognize it.
def recognize(image, photos):
    image_1 = face_recognition.load_image_file(image)
    try:
        image_1_encodings = face_recognition.face_encodings(image_1)[0]
    except Exception as e:
        return 'NOFACES'
    match_index = None

    mathes_ids =[]
    distances = []
    for i in range(len(photos)):
        img_i = face_recognition.load_image_file(photos[i])
        img_i_encodings = face_recognition.face_encodings(img_i)[0]
        result = face_recognition.compare_faces([image_1_encodings], img_i_encodings, tolerance=0.5)
        if result[0]:
            match_index = i + 1
            mathes_ids.append(match_index)
            distances.append(face_recognition.face_distance([img_i_encodings], image_1_encodings)[0])

    for _ in range(len(mathes_ids)):
        for i in range(len(mathes_ids)-1):
            if distances[i]>distances[i+1]:
                a = distances[i]
                distances[i]=distances[i+1]
                distances[i+1] =a
                a = mathes_ids[i]
                mathes_ids[i]=mathes_ids[i+1]
                mathes_ids[i+1] =a
    try:
        return mathes_ids[0]
    except Exception:
        return None

def save_photo(file,path_to_photo):
   
    face_locations = face_recognition.face_locations(file)

    cv2.imwrite(path_to_photo,file[face_locations[0][0]:face_locations[0][2],face_locations[0][3]:face_locations[0][1]])