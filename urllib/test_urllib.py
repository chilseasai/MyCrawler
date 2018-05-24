import urllib.request

# url = "https://www.amazon.com/b?node=1"
url = "https://www.baidu.com"

print('First method')
response = urllib.request.urlopen(url)
print('status code: %s' % response.getcode())
print(len(response.read()))

print('Second method')
request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response = urllib.request.urlopen(request)
print("status code: ", response.getcode())
print(len(response.read()))