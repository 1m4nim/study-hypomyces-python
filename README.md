# study-hypomyces-python

## 菌類データの地図マッピングプロジェクト

このプロジェクトは、菌類（taxa）データを地図上に可視化するためのPythonコードとJupyter Notebookを管理しています。  

### 今までの試み<br/>
https://github.com/1m4nim/study-hypomyces <br/>
https://github.com/1m4nim/study-hypomyces-react<br/>
---

### 主な内容

- `fungi_data_expanded.csv` に含まれる菌類の `taxa_name` と緯度・経度データを用い、Foliumライブラリで日本周辺の地図上にマーカーをプロットします。  
- マーカーは菌類の種類ごとに色分けされております。  
- Jupyter NotebookをHTMLに変換し、コード部分を非表示にした状態で公開しています。
- 変換後のHTMLファイルはGitHub Pagesでホスティングして公開しています。

---

### 使用技術

- Python 3.12.7 
- Pandas  
- Folium (地図描画)  
- Jupyter Notebook  
- GitHub Pages (静的ウェブホスティング)

---

### セットアップと使い方

#### 環境構築

```bash
python -m venv .venv
source .venv/bin/activate  
pip install pandas folium jupyter
```
### デプロイ
https://study-hypomyces-python.vercel.app/ <br/>
https://1m4nim.github.io/study-hypomyces-python/

