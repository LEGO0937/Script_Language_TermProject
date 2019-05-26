#병원정보 서비스 예제
#http://apis.data.go.kr/B551182/hospInfoService/getHospBasisList?serviceKey=sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D&pageNo=1&numOfRows=10&sidoCd=110000&sgguCd=110019
import urllib
import http.client
import urllib.parse
import bs4
import json
from xml.etree import ElementTree


str = "서울특별시"
str1 = "종로구"




conn = http.client.HTTPConnection("openapi.tour.go.kr")
URL = "/openapi/service/TourismResourceService/getTourResourceList?serviceKey=cCHEHEp%2BWRwV%2FfoF1u%2FVeQGoxigy9y%2FrGH8XHy3oN11YntHkyn3zf8fpQiLDIKWuVY6qT9MUkLU8yQ1naKv%2BFw%3D%3D&SIDO=base&GUNGU=sub"
URL = URL.replace("base",urllib.parse.quote('서울특별시'))
URL = URL.replace("sub",urllib.parse.quote('종로구'))
conn.request("GET",URL)
req = conn.getresponse()
#print(req.read().decode("UTF-8"))
# print(bs4.BeautifulSoup(req.read().decode("UTF-8")))
# print(bs4.BeautifulSoup(req.read()))


tree = ElementTree.fromstring(req.read().decode("UTF-8"))
itemElements = tree.getiterator("item")  # item 엘리먼트 리스트 추출
for item in itemElements:
    result = item.find('ASctnNm')
    print(result.text)
    result = item.find('BResNm')
    print(result.text)
    result = item.find('CSido')
    print(result.text)
    result = item.find('DGungu')
    print(result.text)
    result = item.find('EPreSimpleDesc')
    if result != None:
        print(result.text)

    print("\n\n")
print(result)




