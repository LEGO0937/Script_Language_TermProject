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


#http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceDetail?serviceKey=cCHEHEp%2BWRwV%2FfoF1u%2FVeQGoxigy9y%2FrGH8XHy3oN11YntHkyn3zf8fpQiLDIKWuVY6qT9MUkLU8yQ1naKv%2BFw%3D%3D&SIDO=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&GUNGU=%EC%A2%85%EB%A1%9C%EA%B5%AC&RES_NM=%EA%B2%BD%EB%B3%B5%EA%B6%81


conn = http.client.HTTPConnection("openapi.tour.go.kr")
URL = "/openapi/service/TourismResourceService/getTourResourceDetail?serviceKey=cCHEHEp%2BWRwV%2FfoF1u%2FVeQGoxigy9y%2FrGH8XHy3oN11YntHkyn3zf8fpQiLDIKWuVY6qT9MUkLU8yQ1naKv%2BFw%3D%3D&SIDO=base&GUNGU=sub&RES_NM=name"
URL = URL.replace("base",urllib.parse.quote('서울특별시'))
URL = URL.replace("sub",urllib.parse.quote('종로구'))
URL = URL.replace("name",urllib.parse.quote('경복궁'))
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
    result = item.find('FSimpleDesc')
    if result != None:
        print(result.text)
    result = item.find('HEnglishNm')
    print(result.text)
    result = item.find('KPhone')
    print(result.text)

    print("\n\n")


print(result)




