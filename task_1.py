# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Enter the count of nums in 1 array: "))
m = int(input("Enter the count of nums in 2 array: "))

count_n = 0
list_n = []
list_m = []
count_m = 0

while count_n != n:
    num_n = int(input("Enter the n_num: "))
    list_n.append(num_n)
    count_n += 1
# print(list_n)
for i in list_n:
    print(i, end=" ")
print()
list_n = set(list_n)
list_n = list(list_n)


while count_m != m:
    num_m = int(input("Enter the m_num: "))
    list_m.append(num_m)
    count_m += 1
# print(list_m)
for i in list_m:
    print(i, end=" ")
print()
list_m = set(list_m)
list_m = list(list_m)


new_list = []
for i in list_n:
    for j in list_m:
        if i == j:
            new_list.append(i)
sorted(new_list)
for i in new_list:
    print(i, end=" ")





