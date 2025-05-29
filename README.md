# ⚡ AI-Driven EV Charging Infrastructure Planner

## 🌍 Overview

As electric vehicle (EV) adoption accelerates globally, many regions face a shortage of charging infrastructure. This AI-powered project uses real-world EV data, charger locations, and clustering algorithms to identify underserved regions and suggest optimal sites for new public EV charging stations.

---

## 📈 Problem Statement

While EV stock is growing exponentially, public charging infrastructure isn’t keeping pace everywhere. This project addresses:

- Where is EV adoption growing fastest?
- Which regions are underserved by chargers?
- How can we recommend high-impact locations for new stations?

---

## 🎯 Objectives

- Analyze EV stock and charger data by region
- Identify underserved areas using clustering
- Visualize spatial disparities using Voronoi diagrams
- Recommend optimal new charger locations
- Lay the foundation for a dashboard-based planning tool

---

## 🧰 Tech Stack

| Category        | Tools/Libraries |
|----------------|-----------------|
| Language        | Python |
| Data Analysis   | Pandas, NumPy |
| Geocoding       | Geopy |
| Visualization   | Folium, Matplotlib, Seaborn |
| Clustering      | Scikit-learn (KMeans) |
| Spatial Mapping | SciPy (Voronoi) |
| API             | OpenChargeMap |
| Dashboard (Future) | Streamlit |

---

## 🧠 Methodology

### Step 1: Load and Filter EV Stock Data
Use the provided dataset (`EV.csv`) and filter for the most recent EV stock data per region.

### Step 2: Geocode Regions
Use `Geopy` to get latitude/longitude for each region in the dataset.

### Step 3: Visualize EV Stock
Map EV concentration across the globe using `Folium`.

### Step 4: Fetch Charging Station Data
Use the OpenChargeMap API to fetch real-time public charger locations in selected countries.

### Step 5: Overlay Charger Data
Overlay charger markers on the global EV stock map to identify distribution patterns.

### Step 6: Clustering
Use **KMeans clustering** to classify regions based on EV stock and charger density.

### Step 7: Voronoi Diagram
Generate a **Voronoi diagram** to highlight spatial service gaps and coverage areas of existing chargers.

---

## 📊 Key Results

- Clusters reveal countries with high EV stock but insufficient charger infrastructure.
- Voronoi plots show geographic gaps in public charger availability.
- Combined insights help prioritize where new chargers will have the most impact.

---

## 📂 Project Structure

EV-Infrastructure-AI/
├── EV.csv # EV stock dataset
├── app.py # Streamlit dashboard (future)
├── ev_charging_map.html # EV stock visualization
├── ev_stock_with_chargers.html # EV + charger visualization
├── df_cluster.csv # Clustered dataset
└── README.md # Project overview

---

## 🚀 Running the Project

 Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ev-infrastructure-ai.git
   cd ev-infrastructure-a
   ```
---

## 🔮 Future Enhancements
✅ Streamlit Dashboard for live filtering and visualization

📈 Incorporate more datasets (traffic, urban population, power grid)

🧠 Predictive modeling for EV growth using time series forecasting

📍 Reinforcement Learning for charger placement optimization

🌐 Country-level filtering, multi-criteria decision making

---

🙌 Contribution
Feel free to fork, star, or open issues. PRs for adding new datasets or better clustering models are welcome!

---

👤 Author
Yash
Data Science | Machine Learning | Geospatial AI
