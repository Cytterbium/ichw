#!/usr/bin/env python
# coding: utf-8

# In[9]:


#!/usr/bin/env python3

"""assign2.py:  exchange money 

__author__ = "xuzhun"
__pkuid__  = "1800011793"
__email__  = "1800011793@pku.edu.cn"
"""


def exchange(currency_from, currency_to, amount_from):
    '''
    进行货币计算，输出   转换后的金额数字
    currency_from表示    被转换单位
    currency_to表示        转换成的单位
    amount_from表示      转换前金额数（以原单位）
    '''
    
    #part 1 get useful string named 's_pre'
    URL='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+            currency_from+'&to='+currency_to+'&amt='+amount_from
    from urllib.request import urlopen
    doc = urlopen(URL)
    docstr = doc.read()
    doc.close()
    s_pre = docstr.decode('ascii')
    
    #part 2 deal with the string and get exchanged amount of money.
    for i in ["{","}",",",":",'"to"','"from"','"success"','"']:
        s_pre=s_pre.replace(i,'')
    s=s_pre.split("  ")
    get_to=s[2]
    a=get_to.split(maxsplit=1)
    b=float(a[0])
    return b


def test_exchange():
    # test for exchange(currency_from, currency_to, amount_from) 
        
    assert(2.1589225 == exchange('USD','EUR','2.5'))        
    assert(483.728663==exchange('USD','AMD','1'))
    assert(30.775==exchange('USD','TWD','1'))
    print("All tests passed")


def main():
    # run the testment and get currency_from, currency_to, amount_from from input
    # print the total amount after exchange
    
    test_exchange()
    currency_from=input()
    currency_to=input()
    amount_from=input()
    print(exchange(currency_from, currency_to, amount_from))

    
if  __name__ == '__main__':
    main()

