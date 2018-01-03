#! ~/usr/bin/env python
# coding=utf-8

import socket

s= socket.socket();
host = socket.gethostname();
port = 12345;
s.bind((host,port));
s.listen(5);
print "accepting。。。";
c,addr = s.accept();
print "address",addr;
c.send("welcome");
c.close();

