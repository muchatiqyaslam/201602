import requests

nama = raw_input('masukkan nama: ')
sandi = raw_input ('masukkan sandi: ')
url = 'http://127.0.0.1:5000/login/{}/{}'.format(nama, sandi)
print ('mboh mboh')

r = requests.get(url)
d = r.json()
print ('hdgfhgjh')