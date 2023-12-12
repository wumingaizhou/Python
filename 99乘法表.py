# 打印9*9乘法表
# 第一版本
i = 1 # 行
while i <= 9:
    # 列
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end='')
        j += 1
    print() # 换行
    i += 1


# 第二版本
for i in range(1,10):
    for j in range(1,i + 1):
        print(f"{j}*{i}={j * i}\t",end="")
    print()
