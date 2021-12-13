# Leer contenido online
import urllib3
http = urllib3.PoolManager()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
url = 'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt'

palabras = []
msg = http.request('GET', url, headers=headers)

contenido = msg.data.decode('utf-8').split()

print(contenido)

# for line in contenido:
#     print(line)


