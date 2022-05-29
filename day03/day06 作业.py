# 1. 以下哪些数据类型转换为布尔值为False
#
# ```python
# 1""-19[][11,22](1)(1,2,3)()
# ```
#
# 2. 运算符操作
#
# ```python
# v1 = [] or "alex"
# "alex"
# # v2 = [11,22] and (1,2,)
# [11,22]
# ```
#
# 3. 比较：`a = [1,2,3]`和 `b = [(1),(2),(3) ]` 以及 `c = [(1,),(2,),(3,) ]` 的区别？
# 4. 将字符串`text = "wupeiqi|alex|eric"`根据 `|` 分割为列表，然后列表转换为元组类型。
# text = "wupeiqi|alex|eric"
# a = tuple(text.split("|"))
# print(a)
# 5. 根据如下规则创建一副扑克牌（排除大小王）。
# 花色列表
color_list = ["红桃","黑桃","方片","梅花"]
# 牌值
result = []
num_list = []

for item in color_list:
    for num in range(1,14):
        a = (item,num)
        result.append(a)
print(result)

# 请根据以上的花色和牌值创建一副扑克牌（排除大小王）
# 最终result的结果格式为： [ ("红桃",1), ("红桃",2) ... ]