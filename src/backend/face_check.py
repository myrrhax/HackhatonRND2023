import face_recognition
import cv2
import numpy as np
import os 



# Load a sample picture and learn how to recognize it.
def Recognize(frame, photos):
    frame_np = np.fromstring(i, np.uint8)
    frame_photo = cv2.imdecode(frame_np, cv2.IMREAD_COLOR)
    for i in range(len(photos)):
        nparr = np.fromstring(photos[i], np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        #while True:
        #    cv2.imshow("f",standart_from_base)
        standart_encoding = face_recognition.face_encodings(img_np)[0]


        known_face_encodings = [
        standart_encoding,   
        ]

        known_face_names = [
            "Recognized",  
        ]


        face_locations = []
        face_encodings = []
        face_names = []

        face_locations = face_recognition.face_locations(frame_photo)
        if face_locations == []:
            return("photoisnull")
        face_encodings = face_recognition.face_encodings(frame_photo, face_locations)

        face_names = []
        for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        if name == "Recognized":
            recognized_users.append(list_of_standarts[i])
        if recognized_users != []:
            return recognized_users      
        
    return("isntinbase")
