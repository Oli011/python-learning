### 练习题

# 1. 补充代码：实现下载视频并保存到本地
#
# # ```python
# import requests
#
# res = requests.get(
#     url="http://live.video.weibocdn.com/547d4a88-6d8c-41e5-b129-6735a505637a_index.m3u8?ori=0&ps=1CwnkDw1GXwCQx&Expires=1653715423&ssig=44pk5ClD16&KID=unistore,video",
#     headers={
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
#     }
# )
#
# # 视频的文件内容
# with open('talk.mp4',mode='wb') as file_object:
#     file_object.write(res.content)

#
# 2. 日志分析，计算某用户`223.73.89.192`访问次数。日志文件如下：`access.log`
#
#

# ```
# f = open("access.log", mode='r', encoding='utf-8')
# i = 0
# for line in f:
#     if line.startswith("223.73.89.192"):
#         i += 1
# print(f"用户`223.73.89.192`访问了{i}次")

# ```
#
# 3. 日志分析升级，计算所有用户的访问次数。
# f = open("access.log", mode='r', encoding='utf-8')
# i = 0
# user_list = []
# log = {}
# #找出所有用户
# for line in f:
#     user_list.append(line.split(" - - ")[0])
# for key in user_list:
#     log[key] = log.get(key, 0) + 1
# print(log)

#user_dict = {}
# with open("access.log", mode='r', encoding='utf-8') as file_object:
#     for line in file_object:
#         user_ip = line.split(" ")[0]
#         if user_ip in user_dict:
#             user_dict[user_ip] += 1
#         else:
#             user_dict[user_ip] = 1
# print(user_dict)
# 4. 筛选出股票 当前价大于 20 的所有股票数据。
#
# # ```
# with open("money.txt", mode='r', encoding='utf-8') as f, open("log1,txt", mode='w', encoding='utf-8') as f1:
#
#     title = f.readline().split(",")
#
#     stock_list = f.readlines()[1:]
#
#     all_list = []
#
#     for stock in stock_list:
#         stock = stock.split(",")
#         #print(stock)
#         item = {}
#         for num in range(len(title)):
#             item[title[num]] = stock[num]
#             if num == len(title) - 1:
#                 all_list.append(item)
#
#     for info in all_list:
#         if float(info.get("当前价")) > 20:
#             print(info)
# with open("money.txt", mode='r', encoding='utf-8') as file_object:
#     file_object.readline()
#     for line in file_object:
#         price = line.strip().split(",")[2]
#         if float(price) > 20:
#             print(line)



# 5. 根据要求修改文件的内容，原文件内容如下：`ha.conf`
#
# ```
# global
# log 127.0.0.1 local2
# daemon
# maxconn 256
# log 127.0.0.1 local2 info
# defaults
# log global
# mode http
# timeout connect 5000ms
# timeout client 50000ms
# timeout server 50000ms
# option  dontlognull
#
# listen stats :8888
# stats enable
# stats uri       /admin
# stats auth      admin:1234
#
# frontend oldboy.org
# bind 0.0.0.0:80
# option httplog
# option httpclose
# option  forwardfor
# log global
# acl www hdr_reg(host) -i www.luffycity.org
# use_backend www.luffycity.com if www
#
# backend www.luffycity.com
# server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000
# ...
# ```
#
# 请将文件中的 `luffycity`修改为 `pythonav` 。
#
# #创建一个新文件，每行读取，同时进行关键词的取代，
# with open("ha.conf", mode='r', encoding='utf-8') as read_file, open("new.conf", mode='w', encoding='utf-8') as write_file:
#     for line in read_file:
#         new_line = line.replace("luffycity", 'pythonav')
#         write_file.write(new_line)
#
# #重命名文件，同名文件新文件会覆盖掉旧文件
# import shutil
# shutil.move('new.conf', 'ha.conf')

#第一次尝试
    # res = read_file.read()
    # res.replace("luffycity", 'pythonav')
    # print(res)
    # # with open("ha.conf", mode='wt',encoding='utf-8') as f1:
    #     f1.write(res)

