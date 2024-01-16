# def replace_string(original_str, search_str, replace_str):
#     replaced_str = original_str.replace(search_str, replace_str)
#     return replaced_str
#str.replace(old, new[, count])
#返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new。 如果给出了可选参数 count，则只替换前 count 次出现。

def replace_str(old,new,replace):
    a=old.replace(replace,new)
    return a

# 测试
old = "Hello, world!"
replace = "world"
new = "Python"
replaced_string = replace_str(old, new, replace)
print(replaced_string)