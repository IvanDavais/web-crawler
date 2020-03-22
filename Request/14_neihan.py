import requests
import re
import json

class Neihan:
    def __init__(self, *args, **kwargs):
        self.temp_url = "http://www.budejie.com/{}"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

    def create_url(self):
        url_list = [self.temp_url.format(i+1) for i in range(10)]
        # print(url_list)
        return(url_list)

    def send_url(self,url):
        response = requests.get(url,headers= self.headers)
        return response.content.decode()
        

    def get_page_content(self,html_str):
        # print(html_str)
        # content_list = re.findall(r"<div class=\"j-item-des\">.*?<a href=\"/detail-.*?\">(.*?)</a>",html_str,re.S)
        content_list = re.findall(r"<div class=\"j-r-list-c\">.*?<div class=\"j-r-list-c-desc\">.*?<a href=\"/detail-.*?html\">(.*?)</a>",html_str,re.S)
        return content_list

    def save(self,content_list,page_num):
        file_name = "Neihan"+page_num+".txt"
        with open(file_name,'a') as f:
            for content in content_list:
                f.writelines(json.dumps(content,ensure_ascii=False))
                f.write("\n")
            # print("保存成功")

    def run(self):
        # 准备url list
        url_list = self.create_url()
        # 遍历url，发送请求
        for url in url_list:
            html_str = self.send_url(url)
            content_list = self.get_page_content(html_str)
            page_num = str(url_list.index(url)+1)
            self.save(content_list,page_num)

        # html_str = self.send_url(self.start_url,self.headers)
        # content_list = self.get_first_page_content(html_str)
        # self.save(content_list)


if __name__ == "__main__":
    neihan = Neihan()
    neihan.run()