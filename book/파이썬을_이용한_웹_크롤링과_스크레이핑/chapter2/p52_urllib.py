from urllib.request import urlopen
f = urlopen('https://hanbit.co.kr')

print(type(f))

print(f.read().decode('utf-8'))

print(f.status)

print(f.getheader('Content-Type'))