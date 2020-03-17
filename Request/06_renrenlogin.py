import requests
""" 复习 """
session = requests.session()

post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"mr_mao_hacker@163.com","password":"alarmchime"}
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

session.post(post_url,post_data,headers=headers)

r = session.get("http://www.renren.com/327550029/profile",headres=headers)

with open("renren.html",w,encoding="utf-8") as f:
    f.write(r.content.decode())