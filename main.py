# Author: Raghavendran Ravichandran
# Date: 2023-06-24
# Version: 1.0
# Description: This is the main file for the weather app

# write doc string for this module
"""This is the main file for the weather app"""


import urllib.request
import requests
import json

# create a python method to read vault.dat
# the method should return a dictionary with the vault data
# the method should return a 404 error if the file is not found


def read_vault():
    # write a doc string for the function below
    """Reads vault.dat and returns the contents as a dictionary"""

    try:
        with open("vault.dat") as f:
            return f.read()
    except FileNotFoundError:
        return {"error": "File not found"}


from fastapi import FastAPI

app = FastAPI()
API_KEY = read_vault()


@app.get("/")
async def root():
    return {"message": "Welcome to the weather app"}  # <generated by cp


# create a fast api function that returns a weather forecast for a city
# the function should take a city name as a parameter
# the function should return a dictionary with the city name and the forecast
# the function should return a 404 error if the city is not found


@app.get("/weather/{countrycode}/{city}")
async def weather(countrycode: str, city: str):

    # write a doc string for the function below
    """Returns the weather forecast for a city"""

    # add if condition to check if city is alpha
    if not city.isalpha():
        return {"error": "Please enter a valid city name"}

    search_address = (
        "http://dataservice.accuweather.com/locations/v1/cities/"
        + countrycode
        + "/search?apikey=XhXAjkKmNAqFLwhGm6LXVrF9auhFFz60"
        + "&q="
        + city
    )
    with urllib.request.urlopen(search_address) as search_address:
        data1 = json.loads(search_address.read().decode())
        key_response = data1[0]["Key"]

    search_city = (
        "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"
        + key_response
        + "?apikey=XhXAjkKmNAqFLwhGm6LXVrF9auhFFz60"
    )

    response = requests.get(search_city)
    data3 = response.text
    data_final = json.loads(data3)["Headline"]["Text"]
    return {"city": city, "forecast": data_final}


# using requests module to make a get request to the weather api
# the api key is stored in vault.dat
# the api key is read from the vault.dat file
# the api key is passed as a parameter to the get request
# the get request returns a json response
# the json response is converted to a dictionary
# the dictionary is returned by the function
