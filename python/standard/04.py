#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926
import time
whatever = [1, 2, 3]

# 1. list

print(whatever[0])
print(whatever[1:2])
whatever.append(4)
print(whatever)


dd = whatever + [5]
print('dd', dd)
dd.remove(4)
print('dd', dd)