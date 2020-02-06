import urllib.request

url = "https://www.python.org"
# url = "https://www.baidu.com"

print('First method')
response = urllib.request.urlopen(url)
print('status code: %s' % response.getcode())
print(len(response.read()))

print('Second method')
request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response = urllib.request.urlopen(request)
print("status code: ", response.status)
print(len(response.read()))
print(response.getheader('Server'))
