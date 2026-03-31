import requests
import json

API_KEY = "AIzaSyBn3N2gLGE1_PzB8imTu8K6TDroGEGua6Q"
CHANNEL_HANDLE = "MrBeast"

url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle=MrBeast&key=AIzaSyBn3N2gLGE1_PzB8imTu8K6TDroGEGua6Q"
response = requests.get(url)

print(response)

data = response.json()

print (json.dumps(data, indent = 4))