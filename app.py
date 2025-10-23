import streamlit as st
from streamlit_folium import st_folium
import folium

# === PAGE SETTINGS ===
st.set_page_config(page_title="GeoMap Platform", layout="wide")

st.title("🌍 Interactive Map Platform Prototype")
st.markdown("""
This prototype demonstrates how to embed an interactive map in a Streamlit app.
You can adapt it for zero-carbon materials, IAQ data, or sustainable building datasets.
""")

# === MAP SETTINGS ===
latitude = st.number_input("Enter latitude:", value=-36.8485)
longitude = st.number_input("Enter longitude:", value=174.7633)
zoom_level = st.slider("Zoom level:", 5, 18, 12)

# === CREATE MAP ===
m = folium.Map(location=[latitude, longitude], zoom_start=zoom_level, tiles="OpenStreetMap")

# Add a marker
folium.Marker(
    [latitude, longitude],
    tooltip="Selected Location",
    popup=f"Lat: {latitude}, Lon: {longitude}"
).add_to(m)

# Add a layer control (optional)
folium.LayerControl().add_to(m)

# === DISPLAY MAP IN STREAMLIT ===
st_data = st_folium(m, width=1000, height=600)

# === INTERACTION OUTPUT ===
if st_data and st_data["last_clicked"]:
    lat = st_data["last_clicked"]["lat"]
    lon = st_data["last_clicked"]["lng"]
    st.success(f"🗺️ You clicked on coordinates: ({lat:.5f}, {lon:.5f})")

st.markdown("---")
st.caption("Prototype created by Armin Baghaei • Streamlit + Folium + GitHub Cloud Deployment")
