import pandas as pd


# 定义大小比较函数
def bigger(a, b):
    return a > b


def smaller(a, b):
    return a < b


# 定义取元素中的第一个元素
def take_first(elem):
    return elem[1]


# 加载数据
with open('stock_data.txt', mode='rt', encoding='utf-8') as source:
    # 创建空列表来存储数据源
    stocks_list = []
    # 将数据传输到内存
    title = source.readline().strip().split(',')

    # 创建title列表

    title.insert(0, '序号')



    res = source.readlines()
    # 整理股票数据源
    for stock in res:
        stock = stock.strip().split(',')
        stocks_list.append(stock)
    # 为每个数据创建序号
    for stock in stocks_list:
        stock.insert(0, "{}".format(stocks_list.index(stock) + 1))

# 用户登录及启动，手动添加序号
while True:
    # 建立空列表来存储结果
    result_list = []
    # 提醒用户进行输入来选择功能
    user_choice = input("请输入'股票查询'或者'股票筛选'来选择功能:(退出请输入Q/q)")
    # 检验是否退出
    if user_choice.upper() == "Q":
        break
    # 股票查询

    elif user_choice == "股票查询":
        user_search = input("请输入要查询的股票名称：(退出请输入Q/q)")
        if user_search.upper() == "Q":
            break
        # 对查询到的结果进行计数
        i = 0
        for stock in stocks_list:
            if user_search in stock[2]:
                print(title)
                result_list.append(stock)
                i += 1
                print(stock)
        print("找到{}条".format(i))
    # 股票筛选
    elif user_choice == "股票筛选":
        print(title)
        user_filter = input("请输入要筛选的条件：(退出请输入Q/q)")
        if user_filter.upper() == "Q":
            break
        # 大于
        if '>' in user_filter:
            num = user_filter.strip().split('>')
            for stock in stocks_list:
                index = title.index(num[0])
                final_num = float(stock[index].strip('%' and '+' and '-'))
                re = filter(bigger(final_num, float(num[1])), stock[index])
                result_list.append(re)
            # 结果列表中按照第一个元素，即后来添加的序号来进行排序
            result_list.sort(key=take_first, reverse=False)
            print(result_list)
        # 小于
        elif '<' in user_filter:
            num = user_filter.strip().split('<')
            for stock in stocks_list:
                index = title.index(num[0])
                final_num = float(stock[index].strip('%' and '+' and '-'))
                result_list.append(filter(smaller(final_num, float(num[1]))))
            # 结果列表中按照第一个元素，即后来添加的序号来进行排序
            result_list.sort(key=take_first, reverse=False)
            print(result_list)
        else:
            print("输入格式错误，请按照格式输入")
    else:
        print("输入格式错误，请重新输入")

# pandas自动添加序号【不用，因为每次查找的结果的编号都是新的，不能满足需求】
# while True:
#     user_search = input("请输入要查询的股票名称：(退出请输入Q/q)")
#     if user_search.upper() == "Q":
#         break
#     result_list = []
#     i = 0
#     for stock in stocks_list:
#         if user_search in stock[1]:
#
#             result_list.append(stock)
#             i += 1
#     df = pd.DataFrame(result_list, columns=title)
#     print(df)
#     print("找到{}条".format(i))
