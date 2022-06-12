import csv
import re


#提取网页源文件内容
with open("venv/baidutieba/source.txt", mode='rt', encoding='utf-8') as f:
    content = f.read()

#提取发帖模块
post_list = re.findall('class="l_post l_post_bright j_l_post clearfix(.*?)class="j_lzl_container core_reply_wrapper', content, re.S)

#各个模块提取需求内容
result = []
for post in post_list:
    temp = {}
    temp['user'] = re.findall('username="(.*?)"', post, re.S)
    temp['reply_content'] = re.findall('"d_post_content j_d_post_content " style="display:;">            (.*?)<', post, re.S)
    temp['date'] = re.findall('tail-info">(2022.*?)<', post, re.S)
    temp['IP_addr'] = re.findall('tail-wrap"><span>IP属地:(.*?)<', post, re.S)
    result.append(temp)

#写入csv文件
with open('result.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['user', 'reply_content', 'date', 'IP_addr'])
    writer.writeheader()
    writer.writerows(result)

# IP：class="post-tail-wrap"><span>IP属地:河北</span><s
# 用户名："userName":"我叫李木木啊"
# 发帖内容：">            把别人废了跟别人比地位<img class=
# 发帖时间："tail-info">2022-06-10 17:56</span><div
# 模块头：class="l_post l_post_bright j_l_post clearfix  "
# 模块尾：class="j_lzl_container core_reply_wrapper"
