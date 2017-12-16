import time
import urllib.request
import urllib.parse



url = 'https://pythonprogramming.net/'
values = {
    's':'basic',
    'submit':'search'
}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)





input(time.time())




