import csv
import json

INPUT_CSV = "妙法守護碑.csv"
OUTPUT_GEOJSON = "妙法守護碑.geojson"

features = []

with open(INPUT_CSV, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            lat = float(row["緯度"])
            lon = float(row["経度"])
        except (ValueError, KeyError):
            # 緯度・経度が無効ならスキップ
            continue

        if row["分類"] not in ["狭義", "広義"]:
            # 狭義と広義以外（保留と未定義）はスキップ
            continue

        properties = {k: v for k, v in row.items() if k not in ["緯度", "経度"]}

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]  # GeoJSONは [経度, 緯度]
            },
            "properties": properties
        }
        features.append(feature)

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open(OUTPUT_GEOJSON, "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2)
