from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="my_geocoder")

places = ["Anhui, China",  
"Fujian, China"  ,
"Guangxi, China " ,
"Hainan, China"  ,
"Hebei, China"  ,
"Hunan, China",  
"Jiangsu, China"  ,
"Jiangxi, China"  ,
"Shanghai, China" , 
"Sichuan, China"  ,
"Zhejiang, China"  ,
"Taiwan, China"  ,
"Tibet, China"  ,
"Inner Mongolia China",  
"Guizhou, China  ",
"Jilin, China"  ,
"Guangdong, China",  
"Gansu, China"  ,
"Hubei, China" ,
"Beijing, China",
"Japan",
"USA",
"Canada",
"Russia",
"Brazil",
"Europe",
"Mexico",
"Cuba",
"Estonia",
"Finland",
"The Netherlands",
"Gabon",
"Iran",
"Korea",
"Indonesia",
"New Zealand",
]

for place in places:
    for attempt in range(3):  # 最大3回トライ
        try:
            location = geolocator.geocode(place, timeout=10)
            if location:
                print(f"{place}: 緯度 = {location.latitude}, 経度 = {location.longitude}")
            else:
                print(f"{place}: 位置が見つかりませんでした")
            break  # 成功したらループを抜ける
        except Exception as e:
            print(f"{place}: 取得失敗 (試行 {attempt+1}/3), エラー: {e}")
            time.sleep(2)
    time.sleep(1)
