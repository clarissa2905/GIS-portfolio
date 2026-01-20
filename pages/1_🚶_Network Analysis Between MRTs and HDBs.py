import streamlit as st

st.header("🚶 Network Analysis Between MRTs and HDBs")

st.set_page_config(page_icon="🚶", layout="centered")

st.markdown(
    ":green-badge[:material/apps: QGIS] :blue-badge[:material/build: Network Analysis]"
)

st.subheader("Introduction")

st.markdown(
    """
    This project was inspired by this Reddit post on r/Singapore, which illustrated 1km and 1.5km radii around all the MRT stations 
    with the intention of showing HDB buildings that are situated beyond these boundaries, which would be considered not walking distance to a station.

    However, there were a couple comments suggesting that plotting actual walking distance would be more representative rather than "point to point" -- which made me do some research.
    """
)
st.space("small")

st.image("./1_reddit pic.png", caption="Posted in 2024", width=600)

st.markdown(
    """
    I learnt about the difference between Euclidean distance and Network distance, where the former is the shortest, straight-line distance between two points in continuous space,
    while the latter is the shortest distance along a network, such as roads, pipelines or power grids. 
    
    In this real-life situation, Network distance would be more applicable to best visualise
    the HDBs that are within a 10 minute walking distance (or 800 metres) from the nearest MRT station.
    This value is based off URA's plan for "10-minute neighbourhoods" in the [2024 Urban Design Guidebook](https://www.ura.gov.sg/-/media/Corporate/Resources/Publications/Books/UD-Guidebook-3_Connected-and-Inclusive-City_2024.pdf),
    where key amenities are within walking distance from homes and workplaces.
    """
)

st.space("small")

st.image("./1_euclidean_network.jpg", caption="Euclidean distance (left), Network distance (middle, right). Source: [Medium](https://axuplatform.medium.com/euclidean-distance-vs-network-distance-69f984397438)", width=600)

st.subheader("Data Collection")

st.markdown(
    """
    - [LTA DataMall](https://datamall.lta.gov.sg/content/datamall/en/static-data.html)
        - Footpath and Road Crossing data as lines in shapefile format
    - [Data.gov](https://data.gov.sg/)
        - Existing HDB buildings data as polygons in GEOJSON format
        - MRT Station Exits as points in GEOJSON format
        - Master Plan 2019 Planning Area Boundary (No Sea) as polygons in GEOJSON format
    """
)

st.subheader("Data Preparation")

st.markdown(
    """
    1. The project Coordinate Reference System (CRS) was set to EPSG:3414 - SVY21 / Singapore TM
    2. Added all datasets except HDB buildings data
    3. Used "Merge Vector Layers" to combine Footpath and Road Crossing data into a single "Pedestrian Network" shapefile

    *insert map with above layers
    """
)

st.subheader("Network-based Service Area Analysis")

st.markdown(
    """
    I want to know which HDBs fall outside a 10-minute walking catchment of any MRT station, along the pedestrian network.

    1. As I used distance-based walking, I added a cost field :blue-badge[length(m)] to the Pedestrian Network attribute table using the Field Calculator
    """
)

st.code("length($geometry)")

st.markdown(
    """
    2. Built 800m walking areas with: Processing Toolbox → Network analysis → Service area (from layer) with the following settings
        - Network layer: Pedestrian Network
        - Start points: MRT exits
        - Path type: shortest
        - Cost field: length_m
        - Travel cost: 800
        - Direction: both
    """
)

st.subheader("Setback")
st.markdown(
    """
    After running the Service Area tool above, the resulting polylines extending from the MRT station exit points were much shorter than 800m. I then realised it was due to
    the original Pedestrian Network layer having multiple gaps, so there was no continuous network for QGIS to detect.

    So, I tried to fix the Pedestrian Network layer as much as possible by running the following geoprocessing tools, then re-ran the Service area tool.
    - Fix geometries
    - Snap geometries to layer
        - Snap tolerance: 5m ?
        - Behavior: Prefer closest point ?
    - Split lines at intersections
    - Multipart to singleparts
    - Fix geometries
    """
)

st.markdown(
    """
    */Side by side comparison images of before and after fix *
    
    /compare new map with one of the 10min maps by LTA at the stations
    """
)