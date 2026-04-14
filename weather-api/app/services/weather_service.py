import logging

import requests
from fastapi import HTTPException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_weather_by_city(city: str) -> dict:
    logger.info("Weather request received for city: %s", city)

    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
    geocoding_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    try:
        response = requests.get(geocoding_url, params=geocoding_params, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        logger.error("Failed to fetch city data from geocoding API")
        raise HTTPException(status_code=503, detail="Error fetching city data")

    geocoding_data = response.json()

    if "results" not in geocoding_data or not geocoding_data["results"]:
        logger.warning("City not found: %s", city)
        raise HTTPException(status_code=404, detail="City not found")

    city_data = geocoding_data["results"][0]
    country = city_data["country"]
    latitude = city_data["latitude"]
    longitude = city_data["longitude"]

    logger.info("Coordinates for %s: %s, %s", city, latitude, longitude)

    forecast_url = "https://api.open-meteo.com/v1/forecast"
    forecast_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
    }

    try:
        weather_response = requests.get(
            forecast_url,
            params=forecast_params,
            timeout=5,
        )
        weather_response.raise_for_status()
    except requests.RequestException:
        logger.error("Failed to fetch weather data")
        raise HTTPException(status_code=503, detail="Error fetching weather data")

    weather_data = weather_response.json()
    current = weather_data["current"]

    temperature = current["temperature_2m"]
    wind_speed = current["wind_speed_10m"]
    time = current["time"]

    logger.info(
        "Weather for %s: temp=%s, wind=%s",
        city,
        temperature,
        wind_speed,
    )

    return {
        "city": city,
        "country": country,
        "latitude": latitude,
        "longitude": longitude,
        "time": time,
        "temperature": temperature,
        "wind_speed": wind_speed,
    }