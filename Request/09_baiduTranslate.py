import requests
import json
import sys

class BaiduTranslate:
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/v2transapi"
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

    # 发送post请求，获取响应
    def send_url(self,url,data):
        response = requests.post(url,data=data,headers=headers)
        return json.loads(response.content.decode())

    # 提取翻译的结果
    def get_ret(self,dict_response):
        ret = dict_response["trans_result"]["data"][0]["dst"]
        print("result is:", ret)

    # 实现主要逻辑结构
    def run():
        # 获取语言类型
            # 1.1 准备post的url地址，post_data
        lang_detect_data = {"query":self.trans_str}
            # 发送past请求，获取响应
        lang = self.send_url(self.lang_detect_data,lang_detect_data)["lan"]
            # 提取语言类型
            # return json.loads(response.content.decode()) 这一步就是提取语言数据

        # 准备post数据
        trans_data = {"query":self.trans_str,"from":"zh","to":"en"} if lang =="zh" else {"query":self.trans_str,"from":"en","to":"zh"}
        # 发送请求，获取响应
        dict_response = self.send_url(self.trans_url,trans_data)
        # 提取翻译的结果
        self.get_ret(dict_response)

if __name__ == "__main__":
    trans_str = sys.argv[1]
    baidu_translate = BaiduTranslate(trans_str)
    baidu_translate.run()