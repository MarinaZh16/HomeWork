import requests 
r = requests.get('https://api.github.com/events')
print(type(r))
print(r.__doc__)
#мы можем выполнять все стандартные запросы — PUT, DELETE, HEAD and OPTIONS:
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)

#Чтобы передать список объектов в виде значения добавляем квадратые скобки [] к ключу
payload = {'key1': 'value1', 'key2[]': ['value2', 'value3']}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)

#POST:
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'user-agent': 'rtfm/0.0.1'}
r = requests.post("http://httpbin.org/post", data=payload, headers=headers)
print(r.text)

#GitHub API v3 принимает POST/PATCH в формате JSON:
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print(r.text)

#POST для файлов составной кодировки:
url = 'http://httpbin.org/post'
files = {'file': open('form.html', 'rb')}
r = requests.post(url, files=files)
print(r.text)
