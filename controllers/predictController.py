from flask_restful import Resource
import sys
import pickle
import sklearn
from flask import request


classifier = pickle.load(open('./dtree.sav', 'rb'))



class PredictController(Resource):

    def get(self):
        return {"response" : "hello get"}

    def post(self):
      formData = request.json
      data = [float(val) for val in formData.values()]
      print("predicting ...")
      print('data: ', data)
      prediction = classifier.predict(np.array(data).reshape(1, -1))
      print("predicted")
      print("prediction ", prediction)
      types = { 0: "A2", 1:'B1', 2:'B2', 3:'C1' }
      response = jsonify({
        "statusCode": 200,
        "status": "Prediction made",
        "result": "The language level is: " + types[prediction[0]]
        })
      response.headers.add('Access-Control-Allow-Origin', '*')
      return {"response": response}


    def put(self):
        return {"response" : "hello put"}

    def delete(self):
        return {"response" : "hello delete"}


