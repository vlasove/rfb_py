# Изменяемость
nums = [10, 20, 30 , 40]
nums[0] = 9999999999

print(nums)

# Ссылочность списков
a_list = [1, 2, 3] # oxfxofx8ff39191
b_list = a_list[:] # a_list.copy()

b_list.append("Vasya")

print("A_list:", a_list)
print("B_list:", b_list)