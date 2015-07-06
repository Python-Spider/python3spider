#--*--coding:utf-8--*--
import re
import urllib.request
from urllib.error import URLError,HTTPError
import sys

url = "http://www.qiushibaike.com/imgrank/page/1"
# ���ļ�����ͷ��Ϣ������ģ�����������
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
j=0
for i in range(1,30+1):
    try:
        #ʵ�ַ�ҳ��ҳ
        url = re.sub('page/\d+','page/%d'%i,url,re.S)
        print(url)
        #�������󣬻�÷�����Ϣ
        req = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(req,timeout=15)
        content = response.read().decode('utf-8')
        #�����ȡ��web��ҳ��������Ϣ������
        items1 = re.findall('<div class="article block untagged mb15" id=(.*?)<div class="stats"',content,re.S)

        for i in items1:
            # ���ʹ��������ʽ��������ץ����ץСԭ�򡣳ɹ�ץȡ������ͼƬ��ַ
            items2 = re.findall('<div class="thumb">(.*?)</div>',i,re.S)
            picurl = re.findall('<img src=\"(.*?)\"',items2[0],re.S)
            print(picurl[0])
            pic = urllib.request.urlopen(picurl[0])
            jpgpic = pic.read()
			#��������и�pic�ļ���
            fp = open('pic/'+str(j)+'.jpg',"wb")
            print(j)
            # д���ļ�
            fp.write(jpgpic)
            fp.close()
            j=j+1
    except HTTPError as e:
        print("HTTPError")
    except URLError as e:
        print("URLError")

