#! ~/usr/bin/env python
# coding=utf-8


import socket

s=socket.socket();
host=socket.gethostname();
port=12345;
print "connecting...";
s.connect((host,port));
print s.recv(1024);
s.close();
