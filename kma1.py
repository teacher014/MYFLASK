from urllib import request
from bs4 import BeautifulSoup

# https://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp
# 1. 경상남북도 중기 예보 url 변경
target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159")

# BeautifulSoup을 사용해 웹 페이지를 분석합니다.
soup = BeautifulSoup(target, "html.parser")

with open(file="k-weather1.xml", mode="a") as urlPage:
    urlPage.write("{}".format(soup))

# 2. 추가 title, wf, province 태그, 
print(soup.select_one("title").string)
print(soup.select_one("wf").string)
print("지역:", soup.select_one("province").string)
print()

# 3. location 태그를 찾습니다. + 날짜
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx, tmEf 태그를 찾아 출력합니다.
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()

print("날짜:", location.select_one("tmEf").string)