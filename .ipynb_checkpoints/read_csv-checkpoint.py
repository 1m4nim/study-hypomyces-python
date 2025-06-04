import pandas as pd
import csv
import re

# 読み込みと整形処理
cleaned_rows = []
with open("fungi_data_expanded.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    headers = next(reader)
    
    for row in reader:
        if len(row) < 5:
            # カンマのずれを処理
            combined = ",".join(row)
            # パターンマッチでカンマの位置を修正
            match = re.match(r'^(.*?),(.*?),(.*?),(-?\d+\.\d+),(-?\d+\.\d+)$', combined)
            if match:
                cleaned_rows.append(list(match.groups()))
            else:
                print("❌ 修正不能な行:", row)
        else:
            cleaned_rows.append(row)

# DataFrameに変換
df = pd.DataFrame(cleaned_rows, columns=["taxa_name", "hosts", "place", "latitude", "longitude"])

# 括弧やカンマの修正（例: place列の")"削除、"China (Xxx" → "China: Xxx" 等）
df["place"] = df["place"].str.replace(r"[()]", "", regex=True)
df["place"] = df["place"].str.replace(r"China\s+\w+", lambda m: m.group(0).replace("China ", "China: "), regex=True)

# データ型を適切に変換（エラーが出ないように）
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

# 欠損がある行を確認（または削除）
print(df[df.isnull().any(axis=1)])

# 保存（必要に応じて）
df.to_csv("cleaned_data.csv", index=False)
