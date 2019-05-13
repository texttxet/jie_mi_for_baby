#coding:utf-8
import time
while 1 < 2:
    shuru_cishu = 10 # 修改这个数值，可以求指定个数数字的和
    i = 0
    sum = 0
    a = list()
    # print(type(lista))
    print('输入')
    while i < shuru_cishu:
        print('请输入第',i + 1,'个数值:')
        houqu_shuru = float(input())
        a.append(houqu_shuru) # 构建列表
        # print(lista)
        sum += houqu_shuru
        i += 1
    time.sleep(1)
    print('输入完成，开始计算..........................')
    average = sum / shuru_cishu
    print('平均值位：{:.5f}'.format(average))
    print('最大值为:',max(a)) # 打印最大值
    print('最小值为:',min(a)) # 打印最小值
    print('计算完毕...................................')