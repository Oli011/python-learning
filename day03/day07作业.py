# ## 作业
#
# 1. 根据需求写代码
#
# ```python
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# # 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic.setdefault("k4", "v4")
# print(dic)
# # 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic.update({"k1":"alex"})
# print(dic)
# 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic.update({"k3":[11,22,33,44]})
# print(dic)
# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic["k3"].insert(1,18)
# print(dic)
# ```
#
# 2. 根据需求写代码
#
# ```python
# dic = { 'name':['alex',2,3,5], 'job':'teacher', 'oldboy':{'alex':['python1','python2',100]}}
# 1，将name对应的列表追加⼀个元素’wusir’。
# dic["name"].append("wusir")
# print(dic)
# 2，将name对应的列表中的alex全变成大写。
# dic["name"][0] = dic["name"][0].upper()
# print(dic)
# 3，oldboy对应的字典加⼀个键值对’⽼男孩’:’linux’。
# dic["oldboy"]["老男孩"] = "linux"
# 4，将oldboy对应的字典中的alex对应的列表中的python2删除
# dic["oldboy"].get("alex").remove("python2")
# print(dic)

# ```
#
# 3. 循环提示用户输入，并将输入内容添加到字典中（如果输入N或n则停止循环）
#
# ```python
# 例如：用户输入 x1|wupeiqi ,则需要再字典中添加键值对 {'x1':"wupeiqi"}
# ```
# info = {}
# while True:
#     aa =input("请输入用户名和密码，中间用“|”隔开，输入N/n停止输入:")
#     if aa.upper() == "N":
#         break
#     c = aa.split("|")
#     if len(c) == 2:
#         name = c[0]
#         pwd = c[1]
#         info[name] = pwd
# print(info)
# 4. 判断以下值那个能做字典的key ？那个能做集合的元素？
# - 1
# - 1
# - ""
# - None
# - [1,2]
# - (1,)
# - {11,22,33,4}
# - {‘name’:‘wupeiq’,‘age’:18}
# 5. 将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
#
# ```python
# key_list = []
# value_list = []
# info = {'k1':'v1','k2':'v2','k3':'v3'}
# key_list = info.keys()
# value_list = info.values()
#
# print(value_list)
# ```
#
# 6. 字典dic = {‘k1’: “v1”, “k2”: “v2”, “k3”: [11,22,33]}
#
# ```python
# info = {'k1':'v1','k2':'v2','k3':'v3'}
# a. 请循环输出所有的ke
# for key in info:
#     print(key)
# b. 请循环输出所有的value
# for value in info.values():
#     print(value)
# c. 请循环输出所有的key和value
# for key,value in info.items():
#     print(key,value)
# ```

#
# 7. 请循环打印k2对应的值中的每个元素。
#
# ```python
# info = {    'k1':'v1',    'k2':[('alex'),('wupeiqi'),('oldboy')],}
# for item in info.get("k2"):
#     print(item)
# ```
#
# 8. 有字符串“k: 1|k1:2|k2:3 |k3 :4” 处理成字典 {‘k’:1,‘k1’:2….}
# aa = "k: 1|k1:2|k2:3 |k3 :4"
# bb = aa.split("|")
# info = {}
# for item in bb:
#     item = item.strip().split(":")
#     info[item[0]] = int(item[1])
# print(info)
# 9. 写代码
#
# ```python
# """有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
# result = {'k1':[],'k2':[]}"""
# ```
# result = {'k1':[],'k2':[]}
# li= [11,22,33,44,55,66,77,88,99,90]
# for item in li:
#     if item > 66:
#         result.get("k1").append(item)
#     else:
#         result.get("k2").append(item)
# print(result)
# 10. 输出商品列表，用户输入序号，显示用户选中的商品
#
# ```python
# """商品列表：
# goods = [{"name": "电脑", "price": 1999},{"name": "鼠标", "price": 10},{"name": "游艇", "price": 20},{"name": "美女", "price": 998}]
# # 要求:
# # 1：页面显示 序号 + 商品名称 + 商品价格，如：      1 电脑 1999      2 鼠标 10      ...
# for item in goods:
#     print(goods.index(item) + 1,item["name"],item.get("price"))
# # 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# while True:
#     aa = input("请输入要购买的商品前面序号：")
#     if aa.upper() == "Q":
#         break
#     if aa.isdecimal():
#         bb = int(aa) - 1
#         if 0 <= bb <= 3:
#             print("{0}{1}元".format(goods[bb].get("name"),goods[bb].get("price")))
#         else:
#             print("序号输入有误，请重新输入")
#     else:
#         print("输入有误，请重新输入")

# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序。"""
# ```