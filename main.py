#Creating a weather/rain notifier app, that sends out an email

import requests
import smtplib
import os
from twilio.rest import Client

#use this online tool: https://jsonviewer.stack.hu/

#32.742,-81.688  Sylvania, GA
#Wheaton, GA 41.864725, -88.111311


API_KEY = os.environ.get("API_KEY")
MY_LAT = 41.864725 # Your latitude
MY_LONG = -88.111311  # Your longitude
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
COUNT = 4
#https://api.openweathermap.org/data/2.5/forecast?lat=40.417286&lon=-82.907120&appid=f4924e152cf51d60bd124b355ea3aae6


#constants for email generation
GMAIL = "smtp.gmail.com"
HOTMAIL = "smtp.live.com"
YAHOO = "smtp.mail.yahoo.com"
my_email = os.environ.get("MY_EMAIL1")
password = os.environ.get("MY_EMAIL1_PASSWORD")
yahoo = os.environ.get("YAHOO_EMAIL")


parameters ={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": COUNT
}
print("API KEY")
print(API_KEY)
response = requests.get(url=API_ENDPOINT,params=parameters)
response.raise_for_status() #if there is a problem, we should catch those too.
print(response.status_code)
weather_data = response.json()

# print(weather_data)
# print(type(weather_data))
# print(weather_data.keys())


will_rain = False
for item in weather_data['list']:
    condition_code = (item['weather'][0]['id'])
    if condition_code < 700:
        will_rain = True
        print(condition_code)
    else:
        print(condition_code)

if will_rain:
    #print("Bring umbrella")
    with smtplib.SMTP(GMAIL) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=yahoo,
                            msg=f"Subject: Rain Notifier\n\nThe weather shows rain for today, please bring an umbrella")


    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     from_= '+17372324091',
    #     body= "It's going to rain, bring an umbrella",
    #     to= '+12832126918'
    # )
    # print(message.status)


# message = client.messages.create(
#   from_="whatsapp:TWILIO_WHATSAPP_NUMBER",
#   body="It's going to rain today. Remember to bring an umbrella",
#   to="whatsapp:YOUR_TWILIO_VERIFIED_NUMBER"
# )

