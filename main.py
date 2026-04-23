from datetime import datetime
from jinja2 import Template

# 관심 종목
tickers = ["TSLA", "NVDA", "MSFT", "AMZN"]

events = []

# 1️⃣ 주식 데이터 가져오기
for t in tickers:
    stock = yf.Ticker(t)
    info = stock.info

    price = info.get("regularMarketPrice", "N/A")
    name = info.get("shortName", t)

    events.append({
        "time": datetime.now().strftime("%m/%d %H:%M"),
        "event": f"{name} ({t})",
        "importance": "상",
        "note": f"현재가 ${price}"
    })

# 2️⃣ 이벤트 직접 추가 (핵심)
events.append({
    "time": "04/23 06:00",
    "event": "TSLA Q1 실적",
    "importance": "상",
    "note": "마진 + 로보택시 기대"
})

events.append({
    "time": "04/25 21:30",
    "event": "US Core PCE",
    "importance": "상",
    "note": "FOMC 직전 핵심 인플레"
})

# 3️⃣ HTML 템플릿
html_template = """
<html>
<head>
<meta charset="utf-8">
<style>
body { font-family: Arial; padding: 30px; }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 10px; border-bottom: 1px solid #ddd; }
.high { color: #0ea5a4; font-weight: bold; }
.mid { color: #555; }
</style>
</head>

<body>
<h2>📊 Macro Event Briefing</h2>

<table>
<thead>
<tr>
<th>일시 (KST)</th>
<th>이벤트</th>
<th>민감도</th>
<th>왜 중요한가</th>
</tr>
</thead>

<tbody>
{% for e in events %}
<tr>
<td>{{ e.time }}</td>
<td>{{ e.event }}</td>
<td class="{{ 'high' if e.importance == '상' else 'mid' }}">
{{ e.importance }}
</td>
<td>{{ e.note }}</td>
</tr>
{% endfor %}
</tbody>
</table>

</body>
</html>
"""

# 4️⃣ HTML 생성
template = Template(html_template)
output = template.render(events=events)

# 5️⃣ 파일 저장
with open("briefing.html", "w", encoding="utf-8") as f:
    f.write(output)

print("완료: briefing.html 생성됨")
