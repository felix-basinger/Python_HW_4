from random import randint

count_trees = int(input("Enter the count of trees: "))

count_berries = [randint(1, count_trees) for i in range(count_trees)]
print(count_berries)
count = 0
res_list = []

while count != count_trees:
    if count == count_trees - 2:
        # print(count_berries[-2] + count_berries[-1] + count_berries[0])
        res_list.append(count_berries[-2] + count_berries[-1] + count_berries[0])
    elif count == count_trees - 1:
        # print(count_berries[-1] + count_berries[0] + count_berries[1])
        res_list.append(count_berries[-1] + count_berries[0] + count_berries[1])
    else:
        # print(sum(count_berries[count:count + 3]))
        res_list.append(sum(count_berries[count:count + 3]))
    count += 1
print(res_list)

max_num = res_list[0]
for i in range(len(res_list) - 1):
    if max_num < res_list[i + 1]:
        max_num = res_list[i + 1]
print(max_num)