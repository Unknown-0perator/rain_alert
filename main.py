import requests
from twilio.rest import Client

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
MY_KEY = 'be55dec7f5afa5f6be6c0a67f800177a'
LAT = 49.191345
LONG = -122.849014
# Your Account SID from twilio.com/console
account_sid = "Your Account SID"
# Your Auth Token from twilio.com/console
auth_token  = "Your Auth Token"
parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': MY_KEY,
    'exclude': 'current,minutely,daily,alerts'
}
response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="Your verified number",
        from_="Twilio phone number",
        body="It is raining out there, bring your umbrella")

print(message.status)
