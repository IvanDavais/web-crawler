from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>  
        </ul> </div> '''
# 利用etree将字符串转化为element对象，且element对象具有xpath的方法
html = etree.HTML(text)
# print(html)

# 获取class为item-1 li下的a的herf
ret1 = html.xpath("//li[@class='item-1']/a/@href")

# 证明html.xpath("//li[@class='item-1']")的返回值是数组
# ret1 = html.xpath("//li[@class='item-1']")
# for i in ret1:
#     item = i.xpath('a/text()')
#     print(item)
    
# print(ret1)

# 获取class为item-1 li下的a的文本
ret2 = html.xpath("//li[@class='item-1']/a/text()")
print(ret2)

# 每个li是一条新闻，把url和文本组成字典 这种方法不太实用，因为有的时候li对应标题会为空
for href in ret1:
    item = {}
    item["href"] = href
    item["title"] = ret2[ret1.index(href)]
    print(item)

# 由于上面的方法有缺陷，所以采用下面这种方法
# 分组，根据li标签进行分组，对每一组继续写xpath
ret3 =  html.xpath("//li[@class = 'item-1']")# 注意返回值是一个数组里面存的是Element对象
print(ret3)

for i in ret3:
    item = {}
    # i.xpath("a/text()")的返回值是数组，可见17行代码
    item["title"] = i.xpath("a/text()")[0] if len(i.xpath("a/text()"))>0 else None
    item["href"] = i.xpath("a/@href")[0] if len(i.xpath("a/@href"))>0 else None
    print(item)


