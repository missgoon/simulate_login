import requests
import hashlib
import lxml.html

def get_md5_value(str):
	'''
	  用md5加密字符串
	'''
  myMd5 = hashlib.md5()
  myMd5.update(str)
  return myMd5.hexdigest()

url="http://www.gyu.cn:8078/_data/index_LOGIN.aspx"
url2="http://www.gyu.cn:8078/sys/ValidateCode.aspx"
url3="http://www.gyu.cn:8078/MAINFRM.aspx"
url4="http://www.gyu.cn:8078/SYS/Main_banner.aspx"

headers={
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Connection":"keep-alive",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
	"Referer": "http://www.gyu.cn:8078/_data/index_LOGIN.aspx",
	"Host": "www.gyu.cn:8078",
}
txt_asmcdefsddsd="13051940****"
txt_pewerwedsdfsdff="******"
s1=txt_asmcdefsddsd+str(get_md5_value(txt_pewerwedsdfsdff))[0:30].upper()+"10976"
dsdsdsdsdxcxdfgfg=str(get_md5_value(s1))[0:30].upper()
typeName="Ñ§Éú"
sbtState=""
pcInfo="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0Windows NT 6.1; WOW645.0 (Windows) SN:NULL"
Sel_Type="STU"

#begin...
s=requests.Session()
s.cookies["_gscu_1339595322"]="60001265cya00j69"
r1=s.get(url,headers=headers,cookies=s.cookies)
html=lxml.html.fromstring(r1.content)
__VIEWSTATE=html.xpath("//input[@name='__VIEWSTATE']/@value")[0]
#这里抓取验证码  并等待用户输入
r2=s.get(url2,headers=headers,cookies=s.cookies)
with open("gyu_file.jpg","w") as file:
  file.write(r2.content)
txt_sdertfgsadscxcadsads=raw_input("enter verification code:")
s2=str(get_md5_value(txt_sdertfgsadscxcadsads.upper()))[0:30].upper()+"10976"
fgfggfdgtyuuyyuuckjg=str(get_md5_value(s2))[0:30].upper()  
post_data={"__VIEWSTATE":__VIEWSTATE,"Sel_Type":Sel_Type,"pcInfo":pcInfo,"dsdsdsdsdxcxdfgfg":"EF6BED1526F2F0AD6D5263F44EEF73","fgfggfdgtyuuyyuuckjg":fgfggfdgtyuuyyuuckjg,"sbtState":sbtState,"txt_asmcdefsddsd":txt_asmcdefsddsd,"txt_pewerwedsdfsdff":txt_pewerwedsdfsdff,"txt_sdertfgsadscxcadsads":txt_sdertfgsadscxcadsads,"typeName":typeName}
r3=s.post(url,headers=headers,data=post_data,cookies=s.cookies)  #login
r4=s.get(url4,headers=headers,cookies=s.cookies)  #test login successfully
print(r4.text)