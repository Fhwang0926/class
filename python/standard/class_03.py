#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926
import re

try:
    text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
    regex = re.compile("에러 1033")
    mo = regex.search(text)
    if mo != None:
        print("case", mo.group()) 

    # "에러" 문구 관련 
    text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
    regex = re.compile("에러\s\d+")
    mc = regex.findall(text)
    print(mc)
 

    # 정규식을 활용한 연락처 매칭
    text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
    
    regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    matchobj = regex.search(text)
    areaCode = matchobj.group(1)
    num = matchobj.group(2)
    fullNum = matchobj.group()
    print(areaCode, num) # 032 232-3245

    regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    matchobj = regex.search(text)
    phonenumber = matchobj.group()
    print(phonenumber)

    text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
    regex = re.compile("에러 1033")
    mo = regex.search(text)
    if mo != None:
        print(mo.group()) 
    # new regex
    

except Exception as e:
    print(e)
    print('if you have a error, check error msg')
    pass
else:
    print('done 1')
finally:
    print('done 2')
    pass
