import urllib.request

# url = "http://www.baidu.com"
url = "https://www.amazon.com/b?node=1"
print('第一种方法')
response = urllib.request.urlopen(url)
print(response.read())