import json

file_name = "./douban.json"
with open ("./douban.json","r",encoding="utf-8") as f:
    # json.load 将json字符串转化为python字典
    ret = json.load(f)
    # font_family = ret[0]["fontFamily"]

print(ret)
print(type(ret))
# print(font_family)

# json.dumps能够把python类型转化为json字符串
with open("douban1.json","w",encoding="utf-8") as f:
    # 这样写会报错，TypeError: write() argument must be str, not dict
    # f.write(ret)    

    # indent 首行缩进两个空格，格式化代码，ensure_ascii=False可以让其不进行ascii进行
    f.write(json.dumps(ret,ensure_ascii=False,indent=2))

# 使用json.load提取类文件中的数据

# json.dump 能够将python类型（字典）放入类文件对象（json文件中）
with open("douban2.json",'w',encoding="utf-8") as f:
    json.dump(ret,f,ensure_ascii=False,indent=2)
