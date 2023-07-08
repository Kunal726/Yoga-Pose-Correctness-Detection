import mediapipe as mp 
import cv2 
import pandas as pd
import numpy as np
import pickle
import imutils
from subprocess import call

mp_drawing = mp.solutions.drawing_utils # Drawing helpers
mp_holistic = mp.solutions.holistic # Mediapipe Solutions

with open('pose_model_sitting.pkl', 'rb') as f:
    model = pickle.load(f)
print(model)

cap = cv2.VideoCapture(0)
height=1080 
width=1920
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False        
        
        # Make Detections
        results = holistic.process(image)
        # print(results.face_landmarks)
        
        # face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks
        
        # Recolor image back to BGR for rendering
        image.flags.writeable = True   
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # 1. Draw face landmarks
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS, 
                                 mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                 mp_drawing.DrawingSpec(color=(55,189,55), thickness=1, circle_radius=1)
                                 )
        
        # 2. Right hand
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(55,189,55), thickness=2, circle_radius=2)
                                 )
        # 3. Left Hand
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(55,189,55), thickness=2, circle_radius=2)
                                )

        # 4. Pose Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                 mp_drawing.DrawingSpec(color=(55,189,55), thickness=2, circle_radius=2)
                                 )
        # Export coordinates
        try:
            # Extract Pose landmarks
            pose = results.pose_landmarks.landmark
            pose_row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())
            
            
            # Concate rows
            row = pose_row
            
#          
            # Make Detections
            X = pd.DataFrame([row])
            body_language_class = model.predict(X)[0]
            body_language_prob = model.predict_proba(X)[0]
            #print(body_language_class, body_language_prob)

            # Grab ear coordinates
            coords = tuple(np.multiply(
                            np.array(
                                (results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EAR].x, 
                                 results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EAR].y))
                        , [640,480]).astype(int))
            
            cv2.rectangle(image, 
                          (coords[0], coords[1]+5), 
                          (coords[0]+len(body_language_class)*20, coords[1]-30), 
                          (0, 0, 0), -1)
            cv2.putText(image, body_language_class, coords, 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (84, 209, 1), 2, cv2.LINE_AA)
            
            # Get status box
            cv2.rectangle(image, (0,5), (600, 120), (0, 0, 0), -1)
            
            # Display Class
            cv2.putText(image, 'Yoga Pose :- '
                        , (15,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (84, 209, 1), 2, cv2.LINE_AA)
            cv2.putText(image, body_language_class.split(' ')[0]
                        , (250,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (84, 209, 1), 2, cv2.LINE_AA)
            
            # Display Probability
            cv2.putText(image, 'Probability :- '
                        , (15,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (32, 32, 247), 2, cv2.LINE_AA)
            cv2.putText(image, str(round(body_language_prob[np.argmax(body_language_prob)],2))
                        , (250,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (32, 32, 247), 2, cv2.LINE_AA)
            
        except:
            pass
                        
        cv2.imshow('Pose Detection', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            call(["python","pose_selection.py"])
            cv2.destroyAllWindows()
            break