import requests 
import streamlit as st 
from streamlit_lottie import st_lottie
import pandas as pd 
import plotly.express as px 
from PIL import Image
import pathlib as Path


## Lambada 

def additional_bedroom_opportunity(x):
    # try: 
        
    if (x['ratio_sqft_bd'] >= 150)  and (x['BEDS'] > 1):
        return 1
    else:
        return 0
        
    # except:
    #     return 0
    
        
def adu_potential(x):
    #try:
        if (x['ratio_lot_sqft'] >= 3) and (x['BEDS'] > 1):
            return 1 
        else: 
            return 0 
        
    #except:
       # return 0

    

def convert_df(df): 
    return df.to_csv(index=False).encode('utf-8')

st.set_page_config(
    page_title="Real Estate Property Stats",
)

## Streamlit Decorations 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

## Load Assets
lottie_coding = load_lottieurl("https://lottie.host/8f545761-4f4a-45b1-8277-4c5f72768ba9/86JNNb7geq.json")
lottie_coding_2 = load_lottieurl("https://lottie.host/40eecc5c-767b-488a-af75-a1229cdd036e/wdG2emyX24.json")
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)

image_drop= Image.open("C:/Users/monic/Downloads/Proj3/Images_pro3/zoomin4columns.png")
image_ratio_bed= Image.open("C:/Users/monic/Downloads/Proj3/Images_pro3/ratio_bed_excel.png")
image_ratio_bed2=Image.open("C:/Users/monic/Downloads/Proj3/Images_pro3/square_feet_and_beds.png")
image_opp_1=Image.open("C:/Users/monic/Downloads/Proj3/Images_pro3/additionalopppt1.png")
image_opp_2=Image.open("C:/Users/monic/Downloads/Proj3/Images_pro3/additionalopppt2.png")
image_lot_1=Image.open("C:/Users/monic/Downloads/Proj3/Images_pro3/ratio_lotpt1.png")
image_lot_2=Image.open("C:/Users/monic/Downloads/Proj3/Images_pro3/ratio_lotpt2.png")
image_pot_1= Image.open("C:/Users/monic/Downloads/Proj3/Images_pro3/adu_pot1.png")
image_pot_2=Image.open("C:/Users/monic/Downloads/Proj3/Images_pro3/adu_pot2.png")
image_final=Image.open("C:/Users/monic/Downloads/Proj3/Images_pro3/outputfinal.png")


st.title('Real Estate Property Data Stats')
st.markdown('Upload your real estate files to get property market data ')
st.markdown('#### Upload a CSV File')
uploaded_files = st.file_uploader("Choose a CSV file")

if uploaded_files is not None:
    # read the file 
    df= pd.read_csv(uploaded_files)
    

 ###METRICS
    st.markdown('## Property Data')
    col1, col2, col3, col4 =st.columns(4)
    col1.metric("Total", len(df), help="Number of Properties")
    col2.metric("Average Price", "${:,.2f}M".format(df['PRICE'].mean() /1e6), help='Average Sale Price')
    col3.metric("Days on Market", int(df['DAYS ON MARKET'].mean()), help='Average Days on Market')
    col4.metric("Price Per Square Ft", "${:,}".format(int(df['$/SQUARE FEET'].mean())), help='Average Price Per Square Ft')
   
    ##CHARTS
    with st.expander("Charts", expanded=True):
     st.markdown('## Charts')
     fig= px.histogram(df, x="DAYS ON MARKET", title='Days on Market Histogram Chart')
     st.plotly_chart(fig, use_container_width=True)

     fig = px.box(df, x="PRICE", title='Box Plot for Property Price')
     st.plotly_chart(fig, use_container_width=True)

     fig= px.histogram(df, x="$/SQUARE FEET", title='Price Per SQFT')
     st.plotly_chart(fig, use_container_width=True)

     ##FEATURES
    st.write(df.columns)
    df_features = df.copy()
    df_features['ratio_sqft_bd'] = df_features['SQUARE_FEET'] / df_features['BEDS']
    df_features['additional_bd_opp'] = df_features.apply(lambda x:
        additional_bedroom_opportunity(x), axis=1)
    df_features['ratio_lot_sqft'] = df_features['LOT SIZE'] / df_features['SQUARE_FEET']
    df_features['adu_potential'] =df_features.apply(lambda x:
        adu_potential(x), axis=1)
    

    

    st.dataframe(df_features)
    with st.expander('Opportunities', expanded=True):
        st.markdown('## Opportunities')
        df_add_bd= df_features[df_features['additional_bd_opp']== True]
        df_adu= df_features[df_features['adu_potential']==True]

        st.dataframe(df_add_bd)

        print("Number of opportunities for additional bedrooms:", len(df_add_bd))
        print("Number of ADU opportunities:", len(df_adu))
        col1, col2, =st.columns(2)
        col1.metric('Total Add Bd', len(df_add_bd), help='Number of properties with additional bedroom opportunities')
        col2.metric('Total ADU', len(df_adu), help='Number of properties with ADU potential')

        st.markdown('#### Featurized Dataset')
        st.write(df_features)

        #Convert Featurized Dataset into CSV
        csv= convert_df(df_features)

        st.download_button(
            "Download Here!",
            csv,
            "property_dataset.csv",
            "text/csv",
            key='download-csv'
        )

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with left_column:
    st.lottie(lottie_coding_2, height=300, key="building")

