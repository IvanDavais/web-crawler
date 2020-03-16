import requests
""" 
目前此方法已不适用，仅当练习！
"""
# 实例化一个session对象
session = requests.session()

# post_url是指只有用户登录了之后才能访问的页面，例如人人网的profile页面 
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"mr_mao_hacker@163.com","password":"alarmchime"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

# 使用session发送post请求，旨在使服务器在浏览器上设置cookies
session.post(post_url,post_data,headers=headers)

# 携带已经被设置好的cookies发送get请求，获取页面信息
r = session.get("http://www.renren.com/327550029/profile",headers=headers)

# 保存
with open("renren1.html",w,encoding="utf-8") as f:
    f.write(r.content.decode)
