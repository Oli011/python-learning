#打开数据源文件和创建结果文件
with open('day03快递分拣数据源.md', mode='r', encoding='utf-8') as source, open('result.md', mode='at', encoding='utf-8') as result:
    #将数据源文件进行处理
    aa = source.read()
    bb = aa.split("\n")
    cc = []
    for item in bb:
        acc = item[:-1].strip()
        cc.append(acc)

    #创建空列表存储地址
    place = []
    infos = {}
    #找齐所有省份
    for item in cc:
        province = item.strip().split(',')[1][1:4]
        place.append(province)
    #省份去重
    final_place = list(set(place))

    #各个省份找到对应地址并添加字典
    for pro in final_place:
        infos[pro] = []
        for line in cc:
            if line.strip().split(',')[1][1:4] == pro:
                infos.get(pro).append(line)
    #结果写入，像作业要求中的换行格式处理，暂时没想
    result.write(str(infos))
