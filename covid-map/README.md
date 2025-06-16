# 🌍 COVID-19 Global Geovisualization

This project visualizes global COVID-19 data on an interactive world map using **Python**, **Folium**, and data from the [COVID-19 API](https://api.covid19api.com/). It includes a **Choropleth map**, **circular markers**, and a **heatmap** showing confirmed cases, recoveries, and deaths across different countries.

## 📌 Features

- 📊 Pulls real-time COVID-19 statistics from an API
- 🗺️ Generates interactive maps with:
  - Choropleth color shading by confirmed cases
  - Circle markers showing total confirmed and recovered cases
  - Heatmap layer for COVID-19 deaths
- 📍 Uses country geolocation data for marker placement

## 🛠️ Technologies Used

- Python 3
- [Folium](https://python-visualization.github.io/folium/) (for interactive mapping)
- Pandas (for data processing)
- JSON / HTTP.client (for API access)

## 📦 Installation

Install the required packages with pip:

```
pip install folium pandas requests
```

---

## 📥 Data Sources
```
COVID-19 Summary Data: api.covid19api.com/summary
```
```
Country Coordinates:
https://raw.githubusercontent.com/VinitaSilaparasetty/covid-map/master/country-coordinates-world.csv
```
```
World Shape GeoJSON:
https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json
```

---

## 🚀 How It Works

1. Fetch COVID data via API
2. Normalize and clean the dataset
3. Load country coordinate data from CSV
4. Merge COVID data with geolocation data
5. Generate:
    - Choropleth Map (confirmed cases)
    - Circle Markers (confirmed & recovered)
    - Heat Map (deaths)

---

## 📸 Map Examples

- World Choropleth of Confirmed Cases
- Heatmap of COVID-19 Deaths
- Circle Markers with Popups (for each country)

---

## 📁 Project Structure
```
covid-map/
├── covid_map.ipynb  # Main notebook with map code
├── README.md        # Project description
└── ...
```

---

## License
- This project is for educational and visualization purposes.

---