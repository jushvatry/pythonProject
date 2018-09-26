from socket import socket 
import os,sys
import time 



#基本文件操作功能
class FtpClient(object):
    def __init__(self,s):
        self.s = s

    def do_list(self):
        self.s.send(b'L')
        print('L已发送')
        data = self.s.recv(1024).decode()
        if data == 'OK':
            data = self.s.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
        else:
            print(data)

    def do_get(self,filename):
        self.s.send(('G '+ filename).encode())
        data = self.s.recv(1024).decode()
        print(data)
        if data == 'OK':
            fd = open(filename,'wb')
            while True:
                data = self.s.recv(1024)
                if data == b'##':
                    break
                fd.write(data)

    def do_put(self,filename):
        # if filename not in os.listdir(FILE_PATH):
        #     print("文件不存在，重新输入")
        #     return
        self.s.send(('P '+filename).encode())
        data =self.s.recv(1024).decode()
        print(data)
        if data == 'OK':
            fd = open(filename,'rb')
            print(2)
            while True:
                data = fd.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.s.send(b'##')
                    
                    break
                self.s.send(data)
            fd.close()


                    
def main():
    if len(sys.argv)<3:
        print("argv is error")
        return 
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    

    s = socket()
    try:
        s.connect(ADDR)
    except :
        print("连接服务器失败")
        return

    ftp = FtpClient(s)
    while True:
        print("==========命令选项==========")
        print("***********list************")
        print("**********download*********")
        print("***********put*************")
        print("***********quit************")

        cmd = input("请输入命令>>")
        if cmd.strip() == 'list':
            print('list')
            ftp.do_list()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            print("开始执行do_get")
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(' ')[-1]
            print("开始执行do_put")
            ftp.do_put(filename)
            
        else:
            print("请输入正确命令：")
            continue





if __name__ == "__main__":
    main()
