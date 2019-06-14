#http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceList?ServiceKey=qmAs0ut6m%2BwM%2FJwamfdK8RkKJz5yNmI4VrT6DEUuwmm%2FW7GMClJBCltEmgQEeSo7v1poVh0ZYPSbihUbMftNUQ%3D%3D&SIDO=서울특별시&GUNGU=종로구

import spam




str1 = "http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceList?ServiceKey=qmAs0ut6m%2BwM%2FJwamfdK8RkKJz5yNmI4VrT6DEUuwmm%2FW7GMClJBCltEmgQEeSo7v1poVh0ZYPSbihUbMftNUQ%3D%3D&SIDO="
str2 = "서울특별시"
str3 = "&GUNGU="
str4 = "종로구"
str5 = "&"

print(spam.make_url(str1, str2, str3, str4, str5))