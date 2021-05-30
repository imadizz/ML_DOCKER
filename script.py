

import joblib

model = joblib.load('salary_prediction_model.pkl')

data = float(input('Enter your Experience in years:'))

pred = model.predict([[data]])

print('$',pred[0][0])
