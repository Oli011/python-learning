# ## 作业
#
# 1. 基于csv格式实现 用户的注册 & 登录认证。详细需求如下：
#
# - 用户注册时，新注册用户要写入文件csv文件中，输入Q或q则退出。
# - 用户登录时，逐行读取csv文件中的用户信息并进行校验。
# - 提示：文件路径须使用os模块构造的绝对路径的方式。
#
# 2. 补充代码：实现去网上获取指定地区的天气信息，并写入到Excel中。
#
# ```python
# import requests
#
# while True:
#     city = input("请输入城市（Q/q退出）：")
#     if city.upper() == "Q":
#         break
#     url = "http://ws.webxml.com.cn//WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName={}".format(city)
#     res = requests.get(url=url)
#     print（res.text）
#
#     # 1.提取XML格式中的数据
#     # 2.为每个城市创建一个sheet，并将获取的xml格式中的数据写入到excel中。
#     ```
#
# 3. 读取ini文件内容，按照规则写入到Excel中。
#
# - ini文件内容如下：
#
# ```ini
# [mysqld]
# datadir=/var/lib/mysql
# socket=/var/lib/mysql/mysql.sock
# log-bin=py-mysql-bin
# character-set-server=utf8
# collation-server=utf8_general_ci
# log-error=/var/log/mysqld.log
# # Disabling symbolic-links is recommended to prevent assorted security risks
# symbolic-links=0
#
# [mysqld_safe]
# log-error=/var/log/mariadb/mariadb.log
# pid-file=/var/run/mariadb/mariadb.pid
#
# [client]
# default-character-set=utf8
# ```
#
# - 读取ini格式的文件，并创建一个excel文件，且为每个节点创建一个sheet，然后将节点下的键值写入到excel中，按照如下格式。
# <img src="assets/image-20201218204922898.png" alt="image-20201218204922898" style="zoom: 33%;" />
#
# - 首行，字体白色 & 单元格背景色蓝色。
# - 内容均居中。
# - 边框。
#
# 4. 补充代码，实现如下功能。
#
# ```python
# import requests
#
# # 1.下载文件
# file_url = 'https://files.cnblogs.com/files/wupeiqi/HtmlStore.zip'
# res = requests.get(url=file_url)
# print(res.content)
#
# # 2.将下载的文件保存到当前执行脚本同级目录下 /files/package/ 目录下（且文件名为HtmlStore.zip）
#
# # 3.在将下载下来的文件解压到 /files/html/ 目录下
# ```