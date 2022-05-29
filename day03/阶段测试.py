# 16. 请将字符 `name = &quot;wupeiqi&quot;` 翻转。
#
# ```python
# name = "&quot;wupeiqi&quot;"
# print(name[::-1])
# # ```
#
# 17. 进制之间如何进行转换？
# 10:int   16:hex   2:bin   8:oct
# 其他转10：  int（“****”，base=*）
# 18. 循环过程中 break和continue的作用是什么？
# 19. 看代码写结果
#
# ```
# v1 = 1 or 9 and 88 or [11,22] and (1,2,3)
# 9
# v2 = 1&gt;5 or &quot;alex&quot; and {&quot;K1&quot;:&quot;v1&quot;} or 888
# 888
# print(v1)
#
# ```
#
# 20. 看代码写结果
#
# ```python
# info = [
#     {'k1':(1),'k2':{'k9':'luffy','k10':'武沛齐'}},
#     (11,22,33,44),
#     {199,2,3,4,5},
#     True,
#     ['李杰','alex', { 'extra': ("alex",[18,20],'eric') } ]
# ]
# ```
#
# - 利用索引获取 "luffy"
# a = info[0].get("k2").get("k9")
# print(a)
# - 利用索引获取 44
# a = info[1][3]
# print(a)
# - 删除k10对应的键值对
# a = info[0].get("k2").pop("k10")
# print(info)
# - 在 `{ 'extra': ("alex",[18,20],'eric') }` 字典中添加一个键值对 `"name":"武沛齐"`
# info[4][2].update({"name":"武沛齐"})
# print(info)
# - 在集合` {199,2,3,4,5} `中添加一个 "北京"
# info[2].add("北京")
# print(info)
# - 将列表中的True修改为 "真"
# del info[3]
# info.insert(3,"真")
# print(info)
# - 在列表 `[18,20]`的第0个索引位置插入 666
# info[4][2].get("extra")[1].insert(0,"666")
# print(info)
#
# 21. 判断下面的代码是否正确？正确的话则写出结果，否则标明错误。
#
# ```python
# v1 = (11,22,33)
# v2 = (11)
# v3 = {11,2,33}
# v4 = {11,2,("alex","eric"),33} set 不可哈希
# v5 = {11,2,("alex",{"北京","上海"},"eric"),33} set 不可哈希
# ```
#
# 22. 看代码写结果
#
# ```python
# v1 = [11,22,33]
# v2 = [11,22,33]
# v1.append(666)
# #
# print(v1)
# # [11,22,33,666]
# print(v2)
# ```
#
# 23. 看代码写结果
#
# ```python
# v1 = [11,22,33]
# v2 = v1
# v1.append(666)
#
# print(v1)
# print(v2)
# ```
#
# 24. 看代码写结果
#
# ```python
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
# v2[1][0] = 111
# v2[2][0] = 222
# #
# print(v1)
# print(v2)
# ```
#
# 25. 写代码实现，循环提示用户输入内容（Q或q终止），并将内容用 "_" 连接起来。
# aa = []
# while True:
#     a = input("请输入内容，输入Q或q终止")
#     if a.upper() == "Q":
#         break
#     aa.append(a)
# re = "_".join(aa)
# print(re)

#
# 26. 写代码实现，将IP转换为整数。
#
# > 如 10.3.9.12 转换规则为：
# >         10            00001010
# >          3             00000011
# >          9             00001001
# >         12            00001100
# > 再将以上二进制拼接起来，然后再进行一次翻转。
# a = "10.3.9.12"
# b = a.split(".")
# e = []
# for c in b:
#     d = bin(int(c))[2:].zfill(8)
#     e.append(d)
# re ="".join(e)[::-1]
#
# print(re)
# > 最终将翻转之后的二进制转换为整型。
#
# 27. 写代码实现，车牌的区域划分。
#
# ```python
# car_list = ['鲁A32444', '沪B12333', '京B8989M', '京C49678', '黑C46555', '晋B25041', '沪C34567']
# info = {}
# for item in car_list:
#     city = item[0]
#     num = info.get(city,0)
#     info[city] = num + 1
#
#     # a = 0
#     # if item.startswith("鲁"):
#     #     a += 1
#     #     info["鲁"] = a
#     # b = 0
#     # if item.startswith("沪"):
#     #     b += 1
#     #     info["沪"] = b
#     # c = 0
#     # if item.startswith("京"):
#     #     c += 1
#     #     info["京"] = c
#     #
#     # d = 0
#     # if item.startswith("黑"):
#     #     d += 1
#     # e = 0
#     # if item.startswith("晋"):
#     #     e += 1
#
# print(info)
# # 根据以上代码获取各省车牌数量，例如：info = {"沪":2,"京":2 ...}
# ```
#
# 28. 写代码实现，数据格式化处理。
#
# ```python
text = """id,name,age,phone,job
1,alex,22,13651054608,IT 
2,wusir,23,13304320533,Tearcher
3,老男孩,18,1333235322,IT"""
#
# # 将上述数据处理为如下格式的结果：
# #    info = [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},.... ..]
# # 提示：text的内容是根据 \n 分割（\n表示回车换行）。

