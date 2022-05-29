# 1#用户登录系统，连续三次输入错误之后直接退出，每次输入错误时显示剩余错误次数（字符串格式化）
#
# print("系统开始运行,请登录")
# #计算登录次数
# i = 3
# #连续三次输入错误之后退出，循环判断条件设定
# while i > 0 :
#     user = input("请输入用户名：")
#     pwd = input("请输入密码：")
#     if user == "aa" and pwd == "luffy":
#         print("登陆成功")
#     else:
#         i = i - 1
#         #字符串格式化用来显示剩余错误次数
#         print("用户名或密码错误,还有{}次尝试机会".format(i))
# if i == 0:
# print("登录失败，退出系统")

#2 猜年龄，最多尝试三次，三次错误直接退出，猜对了，恭喜并退出
# print("猜年龄")
# #计算猜测次数
# i = 3
# real = 22
# #连续三次输入错误之后退出，循环判断条件设定
# while i > 0:
#     user = input("请猜年龄：")
#     if int(user) == real:
#         print("恭喜你，猜对了")
#         break
#     elif int(user) > real:
#         i = i - 1
#         #字符串格式化用来显示剩余错误次数
#         print("猜大了,还有{}次尝试机会".format(i))
#     elif int(user) < real:
#         i = i - 1
#         #字符串格式化用来显示剩余错误次数
#         print("猜小了,还有{}次尝试机会".format(i))
# if i == 0:
#     print("失败，退出系统")
#3 继续玩版本
# def guess():
#     print("猜年龄")
#     #计算猜测次数
#     i = 3
#     real = 22
#     while i > 0:
#         user = input("请猜年龄：")
#         if int(user) == real:
#             print("恭喜你，猜对了")
#             break
#         elif int(user) > real:
#             i -= 1
#             #字符串格式化用来显示剩余错误次数
#             print("猜大了,还有{}次尝试机会".format(i))
#         elif int(user) < real:
#             i = i - 1
#             #字符串格式化用来显示剩余错误次数
#             print("猜小了,还有{}次尝试机会".format(i))
#     if i == 0:
#         reply = input("请问您是否还想继续玩?请输入想/不想")
#         if reply == "想":
#             i = 3
#             guess()
#         else:
#             print("退出系统")
# guess()

# print("猜年龄")
# #计算猜测次数
# i = 3
# real = 22
# while i > 0:
#     user = input("请猜年龄：")
#     if int(user) == real:
#         print("恭喜你，猜对了")
#         break
#     elif int(user) > real:
#         i -= 1
#         #字符串格式化用来显示剩余错误次数
#         print("猜大了,还有{}次尝试机会".format(i))
#     elif int(user) < real:
#         i = i - 1
#         #字符串格式化用来显示剩余错误次数
#         print("猜小了,还有{}次尝试机会".format(i))
#     if i == 0:
#         reply = input("请问您是否还想继续玩?请输入想/不想")
#         if reply == "想":
#             i = 3
#             continue
#         else:
#             print("退出系统")
#             break