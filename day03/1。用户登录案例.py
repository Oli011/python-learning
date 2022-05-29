#实现一个用户登录系统，如果密码错误则反复提示让用户重新输入，直到输入正确停止

# print("系统开始运行")
#
# flag = True
# while flag:
#     user = input("请输入用户名：")
#     pwd = input("请输入密码：")
#     if user == "aa" and pwd == "luffy":
#         print("登陆成功")
#         flag = False
#     else:
#         print("用户名或密码错误")
#
# print("系统结束")

#阶段练习题
#1.补充代码实现设定理想数字，66，
# 让用户一只输入，比66大，现实大了，比小，显示小了；等于，显示正确
# num = 66
# flag = True
# while flag:
#     no = input("请输入数字：")
#     nums = int(no)
#     if nums == num:
#         print("正确")
#         flag = False
#     elif nums > num:
#         print("大了")
#     else:
#         print("小了")

#2.使用循环输出1-100内所有整数
# num = 1
# while num < 101:
#     print(num)
#     num = num + 1
#3.使用循环输出
# num = 1
# #如何判断能否被整除(取余数）
# #多个条件判断，while优先用作判断次数，更细节的判定可在内层代码里
# while num < 11:
#     if num % 7 != 0:
#         print(num)
#     num = num + 1
#4输出奇数
# num = 1
#
# while num < 101:
#     if num % 2 != 0:
#         print(num)
#     num = num + 1

#5输出偶数
# num = 1
#
# while num < 101:
#     if num % 2 == 0:
#         print(num)
#     num = num + 1
#6求和
# num = 1
#多增加一个变量来储存和值
# a = 0
# while num < 101:
#     a = a + num
#     num = num + 1
#最终显示记得要输出
# print(a)
# 7 输出10-1所有整数
#关键是顺序，打点计时器可以反向设置
# num = 10
#
# while num > 0:
#     print(num)
#     num = num - 1
#注意打点步骤的顺序

#交错数列1-100求和（奇数加偶数减）
'''
num = 1
#多增加一个变量来储存和值
a = 0
while num < 101:
    #奇数判断
    if num % 2 != 0:
        a = a + num
    #偶数判断
    if num % 2 == 0:
        a = a - num
    num = num + 1
#最终显示记得要输出
print(a)
'''
