import requests
import selectorlib
import smtplib, ssl
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"

connection = sqlite3.connect("data.db")


def scrape(url):
    request = requests.get(url)
    source = request.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extractor.yaml")
    data = extractor.extract(source)["tours"]
    return data

def read(extracted):
    row = extracted.split(",")
    row = [i.strip() for i in row]
    band, city, date = row
    cursor = connection.cursor("SELECT * FROM events WHERE band = ? AND city = ? AND date = ?", (band, city, date))
    rows = cursor.fetchall()
    return rows

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ammadali1234@gmail.com"
    password = "kyptsctmkbetsdyu"

    receiver = "ammadali1234@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username,password)
        server.sendmail(username, receiver, message)
    print("Email sent successfully")

def store(extracted):
    rows = extracted.split(",")
    rows = [i.strip() for i in rows]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events (band, city, date) VALUES (?, ?, ?)", rows)
    connection.commit()

if __name__ == "__main__":
    while True:
        source = scrape(URL)
        data = extract(source) 
        if data != "No upcoming tours":
            row = read(data)
            if not row:
                store(data) 
                send_email(message="New Event was Found!") 
        time.sleep(2)