from dotenv import load_dotenv
import os
import requests
import sys

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
if not api_key:
    print("ERROR: No NEWS_API_KEY found in environment variables")
    sys.exit(1)  


url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=5&apiKey={api_key}"


try:
    response = requests.get(url)
    response.raise_for_status()  
except requests.exceptions.RequestException as e:
    print(f"ERROR: Failed to fetch news: {e}")
    sys.exit(1)

try:
    data = response.json()
    articles = data.get("articles", [])
except ValueError as e:
    print(f"ERROR: Failed to parse JSON: {e}")
    sys.exit(1)


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

if not articles:
    html_content += "<li>No articles found.</li>"
else:
    for article in articles:
        title = article.get("title", "No title")
        url_link = article.get("url", "#")
        html_content += f'<li><a href="{url_link}" target="_blank">{title}</a></li>'
