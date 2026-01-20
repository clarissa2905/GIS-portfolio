import streamlit as st

st.header("💧 Pollutant Modelling in Mølle Å Stream")

st.set_page_config(page_icon="💧", layout="centered")

st.markdown(
    """
    This is part of a group assignment for the Masters-level course [12104 Environmental Modelling](https://lifelonglearning.dtu.dk/en/sustain/single-course/environmental-modelling/) 
    I took when I was on student exchange at the Technical University of Denmark in Fall 2024.

    The aim was to visualise the severity of untreated wastewater discharge of 24 Combined Sewer Overflows (CSOs) into the Mølle Å Stream that connects Lyngby Lake to the Øresund strait in Denmark. 
    Such overflows occur during brief, high intensity rain events that generally occurs during summer, where streamflow is the lowest. 
    Therefore, Mølle Å receives the most pollution while it is least able to dilute it, resulting in greatest detrimental effects to the surrounding ecosystem, namely eutrophication.

    We would like to find out how many, and where the stretches of the river are at risk due to CSO emissions.

    To start, the following river data was downloaded as shapefiles from Denmark's open environmental data portal, [Danmarks Miljøportalen](https://danmarksarealinformation.miljoeportal.dk/):
    - Yearly water supply -> for Nitrogen balance
    - Monthly water supply -> for CSO impact assessment
    - Latest water flow calculation point -> for coordinates of the nodes of the river model

    """   
)

st.image("./map of CSO structures along stream.png", caption="Map of CSO structures along Mølle Å", width=600)

st.markdown(
    """
    The data from Danmarks Miljøportalen was analysed using Python and it was found that the CSO nodes "Vi R2" and "Lu R20F" discharged the most pollutant (Phosphorous and Nitrogen).

    """
)

st.image("./copper concentrations map.png", caption="Copper concentrations in Mølle Å in March and July", width=1300)

st.markdown(
   """
   From the image above, the darker coloured circles represent higher concentrations of copper. There are higher
concentrations of copper in July, with the peak value being 0.01327 g/m3 compared to 0.006816 g/m3 in
March. For both months, the stretch of highest risk is between nodes DK1_10023 and DK1_13500,
nearer the end of the river. This stretch corresponds to the location of the CSO, UF01001, which was
identified in to have high discharge. The model establishes a link between that CSO and the high
heavy metal concentration in Mølle Å.

""" 
)