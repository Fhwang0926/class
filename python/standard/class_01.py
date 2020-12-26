#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926



try:
    print(a)
except Exception as e:
    print(e)
    pass
finally:
    print("개발자가 잘못 했네")
a = 10
print(a)