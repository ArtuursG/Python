from fastapi import FastAPI
from .services.weather_service import get_weather_by_city

app = FastAPI()


@app.get(
    "/weather/{city}",
    summary="Get current weather by city",
    description="Returns the current temperature and wind speed for a given city.",
)
def read_weather(city: str):
    return get_weather_by_city(city)


@app.get("/")
def default_msg():
    return {
        "message": "Welcome to the Weather API! Use /weather/{city} to get the current weather for a specific city."
    }