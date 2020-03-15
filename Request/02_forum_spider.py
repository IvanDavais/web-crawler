import requests


class ForumSpider:
    def __init__(self, forum_name):
        self.forum_name = forum_name
        # self.url_temp = "https://tieba.baidu.com/f?kw=‘+ forum_name +’&ie=utf-8&pn={}"
        # ==> Error-prone:此处注意拼接字符串时“”的使用

        # https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=50
        self.url_temp = "https://tieba.baidu.com/f?kw=" + \
            self.forum_name + "&ie=utf-8&pn=50"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

    # 构造url列表
    def get_url_list(self):
        # url_list = []
        # for i in range(100):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i*50) for i in range(1000)]

    # 发送请求，获取响应
    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # 保存html字符串
    def save_html(self, html_str, page_num):
        file_path = "{}--第{}页.html".format(self.forum_name, page_num)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(html_str)

    # 在run方法中实现主要逻辑
    def run(self):
        # 构造url列表
        url_list = self.get_url_list()
        # 遍历URL列表，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存
            page_num = url_list.index(url)+1  # 页码数
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    forum_spider = ForumSpider("lol")
    forum_spider.run()