# #找出title，合并剩余列表，切片取各个部分
# info = []
# #创建空列表来存储用户信息（包含键值对的字典）
# a = text.split("\n")
# #将文本按换行符分割
# title_list = a[0].split(",")
# #取出标题所在列表并按，分割
# for b in a[1:]:
#     b = b.split(",")
#     #将剩余列表按，分割
#     item = {}
#     for i in range(len(title_list)):
#         item[title_list[i]] = b[i]
#         #按照索引，每个标题对应信息创建相应字典
#     info.append(item)
#     #将字典加入列表
#
# print(info)
# # ```
#
# 29. 写代码实现 累乘计算器。
#
# ```python
# content = input("请输入内容:") # 用户可能输入 5*9*99.... 或 5* 9 * 10 * 99 或 5 * 9 * 99...
# content = input("请输入内容:")
# a = content.strip().split("*")
# b = 1
# for i in range(len(a)):
#     b = b * int(a[i])
# print(b)

# # 补充代码实现
# ```
#
# 30. 使用for循环实现输出 9*9 乘法表
#
# ```
# 1*1
# 2*1 2*2
# 3*1 3*2 3*3
# 4*1 4*2 4*3 4*4
# 5*1 5*2 5*3 5*4 5*5
# 6*1 6*2 6*3 6*4 6*5 6*6
# 7*1 7*2 7*3 7*4 7*5 7*6 7*7
# 8*1 8*2 8*3 8*4 8*5 8*6 8*7 8*8
# 9*1 9*2 9*3 9*4 9*5 9*6 9*7 9*8 9*9
# ```
# for i in range(1,10):
#     for j in range(1,i + 1):
#         text = "{}*{}".format(j,i)
#         print(text, end=" ")
#     print("")

# 31. 补充代码实现《棋牌游戏11点》
#
# 需求：
#
# - 生成一副扑克牌（自己设计扑克牌的结构，小王和大王可以分别用14、15表示 ）

# 设定四个花色


# - 3个玩家
#
# ```python
# user_list = ["alex","武沛齐","李路飞"]
# ```
#
# - 发牌规则
#
# - 默认先给用户发一张牌，其中 J、Q、K、小王、大王代表的值为0.5，其他就是则就是当前的牌面值。
# - 用户根据自己的情况判断是否继续要牌。
# - 要，则再给他发一张。
# - 不要，则开始给下个玩家发牌。
# - 如果用户手中的所有牌相加大于11，则表示爆了，此人的分数为0，并且自动开始给下个人发牌。
#
# - 最终计算并获得每个玩家的分值，例如：
#
# ```python
# result = {
#     "alex":8,
#     "武沛齐":9,
#     "李路飞":0
# }
# ```
#
# 必备技术点：随机抽排
#
# ```python
# import random
#
# #
# # total_poke_list = [("红桃", 1), ("黑桃", 2), ("大王", 15), ("小王", 14)]
# #
# # 生成扑克牌
# card = [("小王", 14), ("大王", 15)]
# color = ["梅花", "方块", "红心", "黑桃"]
# #生成1-13卡片
# for item in color:
#     #添加A
#     card.append(tuple([item, "A"]))
#     #添加2-10
#     for i in range(2, 11):
#         cc = tuple([item, i])
#         card.append(cc)
#     #添加J、Q、K
#     for j in ["J", "Q", "K"]:
#         cc = tuple([item, j])
#         card.append(cc)
#
# # 计分空字典
# result = {}
# # 玩家列表
# user_list = ["alex", "武沛齐", "李路飞"]
#
# # 对于每个玩家进行抽牌,
# # 首轮发牌
# for user in user_list:
#     # # 随机生成一个数，当做索引。
#     index = random.randint(0, len(card) - 1)
#     # print("抽到的牌为：", card[index])
#     # print("抽完之后，剩下的牌为：", card)
#     # 踢除这张牌
#     poke = card.pop(index)
#     ###！！！！！！用变量储存分数！！！！！！！！！！！！！！！！！！
#     score = 0
#     p = poke[1]
#     #点数判断分数
#     # 判断点数是否是整型
#     if isinstance(p, int):
#         # 排除大小王
#         if p < 14:
#             value = p
#         # 大小王为0.5点
#         else:
#             value = 0.5
#     else:
#         # A为1点
#         if p == "A":
#             value = 1
#         # JQK为0.5点
#         else:
#             value = 0.5
#     score += value
#     print("给{}发牌：{}{}，此时所有牌面值总和：{}".format(user,poke[0],poke[1],score))
#
#     while True:
#         # #次轮及以后选择要不要发牌
#         con = input("是否继续发牌，输入N/n不要发牌")
#         if con.upper() == "N":
#             print("{}不要牌了".format(user))
#             break
#         index = random.randint(0, len(card) - 1)
#         # print("抽到的牌为：", card[index])
#         # print("抽完之后，剩下的牌为：", card)
#         # 踢除这张牌
#         poke = card.pop(index)
#         #点数判断分数
#         p = poke[1]
#         # 判断点数是否是整型
#         if isinstance(p, int):
#             # 排除大小王
#             if p < 14:
#                 value = p
#             # 大小王为0.5点
#             else:
#                 value = 0.5
#         else:
#             # A为1点
#             if p == "A":
#                 value = 1
#             # JQK为0.5点
#             else:
#                 value = 0.5
#         score += value
#         print("给{}发牌：{}{}，此时所有牌面值总和：{}".format(user,poke[0],poke[1],score))
#
#         if score > 11:
#             print("用户{}爆了".format(user))
#             score = 0
#             break
#     result[user] = score
# print(result)
#
#
# #
# # #
# # 代码示例：（请补充实现）
# #
# # ```python
# # result = {}
# # user_list = ["alex","武沛齐","李路飞"]
# # # 补充代码
# #
# #
# # print(result) ```
