import requests
import json
import img

city ="viena"
apikey = "?"   
lang = "kr"
units = "metric" 

api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}"

result = requests.get(api)

data = json.loads(result.text)

# 날씨 상태 확인
weather_status = data['weather'][0]['id']

# 날씨 상태에 따라 이미지 선택
if weather_status in [800]:
    image_path = 'img/clear kyeongbok.mp4'
        
elif weather_status in[801,802,803,804,701,711,721,731,741]:
    image_path = 'img/foggy kyeongbok.mp4'  # 구름,흐린,안개 날씨 이미지

elif weather_status in [771,781,300,301,302,310,311,312,313,314,321,500,501,502,503,504,511,520,521,522,531,701,200,201,202,210,211,212,221,230,231,232]:
    image_path = 'img/rain kyeongbok.mp4'  # 뇌우 날씨 이미지

elif weather_status in[600,601,602,611,612,613,615,616,620,621,622]:
    image_path = 'img/snow kyeongbok.mp4'  # 눈 오는 날씨 이미지

elif weather_status in[761,762]:
    image_path = 'img/dust kyeongbok.mp4'  # 먼지 날씨 이미지

elif weather_status in [751]:
    image_path = 'img/sandstorm kyeongbok.mp4'  # 황사 날씨 이미지

else:
    image_path = 'img/clear kyeongbok.mp4'  # 기본 이미지

print(weather_status)