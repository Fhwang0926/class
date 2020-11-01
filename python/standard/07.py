#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926

# 다른 파일의 내용 참조
from module_07 import test

# class 불러오기
        
# test 클래스로 instance 객제 생성
instance = test()
getname = instance.main()
print('class getname', getname)

import module_07

# class 불러오기
        
# test 클래스로 instance 객제 생성
instance = module_07.test()
getname = instance.main()
print('class getname', getname)

# 여기서 module_07.pyc 파일이 생길 수 있는데 미리 컴파일한 파일
# 속도 향상을 위해 (씨언어의 전처리 와 비슷)