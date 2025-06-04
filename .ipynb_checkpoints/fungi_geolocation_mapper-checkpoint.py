import json
import csv
import time
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_fungi_mapper")

with open('fungi_data.json', 'r', encoding='utf-8') as f:
    fungi_data = json.load(f)

for item in fungi_data:
    for host_info in item["hosts"]:
        distribution = host_info.get("distribution")
        if not distribution:
            host_info["coordinates"] = []
            continue
        
        places = [place.strip() for place in distribution.split(',')]
        coords_list = []
        for place in places:
            for attempt in range(3):
                try:
                    loc = geolocator.geocode(place, timeout=10)
                    if loc:
                        coords_list.append({"place": place, "latitude": loc.latitude, "longitude": loc.longitude})
                    else:
                        coords_list.append({"place": place, "latitude": None, "longitude": None})
                    break
                except Exception as e:
                    print(f"{place}: エラー（{e}）でリトライ中...")
                    time.sleep(2)
            time.sleep(1)
        host_info["coordinates"] = coords_list

# JSONに緯度経度情報を含めて保存
with open('fungi_data_with_coords.json', 'w', encoding='utf-8') as f:
    json.dump(fungi_data, f, ensure_ascii=False, indent=2)

# CSVは場所ごとに1行ずつ出力
with open('fungi_data_expanded.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["taxa_name", "hosts", "place", "latitude", "longitude"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in fungi_data:
        for host_info in item["hosts"]:
            for coord in host_info.get("coordinates", []):
                writer.writerow({
                    "taxa_name": item["taxa_name"],
                    "hosts": host_info.get("hosts", ""),
                    "place": coord["place"],
                    "latitude": coord["latitude"],
                    "longitude": coord["longitude"],
                })

print("✅ 複数場所の緯度経度取得＆CSV出力が完了しました。")
