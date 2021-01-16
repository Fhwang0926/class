#!/usr/bin/python // 파이썬을 위한 파일임을 선언
# -*- coding: utf8 -*- // 인코딩 방식 지정 => 한글 주석으로 인한 실행 에러 방지
import time

class kakao:
  
  price = 5000
  count = 0

  def __init__(self):
    print("주식 시장 개장, 총 주식 수 : {0}, 현재가격 : {1}".format(self.price, self.count))
  
  def __del__(self):
    print("주식 시장 종장, 총 주식 수 : {0}, 현재가격 : {1}".format(self.price, self.count))
  
  def buy(self, cnt=0):
    time.sleep(3)
    print("{0} 판매가 체결되었습니다 ".format(cnt))
    self.count -= cnt
    
  
  def sell(self, cnt=0):
    time.sleep(3)
    print("{0} 구매가 체결되었습니다 ".format(cnt))
    self.count += cnt

  def status(self):
    print("은행 보유 주식 수: {0}".format(self.count))

if __name__ == "__main__":
  print("카카오 주식 샘플 시작")
  stock = kakao()
  stock.buy(10)
  stock.status()
  stock.sell(15)
  stock.status()
  del stock