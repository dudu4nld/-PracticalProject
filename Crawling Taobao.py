#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pymysql
from time import sleep
from selenium import webdriver
import requests
from lxml import etree


# In[19]:


sql = 'insert into bookdate(name,price,detail) values(%s,%s,%s)'
db = pymysql.connect(host = 'localhost',user = 'root',password = '123456',port = 3306,db = 'bookdate')
cursor = db.cursor()
cursor.execute('create table bookdate(name varchar(255)'
               ',price varchar(255)'
               ',detail varchar(255))')


# In[ ]:





# In[20]:


headers={'cookie':'miid=1302726571432218338; cna=0qvXGJRM5kICATs7CRxNTsQn; t=91b869176ac93bf1ecd3f00a017e7446; sgcookie=E1000Ak%2F3YDC9YsebpLOnslZmDNSI5EuggbtyS7PKRBYQNkAdlItdZDrdUpf7FisZaGw70szeBxxXDUxHckYVQR2Uw%3D%3D; uc3=nk2=F5REP7kaOdMtKGk%3D&id2=Vy0Rol9JmtDw3g%3D%3D&vt3=F8dCuwpukXWhmnLL0nY%3D&lg2=UIHiLt3xD8xYTw%3D%3D; lgc=tb115784539; uc4=id4=0%40VXqfu5po7VJ4Zs4IOLoIHIvidKzS&nk4=0%40FY4Pba1tqax6%2Bbv5LeuhADR%2FbhQwPw%3D%3D; tracknick=tb115784539; _cc_=W5iHLLyFfA%3D%3D; mt=ci=22_1; thw=cn; enc=WOxm8Noie7%2F0Lia8nZwp9IuZ94cHmQHGqVI81wCzJp9qWWebvxiPvI5LX3ID4vrsWxTYbu56PZzxnERibj3cYA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; xlly_s=1; _samesite_flag_=true; cookie2=1332b916526961dcf85963257652be3c; _tb_token_=5b3e31f387a59; _m_h5_tk=c0fe63ace6d1d3a154183c6ebdce15fd_1619527288819; _m_h5_tk_enc=b63b8535b2717c73c3ab2b1909833403; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _uab_collina=161951787107890638346109; uc1=cookie14=Uoe1i6rUlty2Uw%3D%3D; x5sec=7b227365617263686170703b32223a226535366334663334663564613265316434656562646633663937393963313330434d66666e3451474550626a2b5a507731636e7a33514561444451784d6a63304e6a67794d6a55374d54436e68594b652f502f2f2f2f3842227d; JSESSIONID=26A7B103158C5A82F069070C00499293; tfstk=cyEdBFgQR1fHFNMT3yQGVXmkui6GZgvKZpGJ29aidhbByf-RiBZ0D23GRYRKXOC..; l=eBE4mOMRjKWnv_19BOfwourza77OSIRAguPzaNbMiOCPOQ1p5ktfW61urOY9C3GVh6ryR3yIziz8BeYBqIv4n5U62j-la_kmn; isg=BD8_w5CrY_FtvmfpIWTwrWhUzhPJJJPGjRMG2dEM2-414F9i2fQjFr3yIrAeuGs-',
         'user-agent':'Mozilla/5.0'}
url = 'https://search.jd.com/Search?keyword=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&wq=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&psort=3&click=1'


# In[21]:


response = requests.get(url,headers=headers)
response.encoding = 'udf-8'
text = response.text
html = etree.HTML(text)


# In[22]:


list = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li')


# In[23]:


for x in list:
    name = x.xpath('.//div[@class="p-name"]//em/text()')
    price = x.xpath('.//div[@class="p-price"]/strong/i/text()')[0]
    detail = x.xpath('.//div[@class="p-bookdetails"]//text()')
    
    na = ''
    for x in name:
        na += str(x).split(" ")[0]
    s = ''
    for i in price:
        s += str(i)
    sj = ''
    for j in detail:
        sj += str(j)
    sj2 = sj.replace('\n','').replace('\t','')
    data = (na,s,sj2)
    print(data)
    db.ping(reconnect=True)
    cursor.execute(sql,data)
    db.commit()


# In[ ]:




