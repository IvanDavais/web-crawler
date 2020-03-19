""" 既可以发送post请求，又可以发送get请求 """
import requests
from retrying import retry 

headers = {"User_Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

@retry(stop_max_attempt_number=5)
def _send_url(url,method,data,proxies):
    print("*"*20)
    if method == "POST":
        response = requests.post(url,headers=headers,data=data,proxies=proxies)
    else:
        response = requests.get(url,headers = headers,proxies=proxies,timeout=3)
    # Error-prone
    # assert requests.status_codes == 200
    assert response.status_code == 200
    return response.content.decode()

def send_url(url,method="GET",data = None,proxies={}):
    try:
        html_str = _send_url(url,method,data,proxies)
    except Exception as result :
        html_str = result
        print(result)
    return html_str

if __name__ == "__main__":
    url = "http://www.baidu.com" 
    print(send_url(url))
