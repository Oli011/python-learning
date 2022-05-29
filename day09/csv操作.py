import requests
import os

with open("mv.csv", mode='r',encoding='utf-8') as file_object:
    file_object.readline()
    for line in file_object:
        #用三个值去接收
        user_id, user_name, url = line.strip().split(",")
        #print(user_name, url)

        #1.根据url下载图片
        res = requests.get(
            url=url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
        )
        #检查images路径是否存在? 若不存在，则创建images目录
        if not os.path.exists("images"):
            os.makedirs("images")

        #2.将图片的内容下载到文件中,并加上一个images文件夹
        with open("images/{}.png".format(user_name), mode='wb') as img_object:
            img_object.write(res.content)