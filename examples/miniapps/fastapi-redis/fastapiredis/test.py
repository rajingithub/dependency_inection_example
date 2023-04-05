import sys
from urllib import request
url = 'http://127.0.0.1:8086/name?name=' + sys.argv[1]

# print(url)

while True:
  response = request.urlopen(url)
  content = response.read()

  print(content)
