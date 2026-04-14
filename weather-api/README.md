🌤️ Weather API

A simple REST API built with Python and FastAPI that returns the current
weather for a given city.

The API uses Open-Meteo services: - one request to convert a city name
into coordinates - another request to fetch current weather data

This project was created as a learning project to practice backend
development with Python.

------------------------------------------------------------------------

🚀 Features

-   Get current weather by city name
-   Returns temperature and wind speed
-   Returns country and geographic coordinates
-   Handles city not found errors (404)
-   Handles external API errors (503)
-   Logging for requests and errors
-   Automatic interactive API documentation (Swagger)

------------------------------------------------------------------------

🛠 Tech Stack

-   Python
-   FastAPI
-   Requests
-   Uvicorn

------------------------------------------------------------------------

📁 Project Structure

```
weather-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── services/
│       ├── __init__.py
│       └── weather_service.py
│
├── notebooks/
│   └── test_weather.ipynb
│
├── tests/
│   └── __init__.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

------------------------------------------------------------------------

⚙️ Setup

Create and activate a virtual environment.

Windows

    python -m venv venv
    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------

▶️ Run the server

Start the API server:

    python -m uvicorn app.main:app --reload

Server will run at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

🌍 Example request

GET /weather/Riga

Example response:

    {
      "city": "Riga",
      "country": "Latvia",
      "latitude": 56.946,
      "longitude": 24.10589,
      "time": "2026-04-14T10:15",
      "temperature": 8.0,
      "wind_speed": 12.6
    }

------------------------------------------------------------------------

❗ Error Handling

City not found

    {
      "detail": "City not found"
    }

External API error

    {
      "detail": "Error fetching weather data"
    }

------------------------------------------------------------------------

🔮 Future Improvements

Possible improvements:

-   Add more weather parameters
-   Implement caching
-   Add unit tests
-   Deploy the API online
-   Add a simple frontend

------------------------------------------------------------------------

👨‍💻 Author

Learning backend project built with Python and FastAPI.
