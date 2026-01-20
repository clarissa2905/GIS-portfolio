import streamlit as st
import numpy as np
import pandas as pd
# import leafmap.foliumap as leafmap

st.set_page_config(page_icon="📍", layout="centered")

st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 15rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 15rem;}}
    </style>
''',unsafe_allow_html=True)

# Customize page title
st.header("📍 Clarissa's GIS Portfolio")

st.subheader("About Me")

st.markdown(
    """
    Hello! I am an Environmental Engineering major with a minor in Geographic Information Systems (GIS), with a strong interest in applying 
    geospatial technologies for the public good. My interests span from guiding urban planning decisions to improve liveability, 
    to monitoring and mitigating environmental and climate-related risks.

    My GIS coursework includes:
    - **GE3238: GIS Design and Practices**
        - Gained practical skills in GIS design, spatial data modelling, and spatial databases, with experience working across spatial data infrastructures and service-oriented architectures. Developed applied capabilities in spatial network and mobility analysis, spatial optimisation, and the responsible use of geospatial data, including ethical and privacy considerations.
    - **GE3216: Applications of GIS & Remote Sensing**
        - Built practical GIS skills through hands-on experience in GNSS/GPS data collection, raster and vector analysis, spatial statistics, interpolation, and spatial modelling. Gained experience analysing satellite and aerial imagery, assessing spatial data quality, and applying geospatial methods to real-world planning, environmental, and infrastructure problems, with exposure to GeoAI concepts.
    - **GE3252: Cartography and Geovisualisation**
        - Developed core cartographic and geovisualisation skills, including designing effective thematic maps using appropriate symbolisation, colour, projections, and typography. Gained experience evaluating and improving geographic visualisations to ensure clear, accurate, and professional spatial communication.
    
    I am seeking full-time opportunities (July 2026 onwards) in both private 
    consultancies and the public sector, where I can contribute as a creative problem solver with strong written and verbal 
    communication skills.

    On a more personal level, I enjoy travel photography, whipping up new dishes and drinks and reading unusual, thought-provoking stories!
    """
)

st.space("small")

st.subheader("👈 &nbsp; View my projects in the sidebar!")

st.space("small")

st.subheader("Get in Touch")

st.success(
    """
    💼 &nbsp; [LinkedIn](https://www.linkedin.com/in/ongclarissa/)

    📧 &nbsp; [clarissaong@u.nus.edu](mailto:clarissaong@u.nus.edu)

    """
)