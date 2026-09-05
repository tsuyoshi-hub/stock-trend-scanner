from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>上昇初動スキャナー</title>
<style>
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;margin:0;background:#f5f6f8;color:#222}
main{max-width:900px;margin:auto;padding:20px}
h1{font-size:26px}.card{background:white;border-radius:14px;padding:18px;margin:14px 0;box-shadow:0 1px 5px #ddd}
.note{color:#666;line-height:1.7}.tabs{display:flex;gap:8px;flex-wrap:wrap}
button{border:0;border-radius:9px;padding:10px 13px;background:#222;color:white;font-weight:700}
</style>
</head>
<body><main>
<h1>📈 上昇初動スキャナー</h1>
<div class="card">
  <b>上がり始め × 出来高増加 × 過熱除外</b>
  <p class="note">日本株の「上昇初動」を探すためのスキャナーです。</p>
  <div class="tabs">
    <button>新規初動</button><button>初動点</button><button>出来高</button><button>高値突破</button>
  </div>
</div>
<div class="card">
  <h2>Render接続テスト</h2>
  <p>アプリは正常に起動しています。</p>
  <p class="note">まずRenderへの公開を完成させ、その後に実際の日本株データ取得とExcelデータ連携を追加します。</p>
</div>
</main></body></html>
"""

@app.get("/")
def home():
    return render_template_string(HTML)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
