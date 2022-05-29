import faker
import random

staff_list = []

alex = faker.Faker(locale="zh_CN")
for i in range(1,301):
    staff_list.append(alex.name())

level = [30, 6, 3]

for i in range(3):
    winner_list = random.sample(staff_list, level[i])
    for w in winner_list:
        staff_list.remove(w)
    #print(f"剩余人{len(staff_list)}人")
    print(f"获得{3 - i}等奖的是：{winner_list}")