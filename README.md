# Birds_species_Analysis
Birds monitoring analysis and visualization
This project focuses on analyzing and visualizing bird species sightings collected from forest monitoring data. The goal is to identify patterns in species diversity and present insights through an interactive dashboard.

## 📂 Project Structure

- **Jupyter Notebook (`.ipynb`)**  
  Used for **data cleaning**, **preprocessing**, and **exploratory data analysis (EDA)**.  
  Key steps:
  - Merging Excel sheets with pandas
  - Removing duplicates and handling missing values
  - Filtering and formatting columns for analysis

- **Python Script (`.py`)**  
  Contains the code to build the **Streamlit dashboard** for visualization.  
  Features:
  - Location filter
  - Data table display
  - Charts showing bird counts, species distribution, and environmental impacts

- **Streamlit App**  
  An interactive dashboard that allows users to:
  - Select location types and view related sightings
  - Visualize trends with Plotly charts
  - Understand how temperature and humidity relate to bird presence
  
#  Required Python packages:
  pip install pandas streamlit plotly openpyxl
# Streamlit :
streamlit run /home/smirithi/Downloads/Myne/Pro-1/Birds_species_analysis_dashboard.py
http://localhost:8501/
