#引入random模块，不是内置函数
import random 
print('-------猜数游戏------')
#input函数输入为字符串类型
str=input('准备好了吗？YES OR NO\n')
while str=='YES':
    #随机函数用法
    key = random.randint(1,10)
    #数据类型转换
    num=int(input('你心里的数字是什么？\n'))
    while num != key :
        if num > key :
            print('猜大了')
            num = int(input('继续猜\n'))
        if num < key :
            print('猜小了')
            num = int(input('继续猜\n'))
    print('恭喜你，猜对了\n')
    str=input('你还要继续游戏吗？YES OR NO\n')
print('欢迎下次再玩！')
