import requests  # request is a tool to get Data from internet
City = input(" Enter the location : ").strip().title()

# get coordinates 
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={City}"
geo_response = requests.get(geo_url)
geo_data= geo_response.json()
# print(geo_data)
results = geo_data.get("results")
# check results 
if results:
    print("\nSelect the correct location:\n")

    for i,place in enumerate(results):
        print(i,place["name"],"-", place.get("admin1"),"-",place.get("country"))
        
    choice=int(input("\n Enter number:\n")) 
    selected_city = results[choice]

    latitude = selected_city["latitude"]
    longitude = selected_city["longitude"]


    # weather Api 
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()  # Converts API data into python dictionary

    current = data["current_weather"]
    print(f"\n Weather Details of {City}: \n")
    print("Current Temperature: ", current["temperature"], "°C")  # dictionary access
    print("windspeed:", current["windspeed"], "km/h")
    print("Wind-direction : ", current["winddirection"])
else:
    print("City not found !")