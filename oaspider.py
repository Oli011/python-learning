#校内oa公告爬取

import requests
from bs4 import BeautifulSoup as bs
import sendemail

#todo oa界面翻页
#todo 每次获取界面时间范围：每天or一段时间，然后接着上次查询的位置继续
#todo 发文单位的筛选
#todo 删除单一页面获取内容中的空行
# 解决方式：get.text(strip=True)增加一个参数获取网页的文本内容
#todo 标题与正文分开
# 解决方式：标题在表格页面获取，正文内容利用标题对应的连接读取里面的html内容
#todo bs如何读取元素内容
# 解决方式：get、select函数

#存储 a = []
#获取从通知列表界面获取通知链接
r = requests.get('http://oa.stu.edu.cn/csweb/list.jsp')
soup = bs(r.text, "html.parser")

#处理页面内容
def get_text(n):
    r2 = requests.get(n)
    soup2 = bs(r2.text, "html.parser")
    return soup2
#    return soup2.get_text(strip=True)
#从列表中提取通知页面链接
for link in soup.tbody.find_all('a'):#根据网页结构选取部分网页内容
    h = 'http://oa.stu.edu.cn' + link.get('href')
    subject = link.get('title')
    context = get_text(h)
    sendemail.send(subject, context)
