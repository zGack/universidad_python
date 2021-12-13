import urllib3
import json

http = urllib3.PoolManager()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
url = 'http://globalmentoring.com.mx/api/clima.json'

response = http.request('GET', url, headers=headers)

# Se procesa la respuesta
json_response = json.loads(response.data.decode('utf-8'))

principal = json_response['principal']

descripcion_clima = json_response['clima'][0].get('descripcion')
temp_min = principal['temp_min']
temp_max = principal['temp_max']

print(f'Descripcion del clima: {descripcion_clima}')
print(f'Temperatura minima: {temp_min}')
print(f'Temperatura maxima: {temp_max}')
