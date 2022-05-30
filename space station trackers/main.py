import json
import urllib.request
import time
import turtle
import webbrowser
import geocoder 

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("there are currently" + str(result["number"]) + "astronauts on board on the ISS: \n\n")
people = result["people"]
for p in people:
    file.write(p['name'] + " -- on board" + '\n' )

g = geocoder.ip('me')
file.write("\n\nyour current longitude and latitude is" + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

screen = turtle.Screen()
screen.setup(1280, 640)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic("earth-g24808a477_1280.gif")
screen.register_shape("international-space-station-icon.gif")
iss = turtle.Turtle()
iss.shape("international-space-station-icon.gif")
iss.setheading(45)
iss.penup()


while True:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result["iss_position"]
    latitude = location["latitude"]
    longitude = location["longitude"]

    latitude = float(latitude)
    longitude = float(longitude)
    print(f"\nlatitude: {str(latitude)}")
    print(f"\nlongitude: {str(longitude)}")
    iss.goto(longitude, latitude)
    time.sleep(5)