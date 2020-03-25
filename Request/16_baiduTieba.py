import requests
from lxml import etree

class BdTieba:
    def __init__(self):
        self.start_url = "https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85&fr=search"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Cookie":"BIDUPSID=86EBF2BC758D6FC5C88F26715BB65BE6; PSTM=1583303829; TIEBAUID=360a690f4cd07a31981df5ce; bdshare_firstime=1583316403070; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1583393070,1583416725,1583509558,1583639368; BDUSS=1N1Tnh1YndtWUtsdHgteDVaeENQQ0hvZ204SXlwaUJ1N05FUWV4Vk9uMTlESlJlRVFBQUFBJCQAAAAAAAAAAAEAAAAS81BFyfHIpbLey~nHsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH1~bF59f2xea; STOKEN=63b022773503534868870232ec067f2a1e688b115e303400fc4cda35a833c7fa; TIEBA_USERTYPE=b202ce2256ebaaa626f7e6a2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=126CF6EE336C5169850B16068A45F41E:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; H_PS_PSSID=30971_1457_21091_30840_30909_30823_31086_22158; st_key_id=17; SEENKW=%E6%9D%8E%E6%AF%85; IS_NEW_USER=3bef09fa29ec6692d95dda4d; BAIDU_WISE_UID=wapp_1584946443622_858; USER_JUMP=-1; CLIENTWIDTH=107; CLIENTHEIGHT=400; H_WISE_SIDS=141911_140842_143133_142115_139090_143995_140593_140350_138426_143470_143337_143521_138595_139883_142912_140368_141102_110085; mo_originid=1; pb_prompt=1; wise_device=0; st_data=37b92627e4427d46300ecd2da1116346f5f953530f5c3e375039033e0029c76affe2489ee4cef9e3209443b9cb6f3b8c9ece3a0934e102be82b5a86ee5462981147200d906c7b91e7d136d6277f25bb0b1be246d73bf1e917ef802e8b9a33c9d541fd4507a7d6e5fa3d579c67d4af41e74db60147371645950ffe56322276eee; st_sign=55c641bb"
            }

    def send_url(self,url):
        html_content = requests.get(url,headers=self.headers)
        html = html_content.content.decode("utf-8")
        print(html)
        return html
        

    def get_first_list(self,html_str):
        html = etree.HTML(html_str)
        # print(etree.tostring(html).decode())
        li_list = html.xpath("//ul[@id='thread_list']/li[6]")
        # print(li_list)
        # for i in li_list:
        #     item = {}
        #     i.xpath("")

    

    # def save_page(self,html_content):
    #     with open("LiYi.html",'w',encoding="utf-8") as f:
    #         f.write(html_content)
    #     print("保存成功！")

    def run(self):
        # 准备起始url
        url = self.start_url
        # 发送请求，获取响应
        html_content = self.send_url(url)
        self.get_first_list(html_content)

        # 保存页面，查看是否能够准确获取页面数据
        # self.save_page(html_content)

if __name__ == "__main__":
    bdTieba = BdTieba()
    bdTieba.run()