import requests

r = requests.head('https://en.wikipedia.org/wiki/Special:Random')
location = r.headers['location']
print(location)
payload = {'todo': 'READ {location}'.format(location=location)}
requests.post('http://backend-service-internal/todos', json=payload)