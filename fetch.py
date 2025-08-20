from dotenv import load_dotenv
import os
import requests

load_dotenv()  # will read .env if it exists

api_key = os.getenv("NEWS_API_KEY")
if not api_key:
    raise ValueError("No NEWS_API_KEY found in environment variables")


url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=5&apiKey={api_key}"

response = requests.get(url)
data = response.json()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Latest News</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
<h1>Top 5 News Headlines</h1>
<ul>
"""

for article in data['articles']:
    html_content += f'<li><a href="{article["url"]}" target="_blank">{article["title"]}</a></li>'

html_content += "</ul></body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html generated successfully!")
