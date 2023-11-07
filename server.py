#!
# -*- coding:utf-8 -*-
import multiprocessing
import socket as s
# import socketserver as ss
from multiprocessing import Process
import sys


def recv_send(TcpConnect):
    while True:
        try:
            request = TcpConnect.recv(1024)
        except ConnectionResetError:
            TcpConnect.close()
            break


# 创建 socket 对象
TcpServer = s.socket(
    s.AF_INET,
    s.SOCK_STREAM
)

# 绑定端口号
TcpServer.bind(('127.0.0.1', 65500))
# 最大连接数,超过后排队
TcpServer.listen(10)

if __name__ == '__main__':
    while True:
        try:
            # 建立客户端连接
            TcpConnect, addr = TcpServer.accept()
            p = multiprocessing.Process()
            print(f"add: {str(addr)}")
            msg = 'coonected' + "\r\n"
            TcpConnect.send(msg.encode('utf-8'))
            TcpConnect.close()

        except KeyboardInterrupt:
            sys.exit(0)
