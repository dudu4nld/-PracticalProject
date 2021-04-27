import requests
import re
import csv

def getHTMLText(url):
    headers={'cookie':'miid=1302726571432218338; cna=0qvXGJRM5kICATs7CRxNTsQn; t=91b869176ac93bf1ecd3f00a017e7446; sgcookie=E1000Ak%2F3YDC9YsebpLOnslZmDNSI5EuggbtyS7PKRBYQNkAdlItdZDrdUpf7FisZaGw70szeBxxXDUxHckYVQR2Uw%3D%3D; uc3=nk2=F5REP7kaOdMtKGk%3D&id2=Vy0Rol9JmtDw3g%3D%3D&vt3=F8dCuwpukXWhmnLL0nY%3D&lg2=UIHiLt3xD8xYTw%3D%3D; lgc=tb115784539; uc4=id4=0%40VXqfu5po7VJ4Zs4IOLoIHIvidKzS&nk4=0%40FY4Pba1tqax6%2Bbv5LeuhADR%2FbhQwPw%3D%3D; tracknick=tb115784539; _cc_=W5iHLLyFfA%3D%3D; mt=ci=22_1; thw=cn; enc=WOxm8Noie7%2F0Lia8nZwp9IuZ94cHmQHGqVI81wCzJp9qWWebvxiPvI5LX3ID4vrsWxTYbu56PZzxnERibj3cYA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; xlly_s=1; _samesite_flag_=true; cookie2=1332b916526961dcf85963257652be3c; _tb_token_=5b3e31f387a59; _m_h5_tk=c0fe63ace6d1d3a154183c6ebdce15fd_1619527288819; _m_h5_tk_enc=b63b8535b2717c73c3ab2b1909833403; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _uab_collina=161951787107890638346109; x5sec=7b227365617263686170703b32223a223561393532353535316132396339623430326439653863623364663932393630434a50466e34514745502b446d2f712f365a583259686f4d4e4445794e7a51324f4449794e5473784d4b6546677037382f2f2f2f2f77453d227d; uc1=cookie14=Uoe1i6rUlty2Uw%3D%3D; JSESSIONID=C5259AB173F5ED93445DC0417A700566; tfstk=cT95BPjJ2z452DlUU3i4a6GNqRXCZg3fmb_JVCFFeLZjpNt5i62N5Tmwtr2A6i1..; l=eBE4mOMRjKWnvdLQBOfwnurza77tsIRAguPzaNbMiOCP9_5p55KVW61u0lT9CnGVh6-DR3yIzizJBeYBqIv4n5U62j-lasDmn; isg=BMPDN-bip61kGGvdBYg04cSgUodtOFd6sacKzfWgGiKZtOPWfQmWyrwmKkT6FK9y',
         'user-agent':'Mozilla/5.0'}
    try:
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(ilt,html):
    #正则表达式获取商品名称和商品价格
    try:
#使用正则表达式，\表示引入一个"view_price"的键，后面\引入键的值
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
#*？表示最小匹配
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([price,title])
    except:
        print(" ")
def printGoodslist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for x in ilt:
        count = count + 1
        print(tplt.format(count,x[0],x[1]))



def main():
    goods = '编程书籍'
    depth = 2
    star_url = 'https://s.taobao.com/search?q=' +goods
    infoList = []
    for i in range(depth):
        try:
            url = star_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodslist(infoList)
main()