import requests

url = 'http://162.55.220.72:5005/terminal-hw-request'

response = requests.get(url)

print(response.status_code)
print(response.text)
