# 打印9*9乘法表
# 行
i = 1
while i <= 9:
    # 列
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end='')
        j += 1
    print() # 换行
    i += 1
