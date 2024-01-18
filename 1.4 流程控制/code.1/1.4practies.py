# #实现用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败！
# username=input("请输入用户名：")
# password=input("请输入密码：")
# if username=="seven" and password=="123":
#     print("登陆成功")
# else:
#     print("登录失败")


#使用while循环实现输出2-3+4-5+6.....+100的和
count=2
y=0
while(count<101):
    x=count*pow(-1,count)
    count +=1
    y=y+x
print(x)