from flask import Flask, request, jsonify, send_from_directory
import pickle
import numpy as np

app = Flask(__name__)

# Carga el modelo
with open('model/RandomForest.pkl', 'rb') as f:
    modelo = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    newData = [i[1] for i in data.items()]
    for i,j in enumerate(newData):
        if j == True:
            newData[i]= 1
        elif j == False:
            newData[i]= 0
    print(newData)
    prediccion = modelo.predict(np.array(newData).reshape(1, -1))
    #prediccion = modelo.predict(np.array([[6.4, 3.1, 5.5]]))
    #array([[6.4, 3.1, 5.5]])
    output = prediccion[0]
    output = int(output)
    return jsonify({'prediction': output})

@app.route('/')
def serve_prediction_page():
    return send_from_directory('static', 'prediction.html')

if __name__ == '__main__':
    app.run(debug=True)
