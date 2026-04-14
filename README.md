# 🐍 Python Mini Projects & Tools

This repository includes a collection of small yet educational Python projects and system tools developed during my learning journey. Each file demonstrates different aspects of Python programming, from game logic and data visualization to system health checks.

---

# 🌐 Backend / API Projects

### Weather API
### [`weather-api`](https://github.com/ArtuursG/Python/tree/main/weather-api)

A simple REST API built with **FastAPI** that retrieves current weather data for a given city.

The API works by:

1. Converting a city name into geographic coordinates using the **Open-Meteo Geocoding API**
2. Fetching real-time weather information using the **Open-Meteo Forecast API**

Features:

- FastAPI backend
- external API integration
- error handling
- logging
- Swagger API documentation (`/docs`)
- clean project structure

Example endpoint:

GET /weather/Riga

Example response:

{
  "city": "Riga",
  "country": "Latvia",
  "latitude": 56.95,
  "longitude": 24.10,
  "temperature": 8.0,
  "wind_speed": 12.6
}

---

## 🎮 Games

### [`guess_the_number.py`](https://github.com/ArtuursG/Python/blob/main/Number_guess/guess_the_number.py)
A console-based number guessing game where the user has 6 attempts to guess a random number between 1 and 20.

### [`BMW_quiz.py`](https://github.com/ArtuursG/Python/blob/main/Quiz/BMW_quiz.py)
A BMW-themed quiz game with 7 multiple-choice questions. It tracks lives, calculates scores, and saves the result to a file.

---

## 🌍 Data Visualization

### [`covid-map.ipynb`](https://github.com/ArtuursG/Python/tree/main/covid-map)
A Jupyter Notebook that visualizes global COVID-19 case data using `folium` and `pandas`. It includes:
- Choropleth maps
- Circle markers with confirmed/recovered counts
- Heat maps for death toll intensity

Data is fetched from the [COVID-19 API](https://api.covid19api.com/) and enriched with country coordinates.

---

## 🛠️ System Health Tools

### [`all_checks.py`](https://github.com/ArtuursG/Python/blob/main/pc-health-check/all_checks.py) & [`all_checks2.py`](https://github.com/ArtuursG/Python/blob/main/pc-health-check/all_checks2.py)
Scripts to verify basic system health:
- Checks if a system reboot is required
- Verifies root partition disk space

### [`disk_usage.py`](https://github.com/ArtuursG/Python/blob/main/pc-health-check/disk_usage.py)
Checks if a disk has enough free space (at least 2 GB or 10%).

---

## 📁 File Overview
```
guess_the_number.py
BMW_quiz.py
covid-map.ipynb
all_checks.py
all_checks2.py
disk_usage.py
```

---

## 🧑‍🎓 About
These projects reflect my growth as a student diving deeper into Python development, systems programming, and data visualization.
