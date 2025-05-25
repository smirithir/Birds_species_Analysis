import streamlit as st
import pandas as pd
import plotly.express as px

# Load cleaned data
bird_data = pd.read_csv("/home/smirithi/Downloads/Myne/Pro-1/cleaned_bird_sightings.csv") 

# Convert 'date' column to datetime
bird_data['Date'] = pd.to_datetime(bird_data['Date'])

# Sidebar filters
st.sidebar.title("Filters")
location_type = st.sidebar.selectbox("Select Location Type", bird_data['Location_Type'].dropna().unique())
species_filter = st.sidebar.multiselect("Select Common Name(s)", bird_data['Common_Name'].dropna().unique())
date_range = st.sidebar.date_input("Select Date Range", 
                                   [bird_data['Date'].min(), bird_data['Date'].max()])

# Filter data based on selections
filtered_df = bird_data[
    (bird_data['Location_Type'] == location_type) &
    (bird_data['Date'] >= pd.to_datetime(date_range[0])) &
    (bird_data['Date'] <= pd.to_datetime(date_range[1]))
]

if species_filter:
    filtered_df = filtered_df[filtered_df['Common_Name'].isin(species_filter)]

# Page title
st.title("🦜 Bird Species Monitoring Dashboard")

st.markdown("This dashboard provides interactive visualizations for bird species diversity, weather conditions, and observational patterns.")

# Species count bar chart
species_count = filtered_df['Common_Name'].value_counts().reset_index()
species_count.columns = ['Common Name', 'Count']
fig_species = px.bar(species_count, x='Common Name', y='Count', title="Species Observation Count")
st.plotly_chart(fig_species)

# Temperature vs Humidity scatter plot
fig_weather = px.scatter(filtered_df,
                         x='Temperature',
                         y='Humidity',
                         color='Common_Name',
                         hover_data=['Scientific_Name', 'Plot_Name', 'Date'],
                         title='Temperature vs Humidity by Species')
st.plotly_chart(fig_weather)

# Display filtered data
st.subheader(f"Filtered Data ({len(filtered_df)} records):")
st.dataframe(filtered_df[['Date', 'Scientific_Name', 'Common_Name', 'Plot_Name', 'Temperature', 'Humidity']])

# Optional: Map (if coordinates are present)
if 'Latitude' in bird_data.columns and 'Longitude' in bird_data.columns:
    st.subheader("Observation Map")
    st.map(filtered_df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}))

# Footer
st.markdown("---")

