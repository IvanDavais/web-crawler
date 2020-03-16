import requests

proxies = {"http":"http://221.218.102.146:35110"}
headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36"}

r = requests.get("http://www.baidu.com",proxies=proxies,headers=headers)
print(r.status_code)