#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926

# function
# 정의
def main(name="default"):
    print("main", main, name)
    return name

# class
# 정의
class test:
    # self 가 명시적으로 필요, 그래야 test 에서 참조
    def main(self, name="default"):
        print("main", main, name)
        return name
        
# test 클래스로 instance 객제 생성
instance = test()
getname = instance.main()
print('class getname', getname)