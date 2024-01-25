import argparse

import json

with open('config.json') as config_file:
    config = json.load(config_file)

import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from flask import Flask
from flask_mail import Mail, Message

from dotenv import load_dotenv
import os

app = Flask(__name__)
mail= Mail(app)
load_dotenv()
emailpw = os.getenv('GMAIL_PW')
news_api_key = os.getenv('THE_NEWS_API')
weather_api_key = os.getenv('OPEN_WEATHER_API')

news_url = f"https://api.thenewsapi.com/v1/news/top?locale=us&language=en&api_token={news_api_key}"

news_response = requests.get(news_url)
news_data = news_response.json()

weather_api_key = config['OPEN_WEATHER_API']
weather_url = f"https://api.openweathermap.org/data/2.5/forecast?lat=42.2206977&lon=-71.6442671&appid={weather_api_key}"
weather_response = requests.get(weather_url)
weather_data = weather_response.json()
current_temp = weather_data['list'][0]['main']['temp']
current_temp = round((current_temp - 273.15) * 9/5 + 32)
current_weather = weather_data['list'][0]['weather'][0]['main']
current_weather_description = weather_data['list'][0]['weather'][0]['description']
current_weather_icon = weather_data['list'][0]['weather'][0]['icon']
current_weather_icon_url = f"http://openweathermap.org/img/w/{current_weather_icon}.png"
three_hour_temp = weather_data['list'][1]['main']['temp']
three_hour_temp = round((three_hour_temp - 273.15) * 9/5 + 32)
three_hour_weather = weather_data['list'][1]['weather'][0]['main']
three_hour_weather_description = weather_data['list'][1]['weather'][0]['description']
three_hour_weather_icon = weather_data['list'][1]['weather'][0]['icon']
three_hour_weather_icon_url = f"http://openweathermap.org/img/w/{three_hour_weather_icon}.png"
six_hour_temp = weather_data['list'][2]['main']['temp']
six_hour_temp = round((six_hour_temp - 273.15) * 9/5 + 32)
six_hour_weather = weather_data['list'][2]['weather'][0]['main']
six_hour_weather_description = weather_data['list'][2]['weather'][0]['description']
six_hour_weather_icon = weather_data['list'][2]['weather'][0]['icon']
six_hour_weather_icon_url = f"http://openweathermap.org/img/w/{six_hour_weather_icon}.png"
five_day_weather = []
for i in range(0, 40, 8):
    five_day_weather.append(weather_data['list'][i]['weather'][0]['main'])
five_day_weather_description = []
for i in range(0, 40, 8):
    five_day_weather_description.append(weather_data['list'][i]['weather'][0]['description'])
    

email_body = ""
for article in news_data['data']:
   email_body += f"Title: {article['title']}\n"
   email_body += f"Description: {article['description']}\n"
   email_body += f"URL: {article['url']}\n\n"
   email_body += "--------------------------------------\n\n"

email_body += f"""
Current Temp: {current_temp}°F<br>
Current Weather: {current_weather}<br>
Current Weather Description: {current_weather_description}<br>
<img src='{current_weather_icon_url}' alt='Weather icon'><br>
3 Hour Temp: {three_hour_temp}°F<br>
3 Hour Weather: {three_hour_weather}<br>
3 Hour Weather Description: {three_hour_weather_description}<br>
<img src='{three_hour_weather_icon_url}' alt='Weather icon'><br>
6 Hour Temp: {six_hour_temp}°F<br>
6 Hour Weather: {six_hour_weather}<br>
6 Hour Weather Description: {six_hour_weather_description}<br>
<img src='{six_hour_weather_icon_url}' alt='Weather icon'><br>
5 Day Weather: {five_day_weather}<br>
5 Day Weather Description: {five_day_weather_description}<br>
"""
   
email = 'kgsender1@gmail.com'
password = os.getenv('GMAIL_PW')
to_email = 'dudeguykid@gmail.com'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = to_email
msg['Subject'] = 'Good Morning'
body = email_body
msg.attach(MIMEText(email_body, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string().encode('utf-8')
server.sendmail(email, to_email, text)
server.quit()
print('Email sent')

if __name__ == '__main__':
   app.run(debug = True)


