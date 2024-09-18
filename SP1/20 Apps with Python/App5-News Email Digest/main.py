import requests
import send_email

api_key = "8495297b5d0e4e1f94a8dbcb79ba21e5"

topic = "tesla"

url = f"https://newsapi.org/v2/everything?"\
        f"q={topic}&"\
        "from=2024-07-08&"\
        "sortBy=publishedAt&"\
        "apiKey=8495297b5d0e4e1f94a8dbcb79ba21e5&"\
        "language=en"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
# send_email(body)
print(body)