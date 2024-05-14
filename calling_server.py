import requests

# Calling flask server and providing input to model for prediction
r = requests.post('http://127.0.0.1:5000/get_predictions', json={'SepalLengthCm': 5.1, 'SepalWidthCm': 3.5, 'PetalLengthCm': 1.4, 'PetalWidthCm': 0.2})
r.status_code
r.text   # Gives prediction output

# If prediction output is 0 -> 'Iris-setosa'
# If prediction output is 1 -> 'Iris-versicolor'
# If prediction output is 2 -> 'Iris-virginica'