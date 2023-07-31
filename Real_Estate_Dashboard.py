import pandas as pd 
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Sales Dashboard", layout="wide"
        )

uploaded_files= st.file_uploader("Choose a CSV File")


df= pd.read_csv(uploaded_files)
    


st.sidebar.header("Please Filter Here:")
location = st.sidebar.multiselect(
    "Select the Location:",
    options=df["LOCATION"].unique(),
    default=df["LOCATION"].unique()
)


min_bedrooms, max_bedrooms = st.sidebar.slider(
    "Select the Number of Bedrooms:",
    min_value=int(df['BEDS'].min()),
    max_value=int(df['BEDS'].max()),
    value=(int(df['BEDS'].min()), int(df['BEDS'].max()))
)

min_sqft, max_sqft = st.sidebar.slider(
    "Select the Sqaure Feet Range:", 
    min_value=int(df['SQUARE_FEET'].min()),
    max_value=int(df['SQUARE_FEET'].max()),
    value=(int(df['SQUARE_FEET'].min()), int(df['SQUARE_FEET'].max()))
)

status = st.sidebar.multiselect(
    "Select the Status:",
    options=df["STATUS"].unique().astype(str),
    default=df["STATUS"].unique().astype(str)
)

state = st.sidebar.multiselect(
    "Select the State:",
    options=df["STATE_OR_PROVINCE"].unique(),
    default=df["STATE_OR_PROVINCE"].unique()
)

df_selection = df[(df["STATE_OR_PROVINCE"].isin(state)) & 
    (df["STATUS"].isin(status)) & 
    (df["LOCATION"].isin(location)) &
    (df["BEDS"].between(min_bedrooms, max_bedrooms)) &
    (df["SQUARE_FEET"].between(min_sqft, max_sqft))
    ]

st.dataframe(df_selection)

csv_string= df_selection.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv_string,
    file_name="filtered_data.csv",
    mime="text/csv",
)