import requests
import pprint

# 검색할 주소
location = '서현동'

# 요청 주소(구글맵)

# Local(테스트) 환경 - https 요청이 필요없고, API Key가 따로 필요하지 않지만 횟수에 제약이 있습니다.
URL = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address={}' \
.format(location)

# Production(실제 서비스) 환경 - https 요청이 필수이고, API Key 발급(사용설정) 및 과금 설정이 반드시 필요합니다.
URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=<구글 맵 API key>' \
'&sensor=false&language=ko&address={}'.format(location)

# URL로 보낸 Requst의 Response를 response 변수에 할당
response = requests.get(URL)

# JSON 파싱
data = response.json()

# lat, lon 추출
lat = data['results'][0]['geometry']['location']['lat']
lng = data['results'][0]['geometry']['location']['lng']

# print() 함수 대신 pprint.pprint() 함수를 사용하는 이유는 좀 더 보기 쉽게 출력하기 위함입니다.
pprint.pprint(data)