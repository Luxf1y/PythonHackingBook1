def reverse_list(lst):
    reversed_lst = lst[::-1] #使用切片操作符来逆序一个列表的常见方法; 表示从列表的最后一个元素开始，以步长为 -1 的方式遍历整个列表，从而实现逆序输出。
    return reversed_lst

# 测试
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print(reversed_list)