st.markdown('### How to Use')
st.write('###### You must format your CSV for this app to work please follow these steps below :')
st.write('1. Set your bedrooms column to BEDS')
st.write('2. Set your price column to PRICE')
st.write('3. Set lot size to LOT_SIZE')
st.write('4. Set your square footage to SQUARE_FEET')
st.write('5. Set your days on market to DAYS_ON_MARKET (if any, if not then just add 0 to the whole column) ')

with st.container():
    st.write("------")
    st.write('#### How to calculate for additional bedrooms and ADU (Additional Dwelling Opportunities) ')
    st.write('**Note: For the opportunities there is a fixed set needed to satisfy an additional bedroom and dwelling unit. This criteria is fixed into the app and is unable to be changed by the user')
    st.write('##')
    st.write('##### 1. Insert four additional columns at the end of your spreadsheet with the following titles:')
    st.write('- ratio_sqft_bd')
    st.write('- additional_bd_opp')
    st.write('- ratio_lot_sqft')
    st.write('- adu_potential')
    st.write('Example below:')
    image_column, text_column= st.columns((1,2))
    with image_column: 
        st.image(image_drop)
    st.write("##")
    st.write('##### 2. Next calculate each column through these formulas: ')
    st.write('###### A. ratio_sqft_bd')
    st.write(' For ratio_sqft_bd column divide the square feet by number of bedrooms (= SQUARE_FEET/BEDS)')
    image_column, text_column= st.columns((1,2))
    with image_column: 
        st.image(image_ratio_bed)
        st.image(image_ratio_bed2)
    st.write('##')
    st.write('###### B. additional_bd_opp')
    st.write(' For the additional_bd_opp you need to set a criteria referencing the ratio_sqft_bd value where it must be greater than or equal to 150(ratio_sqft_bd) and has more than one bedroom, the output has to be a TRUE or FALSE value')
    st.write('Example below:')
    image_column, text_column= st.columns((1,2))
    with image_column: 
        st.image(image_opp_1)
        st.image(image_opp_2)
    st.write('##')
    st.write('###### C. ratio_lot_sqft')
    st.write('To calculate the ratio_lot_sqft you divide the lot size by the square feet (LOT_SIZE/SQUARE_FEET)')
    image_column, text_column= st.columns((1,2))
    with image_column: 
        st.image(image_lot_1)
        st.image(image_lot_2)

    st.write('##')
    st.write('###### D. adu_potential')
    st.write(' For adu_potential similar to additional bedroom opportunity the output must either be TRUE or FALSE, it must satisfy the condition where the ratio_lot_sqft value be at least 5 and a minimum of one bedroom')
    image_column, text_column= st.columns((1,2))
    with image_column: 
        st.image(image_pot_1)
        st.image(image_pot_2)
    st.write('###### The final output should look like this')
    image_column, text_column= st.columns((1,2))
    with image_column: 
        st.image(image_final)
        

    
    
    