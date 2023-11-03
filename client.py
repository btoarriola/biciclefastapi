import requests
body = {
  "Date": 1122017,
  "Hour": 0,
  "Temperature": -5.2,
  "Humidity": 37,
  "Wind_Speed": 2.2,
  "Visibility": 2000,
  "Dew_Point": -17.6,
  "Solar_Radiation": 0,
  "Rainfall": 0,
  "Snowfall": 0,
  "Season": 1,
  "IsHoliday": 0,
  "IsFunctioningDay": 1
}
response = requests.post(url = 'http://127.0.0.1:8000/rented',
              json = body)
print (response.json())
# output: {'score': 0.866490130600765}
