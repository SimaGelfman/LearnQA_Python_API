import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
print(f'Number of redirects is {len(response.history)} \nThe final URL is {response.url}')
