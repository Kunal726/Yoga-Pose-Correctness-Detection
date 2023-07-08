import mediapipe as mp 
import cv2 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline 
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score # Accuracy metrics
from sklearn.metrics import classification_report # Accuracy metrics

import pickle


mp_drawing = mp.solutions.drawing_utils # Drawing helpers
mp_holistic = mp.solutions.holistic

df = pd.read_csv('standing.csv')

X = df.drop('class', axis=1) # features
y = df['class'] # target value

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

""" Block to create Classification Model with multiple pipelines using 
    LogisticRegression, RidgeRegression, RandomForestClassifier and GradientBoostingClassifier
"""
pipelines = {
    'lr':make_pipeline(
        StandardScaler(),
        LogisticRegression(random_state=42,multi_class='multinomial', solver='saga')
        ),
    'rc':make_pipeline(
        StandardScaler(), 
        RidgeClassifier(alpha=10)
        ),
    'rf':make_pipeline(
        StandardScaler(), 
        RandomForestClassifier()
        ),
    'gb':make_pipeline(
        StandardScaler(), 
        GradientBoostingClassifier()
        ),
}

""" Creating a dictionary to store the Classification Algorithms and their Corresponding 
    models which are computed using .fit() method.
"""
fit_models = {}
for algo, pipeline in pipelines.items():
    model = pipeline.fit(X_train, y_train)
    fit_models[algo] = model
print(fit_models)


""" Running a for loop to iterate in the 'fit_models' dictionary to predict the result 
    using the X_test values and return the classification report for each model.
"""    
for algo,model in fit_models.items():
    y_pred = model.predict(X_test)
    print("Accuracy of",algo,accuracy_score(y_test, y_pred))
    #print(classification_report(y_test,y_pred)) 


""" Create an pickle file of the model that we want to use further.
    This helps in using our model for any other similar applications and can easily 
    integrated in our app as well as other apps.
"""
# with open('pose_model_standing.pkl', 'wb') as f:
#     pickle.dump(fit_models['lr'], f)
    
