# -*- coding:utf-8 -*-
import sys
import hashlib

reload(sys)
sys.setdefaultencoding("utf-8")


def md5_32(content):
   m = hashlib.md5()
   m.update(content)
   psw = m.hexdigest()
   return psw


if __name__ == '__main__':
   print md5_32("1234556")





