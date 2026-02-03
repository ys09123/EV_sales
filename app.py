import streamlit as st
import pandas as pd
import folium
from streamlit.components.v1 import html

# ======================
# Load clustered data
# ======================
df_cluster = pd.read_csv("df_cluster.csv")

st.set_page_config(page_title="EV Infrastructure Recommendations", layout="wide", page_icon="🔋")

st.title("EV Infrastructure Recommendations")

# ======================
# Helper: cluster color
# ======================
def get_color(cluster):
    if cluster == 0:
        return "red"        # High priority
    elif cluster == 1:
        return "orange"     # Medium priority
    else:
        return "green"      # Low priority

# ======================
# Create map
# ======================
m = folium.Map(
    location=[df_cluster["lat"].mean(), df_cluster["lon"].mean()],
    zoom_start=4,
    tiles="CartoDB positron"
)

for _, row in df_cluster.iterrows():
    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=3,
        color=get_color(row["cluster"]),
        fill=True,
        fill_opacity=0.7,
        popup=f"""
        <b>Region:</b> {row['region']}<br>
        <b>EV Value:</b> {row['value']}<br>
        <b>Chargers:</b> {row['num_chargers']}<br>
        <b>Charger Density:</b> {row['charger_density']}<br>
        <b>Cluster:</b> {row['cluster']}
        """
    ).add_to(m)

# ======================
# Display map
# ======================
st.subheader("EV Infrastructure Priority Map")
html(m._repr_html_(), height=520)

st.markdown("""
**Cluster Legend**
- 🔴 High EV demand, low charger density
- 🟠 Moderate EV demand
- 🟢 Adequate infrastructure
""")