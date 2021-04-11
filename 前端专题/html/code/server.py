# -*- coding:utf-8 -*-
# author:cdc
# date:2019/12/21

import socket

# 1 创建socket对象
sk = socket.socket()

# 2 绑定一个端口
sk.bind(("127.0.0.1", 8080))

# 3 设置监听，最大的监听对象个数为5个
sk.listen(5)

while True:
    # 等待客户端连接
    conn, addr = sk.accept()
    data = str(conn.recv(9000), encoding="utf-8")
    data_lst_tmp = data.split("\r\n\r\n")
    data_lst = [i for i in data_lst_tmp if i != ""]
    if len(data_lst) != 2:
        pass
    else:
        info = dict()
        info_lst = data_lst[-1].split("&")
        for i in info_lst:
            content = i.split("=")
            info[content[0].strip()] = content[1].strip()
        print(info)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    res = bytes("注册成功", encoding="gbk")
    conn.send(res)
    conn.close()