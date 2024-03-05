#阶乘递归
def multi(i):
    if i<0 :
        print("参数应为正整数")
    if i==0:
        return 0
    if i == 1:
        return 1
    if i>1:

        return i*multi(i-1)
#斐波那契数列递归
def F(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return F(n-1)+F(n-2)
f=F(int(input("请输入第几个月的兔子数量：")))
print(f)
