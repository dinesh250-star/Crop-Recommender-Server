from django.shortcuts import render
import os
import json
import pickle
import numpy as np
from scipy import stats
from . import data
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import *
from . serializer import *


# Loading all Crop Recommendation Models

crop_label_dict = pickle.load(
    open("model/label_dictionary.pkl", "rb")
)
crop_xg_boost = pickle.load(
    open("model/xgBoost.pkl", "rb")
)


def crop_prediction(input_data):
    prediction_data = []
    prediction_data.append((crop_label_dict[
            crop_xg_boost.predict(input_data)[0]
        ],max(crop_xg_boost.predict_proba(input_data)[0])
        * 100))
    print(crop_label_dict[
            crop_xg_boost.predict(input_data)[0]
        ])
    return prediction_data
    

#---------------------Crop Recommendation API---------------------

class CropApiEndPoint(APIView):
    
        serializer_class = CropRecommenderSerializer
        
        def post(self, request, format=None):
            serializer = CropRecommenderSerializer(data=request.data)
            if serializer.is_valid():
                print(serializer.data)
                form_values = serializer.data
                column_names = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
                input_data = np.asarray([float(form_values[i].strip()) for i in column_names]).reshape(
                    1, -1
                )
                print(input_data)
                print("hii")
                predictiondata = crop_prediction(input_data)
                resultdata = data.crop(predictiondata[0][0])
                return Response(resultdata)
