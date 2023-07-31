# Real-Estate-App

## Project Description
##### What the Application Does:

The application serves as a comprehensive descriptive analytics tool for the real estate market. Users can upload their property data in CSV format, and the app performs meticulous data analysis, focusing on key factors such as "Beds," "Square Footage," and "Lot Size." By filtering out irrelevant or missing data, the app ensures the accuracy of its results.

The app presents users with essential property metrics, including the total number of properties in the dataset, the average property price, and the average price per square foot. Users can further explore how specific factors impact property prices, enabling them to make well-informed investment or pricing decisions.

#### Why We Used These Technologies:

The application was built using Streamlit. Streamlit's simplicity and efficiency allowed us to rapidly develop a highly interactive and user-friendly interface.

Python was the programming language of choice due to its versatility and robust data processing capabilities. Leveraging Python's libraries such as Pandas and NumPy enabled us to handle complex data analysis.

#### Challenges Faced and Future Features:

During the development process, we encountered several challenges. One such challenge was ensuring the accuracy of the app's results by considering additional factors beyond property size. Factors like zoning laws, city regulations, and property shape influence the feasibility of certain property enhancements, like adding an ADU. In the future, we aim to incorporate more sophisticated algorithms and machine learning techniques to account for these variables and deliver even more precise insights.

Additionally, expanding the app to include a broader range of property types, such as commercial real estate, is a key feature we plan to implement. By incorporating commercial property data, the app will cater to a wider audience, including investors exploring different sectors of the real estate market.

### TABLE OF CONTENT:
1. Imported Modules
2.
3.

### Imported Modules 

These are the modules used for the three pages of the Streamlit 

#### Real Estate Page

![real_estate_libraries page](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/260b7822-e21d-49a5-81cd-925d98b1b16b)

#### Real Estate Dashboard and Real Estate Sales Page

![sales_dash](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/0eae58a4-ccb7-4d95-b8c2-18a0758c2419)

Here you can name your Streamlit browser title with st.title function , to add the function of uploading files yuo use the st.file_uploader and assign it a variable

![choose_csv](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/67622ff8-8763-4cea-93f8-76bfc4997eaf)


#### CONVERT 
Here we will convert the df(dataframe) into a CSV file.After converting the DataFrame to a CSV string, this method encodes the string using UTF-8 format. UTF-8 is a character encoding that allows for the representation of a wide range of characters from various languages and is widely used to ensure compatibility across different systems and platforms.

![convert_df](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/791daf7d-9cd3-4912-9280-4ebf80693082)


#### LOTTIE 

A Lottie is a JSON-based animation file format that allows you to ship animations on any platform as easily as shipping static assets. They are small files that work on any device and can scale up or down without pixelation. 

Below is how you code your function to get your lottie animations in, you would need to use requests which is one of the modules you import in your libraries 
we will be using json as the file you can use from the lottie website is the json url.
- set a container with options of a right and left column 

Lottie is optional if you want to add animations you can go to the Lottie website [Here!](https://lottiefiles.com/)

![lottie_deco](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/24ff0587-6dfd-4bd8-9c45-13f5debf242d)

After referencing the link to your desired Lottie Files assing the lottie varibales to the left or right column of the streamlit page:

#### LAMBDA
Below is the function for adding an additional bedroom and an additional adu, here its set at a ratio of at least 150 for bedrooms and a ratio of at least 3 for ADU and at elast one present bedroom, but you can change it if you follow a different criteria

The 1 and 0 is the true and false values where you must reference later when creating these columns in the csv file

![real_estate_lambda](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/e3c40a47-4c1e-43f5-8d3d-72aa14d36fe9)

#### CHARTS

Here we are creating the various charts for each different metric , we will also be using the plotly express library to do this

Here we assign the 

![charts](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/edd0d52f-cf9c-43f1-a1fc-4aca83f352e3)

![df_features](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/d657a351-9f0f-4488-b5d9-8ccce44fb19b)

![download](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/f8622258-96e4-41ad-b149-65dec65a1218)

![features](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/3bf869c3-3815-4615-9453-56c0385a7ebc)

![lottie ref](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/51fb51a6-810b-4625-aa91-fac61fbced2a)

![Metrics ](https://github.com/Mestrada1997/Real-Estate-App/assets/125697853/61c316bb-746b-497e-b77d-4bebcc04e00b)





Note: The Lottie and PIL libraries are optional if you wanna add animations and images to your Streamlit





