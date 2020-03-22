import requests
import json

class DoubanSpider:
    def __init__(self):
        self.temp_url="http://m.douban.com//rexxar/api/v2/subject?start={}&end=1000"
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36"}

    # 发送数据 
    def send_url(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    # 提取json数据
    def get_content_list(self,json_str):
        dict_ret = json.loads(json_str)
        content_list = dict_ret['subject_collection_items']
        total = dict_ret["total"]
        return content_list,total

    # 保存
    def save_content_list(self,content_list):
        # a:以追加的方式进行书写
        with open("douban.txt", "a") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n") #写入换行符，进行换行



    # 实现主要逻辑
    def run(self): 
        number = 0
        total = 100 #假设有第一页
        while num<total:
            # 1.start_url
            url = self.temp_url.format(number)
            # 2.发送请求，获取响应
            json_str = send_url(url)
            # 3.提取数据
            content_list,total = self.get_content_list(json_str)
            # 保存
            self.save_content_list(content_list)
            # 5.构造下一页的url地址，进入循环
            # 结束循环的方法之一
            # if len(content_list)<18:
            #     break;
            num += 18