# Leer archivo json
# JSON = JavaScript Object Notation
import urllib3
import json

http = urllib3.PoolManager()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
url = 'http://globalmentoring.com.mx/api/personas.json'

respuesta = http.request('GET', url, headers=headers)
print(respuesta)

cuerpo_respuesta = respuesta.data
print(cuerpo_respuesta)

# Se procesa la respuesta
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)

# Imprimir solo los nombres de las personas
# JSON se convierte a listas y diccionarios
for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]} {persona["edad"]}')

# Se accede a las variables independientes
print(f'Total de persona: {json_respuesta["total"]}')
print(f'Mensaje: {json_respuesta["mensaje"]}')