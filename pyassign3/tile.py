#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''__author__ = "XuZhun"
__pkuid__  = "1800011793"
__email__  = "1800011793@pku.edu.cn"'''


def getlist(m, n):
    '''生成墙列表
    输出格式为list，比如[0，1，2，3，4]
    '''

    lst = []
    for i in range(m*n):
        lst.append(i)
    return lst


def judge(lst, o, a, b, m):
    '''判断模块
    本模块用于判断在某处的情况分类
    分别输出 1，2，3, False 表示能否铺开，横竖铺的情况
    '''
    tim2 = 0
    tim1 = 0
    for y in range(a):
        for x in range(b):
            i = o + x + m*y
            if i in lst:
                tim2 = tim2 + 1

    for y in range(a):
        for x in range(b):
            i = o + y + m*x
            if i in lst:
                tim1 = tim1 + 1
    if tim2 == a*b and tim1 == a*b and o % m + max(a, b) <= m and a != b:
        return 1
    elif tim2 == a*b and (tim1 != a*b or o % m + a > m or a == b):
        return 2
    elif tim1 == a*b and (tim2 != a*b or o % m + b > m):
        return 3
    else:
        return False


def puzhuan(m, n, a, b, lst):
    '''铺砖模块
    本模块通过递归方法生成铺砖结果，并返回结果列表
    按不同judge函数值进行
    返回list_out即铺法
    '''

    import copy
    list_out = []
    if lst == []:
        return []
    fir = min(lst)
    if judge(lst, fir, a, b, m) is False:
        return []

#第一类情况
    if judge(lst, fir, a, b, m) == 1:
        part = []
        part1 = []
        tem_lst = []
        lstt = copy.copy(lst)
        for y in range(a):
            for x in range(b):
                i = fir + x + m*y
                lstt.remove(i)
                tem_lst.append(i)
        temp = puzhuan(m, n, a, b, lstt)
        if temp == []:
            part = part + [tuple(tem_lst)]
        else:
            for i in temp:
                if type(i) == list:
                    part.append([tuple(tem_lst)] + i)
                else:
                    part = part + [tuple(tem_lst)] + temp
                    break
        for i in part:
            if type(i) == list:
                list_out.append(i)
            else:
                list_out.append(part)
                break
        tem_lst1 = []
        lstt1 = copy.copy(lst)
        for y in range(a):
            for x in range(b):
                i = fir + y + m*x
                tem_lst1.append(i)
                lstt1.remove(i)
        temp1 = puzhuan(m, n, a, b, lstt1)
        if temp1 == []:
            part1 = part1 + [tuple(tem_lst1)]
        else:
            for ii in temp1:
                if type(ii) == list:
                    part1.append([tuple(tem_lst1)] + ii)
                else:
                    part1 = part1 + [tuple(tem_lst1)] + temp1
                    break
        for i in part1:
            if type(i) == list:
                list_out.append(i)
            else:
                list_out.append(part1)
                break
#第二类情况
    elif judge(lst, fir, a, b, m) == 2:
        tem_lst = []
        lstt = copy.copy(lst)
        for y in range(a):
            for x in range(b):
                i = fir + x + m*y
                tem_lst.append(i)
                lstt.remove(i)
        temp = puzhuan(m, n, a, b, lstt)
        if temp == []:
            list_out = list_out + [tuple(tem_lst)]
        else:
            for i in temp:
                if type(i) == list:
                    list_out.append([tuple(tem_lst)] + i)
                else:
                    list_out = list_out + [tuple(tem_lst)] + temp
                    break
                    
#第三类情况
    elif judge(lst, fir, a, b, m) == 3:
        lstt = copy.copy(lst)
        tem_lst = []
        for y in range(a):
            for x in range(b):
                i = fir + y + m*x
                tem_lst.append(i)
                lstt.remove(i)
        temp = puzhuan(m, n, a, b, lstt)
        if temp == []:
            list_out = list_out + [tuple(tem_lst)]
        else:
            for i in temp:
                if type(i) == list:
                    list_out.append([tuple(tem_lst)] + i)
                else:
                    list_out = list_out + [tuple(tem_lst)] + temp
                    break
    return list_out


def wall(m, n):
    '''墙的可视化'''

    import turtle
    t = turtle.Pen()
    t.speed(0)
    for i in range(m*n):
        t.penup()
        t.goto(50*(i//m), 50*(i % m))
        t.pendown()
        for a in range(4):
            t.forward(50)
            t.left(90)
        t.penup()
        t.goto(50*(i//m) + 25, 50*(i % m) + 25)
        t.pendown()
        t.write(str(i), False, "left", ("Arial", 8, "normal"))


def sight(m, a, b, lst):
    '''铺砖结果的可视化'''

    import turtle
    t1 = turtle.Pen()
    t1.speed(0)
    t1.pencolor('red')
    t1.pensize(3)
    for i in lst:
        x = min(i)
        y = max(i)
        t1.penup()
        t1.goto(50*(x//m), 50*(x % m))
        t1.pendown()
        if y == x + (a - 1) + (b - 1)*m:
            for i in [1, 2]:
                t1.fd(50*b)
                t1.left(90)
                t1.fd(50*a)
                t1.left(90)
        else:
            for i in [1, 2]:
                t1.fd(50*a)
                t1.left(90)
                t1.fd(50*b)
                t1.left(90)


def main():
    '''运行模块
    本模块具体执行以上函数，输出结果并根据需要进行可视化
    '''

    m = int(input('m='))
    n = int(input('n='))
    a = int(input('a='))
    b = int(input('b='))
    lst = getlist(m, n)
    result = puzhuan(m, n, a, b, lst)
    result1 = []
    if type(result[0]) == tuple:
        print('一共有1种答案')
        result1.append(result)
        print('1: ' + str(result))
    else:
        for i in range((len(result))):
            if len(result[i]) == m*n/(a*b):
                result1.append(result[i])
        print('一共有' + str(len(result1)) + '种答案')
        for i in range((len(result1))):
            print(str(i+1) + ': ' + str(result1[i]))
    if len(result1) != 0:
        wall(m, n)
        kind = input('要可视化的种类：')
        lst0 = result1[(int(kind) - 1)]
        sight(m, a, b, lst0)


if __name__ == '__main__':
    main()


# In[ ]:




