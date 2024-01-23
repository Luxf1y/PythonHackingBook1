# -*- coding: UTF-8 -*-

# import myModule
# import sys

# print('The command line arguments are:')
# for i in sys.argv:
#     print(i)

# print('\n\nThe PYTHONPATH is', sys.path, '\n')


# if __name__ == '__main__':
#     print('当前代码被单独运行')
# else:
#     print('当前代码被导入运行')
# myModule.sayhi()
# print('Version', myModule.version)
# myModule.version = 0.5

# import test

# print(test.c1.name)



#from..import就是在库里面直接调用具体的某个函数
#比如import sys 要使用argv的话，要使用sys.argv
#from sys import argv 的话直接使用argv即可
from sys import argv

print('The command line arguments are:')
# for i in sys.argv:
#     print(i)
print(argv) #这句同上
#print(sys.path)

import myModule
if __name__ == '__main__':
    print('当前代码被单独运行')
else:
     print('当前代码被导入运行')
myModule.sayhi()
print('Version', myModule.version)
myModule.version = 0.5

if __name__ == '__main__':
    print('当前代码被单独运行')
else:
     print('当前代码被导入运行')