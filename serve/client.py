import requests
import json
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:8000/text_classification"
headers = {"Content-Type": "application/json"}

data = {"text": "这是什么鬼啊！！"}

response = requests.post(
    url=url,
    data=json.dumps(data),
    headers=headers,
    auth=HTTPBasicAuth("example_username", "example_password"),
)

print(response.json())
