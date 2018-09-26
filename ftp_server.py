'''
ftp文件服务器
'''

from socket import *
import os,sys
import time 
import signal


FILE_PATH = '/home/tarena/图片/'
HOST = ''
PORT = 8888
ADDR = (HOST,PORT)

#将文件服务器功能写在类中
class FtpServer(object):
    def __init__(self,c):
        self.c = c
    def do_list(self):
        file_list = os.listdir(FILE_PATH)
        print(file_list)

        if not file_list:
            self.c.send("文件库为空".encode())
            return 
        else:
            self.c.send(b'OK')
            time.sleep(0.1)
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile:
                files = files + file + '#'
        self.c.send(files.encode())

    def do_get(self,filename):
        try:
            fd = open(FILE_PATH + filename,'rb')
            print('已找到文件，发送ok')
        except:
            self.c.send("文件不存在".encode())
            return
        self.c.send('OK'.encode())

        time.sleep(0.1)
        while True:
            data = fd.read(1024)
            
            if not data:
                time.sleep(0.1)
                self.c.send('##'.encode())
                fd.close()
                break
            self.c.send(data)
    def do_put(self,filename):
        self.c.send(b'OK')
        fd = open(FILE_PATH + filename,'wb')
        print(1)
        while True:
            data = self.c.recv(1024)
            if data == b'##':
                
                break
            fd.write(data)
        fd.close()






#创建套接字，接收客户端连接，创建新的进程
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print('listen the port 8888')

    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        print("已连接客户端", addr)

        pid = os.fork()

        if pid == 0:
            ftp = FtpServer(c)
            s.close()
            while True:
                data = c.recv(1024).decode()
                print(data)
                if not data:
                    c.close()
                    sys.exit("客户端退出")
                elif data[0] == 'L':
                    ftp.do_list()
                    
                elif data[0] == 'G':
                    print("shoudaol")
                    filename = data.split(' ')[-1]
                    ftp.do_get(filename)
                elif data[0] == 'P':
                    print("shoudaol")
                    filename = data.split(' ')[-1]
                    ftp.do_put(filename)
                    

        else:
            c.close()
            continue


if __name__ == "__main__":
    main()
