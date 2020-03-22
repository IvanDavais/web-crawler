import requests

class M3u_Spider:
    def __init__(self, *args, **kwargs):
        # day and month
        self.start_url = "https://www.iptvm3ulist.com/english-free-iptv-m3u-list-files-{}-{}-2020/"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
            }
        cookies = "__cfduid=d9b08fd675f8680c6b96b5266b69ef87a1583327558; cookie_notice_accepted=true"
        self.cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}

    def send_url(self,url):
        html_str = requests.get(url,headers = self.headers,cookies=self.cookies)
        assert html_str.status_code
        return html_str.content.decode()
    
    def save(self,response_str):
        with open('m3u1.html','w',encoding='utf-8') as f:
            f.write(response_str)
            print("保存成功！")

    def run(self,num,month):
        # 构造起始url
        url = self.start_url.format(num,month)
        print(url)
        # 发送请求，获取响应
        response_str = self.send_url(url)
        
        # 保存数据
        self.save(response_str)

if __name__ == "__main__":
    m3u_spider = M3u_Spider()
    m3u_spider.run(19,"mar")
      
