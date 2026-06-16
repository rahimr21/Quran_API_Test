import requests

BASE_URL = 'http://api.alquran.cloud/v1/'

surah = input('Enter Surah Number: ')
response = requests.get(BASE_URL + 'surah/' + surah)

print(response.json())