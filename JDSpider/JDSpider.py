import re
import pandas
import requests

''' response=requests.get('https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv12650&productId=5089225&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1')
response=response.text
#print(response)
pant='"content":"(.*?)","'
res=re.findall(pant,response)
for i in res:
    i=i.replace('\\n','')
    print(i)
type(res) '''
f = open('comment_iphone8_.txt','a')
for i in range(0,720):#720
    try:
        response = requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv4962&productId=5089225&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&rid=0&fold=1')
        response = response.text
        #print(response)
        pat = '"content":"(.*?)","'
        res = re.findall(pat,response)
        for i in res:
            i = i.replace('\\n','')
            #print(i)
            f.write(i)
            f.write('\n')
    except:
        print('爬取第'+str(i)+'页出现问题')
        continue
f.close()