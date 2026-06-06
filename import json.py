import json

# 读取已转换的 WGS84 JSON
with open('Data/xuhuiqu/xuhui_poi_wgs84.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 转换为 GeoJSON 格式
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [p['wgs84']['lng'], p['wgs84']['lat']]
            },
            "properties": {
                "name": p['name'],
                "category": p['category'],
                "address": p['address']
            }
        } for p in data['points']
    ]
}

# 保存为固化文件
with open('Data/xuhuiqu/xuhui_poi_fixed.geojson', 'w', encoding='utf-8') as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2)

print("位置已固化为 GeoJSON 文件，可直接用于 GIS 软件导出 SHP。")