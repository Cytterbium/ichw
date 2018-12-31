#!/usr/bin/env python
# coding: utf-8

# In[44]:


"""wcount.py: count words from an Internet file.

__author__ = "XuZhun"
__pkuid__  = "1800011793"
__email__  = "1800011793@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import urllib.error


def wcount(astring, topn=10):

    #设置储存器chucunqi和处理器chuliqi，字母表zimubiao
    zimubiao='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chucunqi=''
    dic={}
    dic_={}
    
    for i in astring:
        if i in zimubiao:
            chucunqi+=i     #将字母相连的子字符串截下来，储存到dic中
                                  #但会把但字母符号比如 r  n  截下来
        else:
            chuliqi=chucunqi
            if chuliqi not in dic:
                dic[chuliqi]=1
            else:
                dic[chuliqi]+=1

            chucunqi=''

    z = sorted(zip(dic.values(),dic.keys()),reverse=True) #对dic中values进行排序。倒序。
    
    for (i,x) in z: #筛去无意义的单字母符号和空号，生成新字典dic_
        if x=='' or x in ['b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']:
            pass
        else:
            dic_[x]=i

    #打印“整齐”双列       
    x=0
    for i in dic_:
        if x>=topn:
            break
        else:
            print(i.ljust(20)+' '*8+str(dic_[i]).ljust(20))
            x+=1

if __name__ == '__main__':
    
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    
    else:
        url=sys.argv[1]
        
        try:
            topn=int(sys.argv[2])
            if topn<=0:
                print('topn无意义，无输出')
        except ValueError:  
            #若输入如‘a’等无法进行int（）运算的，将报错，并赋值topn=10
            print('topn无效，默认作10运行程序')
            topn=10

        #打开网址得到包含内容的string，命名为astring
        try:
            doc = urlopen(url)
            docstr = doc.readline()
            lines = docstr.decode('utf-8')  #采用utf-8进行读码
            astring=lines

            while lines:
                docstr = doc.readline()
                lines = docstr.decode('utf-8')
                astring=astring+lines
            astring=astring.lower()  #转化为小写
            doc.close()
            wcount(astring,topn)  #运行函数，得到打印的列表（如果有的话）
            
        except urllib.error.URLError as e:
            #报错：未连接网络或网址错误
            print('未连接网络或网址有误'+str(e.reason))
            

