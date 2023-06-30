import json
import client as pik
import shell_cmds as cmd

if __name__ == "__main__":

    import sys
    if len(sys.argv) >1:
        cred_filename= sys.argv[1]
    else:
        cred_filename="client.json"
    print(" read credit information from file ", cred_filename)
    print("="*30)
    client, conf=pik.client_from_credit(cred_filename, proxy=None)
    if not client:
        user=input("输入用户名: ")
        passwd=input("输入密码: ")
        proxy=input("HTTP代理: ")
        #credfilename=input("保存的文件名: ")
        client, conf=pik.client_from_password(user, passwd, cred_filename, proxy)
    if not client:
        print("登录无效")
        exit()
    #client=pik.create_client(cred_filename, config.user, config.passwd, proxy=None)
    print(json.dumps(client.get_user_info(), indent=4))
    print("=" * 30, end="\n\n")

    curdir='' # current directory
    while True:
        command=input("input COMMAND (exit to quit): ")
        print("=" * 30, end="\n\n")
        if not command: # 输入为空
            continue
        if command=='exit':
            break
        #re.split('\s+', s)
        cmds=command.split(maxsplit=1) # into max two parts
        command=cmds[0]
        param=cmds[1:]
        if param:
            param=param[0]
        else:
            param=''
        if command in cmd.cmds:
            cmd.cmds[command](client, param)



def download_file(fileid):
    files=client.get_download_url(fileid)
    print("link: ", files['web_content_link'])
    print("filename: ", files['name'])
    print("size: ", files['size'])
    print("="*30)
    with open("down.bash", "w") as f:
        f.write("#!/bin/bash\n")
        f.write("# download by weget\n")
        f.write(f"\nwget -O \"{files['name']}\" \"{files['web_content_link']}\"")
        f.write("\n")
    print(f"usage: . down.bash\n")

