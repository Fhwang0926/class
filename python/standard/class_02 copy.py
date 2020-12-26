#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926

try:
    f = open('./apache_access.log', 'r')
    f_new = open('./apache_access_new.log', 'w')
    lines = f.readlines()
    for line in lines:
        print(line)
        print('parser 1')
        row = line.split(' ')
        print(row)
        print('parser 2')
        new_data = "[{0}] => {1}, Result : {2}".format(row[0], row[5], row[8]) 
        print(new_data)
        print('parser 3')
        new_data = new_data.replace('"', '')
        print(new_data)
        f_new.write(new_data+"\n")
        pass
    f.close()
    f_new.close()
except Exception as e:
    print(e)
    print('if you have a error, check error msg')
    pass
else:
    print('done 1')
finally:
    print('done 2')
    pass
