import streamlit as st
import pickle
import numpy as np
import os

st.sidebar.title("Vijay Used Car Price Prediction!!!")

# Ensure all dictionaries are fully defined
Make_dict = {'Maruti': 0, 'Hyundai': 1, 'Datsun': 2, 'Honda': 3, 'Tata': 4, 'Chevrolet': 5, 'Toyota': 6, 'Jaguar': 7, 'Mercedes-Benz': 8, 'Audi': 9, 'Skoda': 10, 'Jeep': 11, 'BMW': 12, 'Mahindra': 13, 'Ford': 14, 'Nissan': 15, 'Renault': 16, 'Fiat': 17, 'Volkswagen': 18, 'Volvo': 19, 'Mitsubishi': 20, 'Land': 21, 'Daewoo': 22, 'MG': 23, 'Force': 24, 'Isuzu': 25, 'OpelCorsa': 26, 'Ambassador': 27, 'Kia': 28}

Model_dict = {'800 AC': 0, 'Wagon R LXI Minor': 1, 'RediGO T Option': 2, 'Amaze VX i-DTEC': 3, 'Indigo Grand Petrol': 4, 'Sail 1.2 Base': 5, 'Corolla Altis 1.8 VL CVT': 6, 'Ciaz VXi Plus': 7, 'Enjoy TCDi LTZ 7 Seater': 8, 'New C-Class 220 CDI AT': 9, 'Vitara Brezza ZDi Plus AMT': 10, 'Q5 2.0 TDI': 11, 'City V MT': 12, 'A6 2.0 TDI Design Edition': 13, 'Superb Ambition 2.0 TDI CR AT': 14, 'Corolla Altis G AT': 15, 'Compass 1.4 Sport Plus BSIV': 16, 'E-Class E 200 CGI Elegance': 17, 'i10 Magna 1.1L': 18, 'Q7 35 TDI Quattro Premium': 19, 'Elantra CRDi S': 20, 'Scorpio 1.99 S10': 21, 'City i DTEC V': 22, 'Scorpio LX': 23, 'Santro Xing GLS': 24, 'Alto LXi': 25, 'Swift Dzire VDI Optional': 26, 'Eeco 5 Seater AC BSIV': 27, 'Omni Maruti Omni MPI STD BSIII 5-STR W/ IMMOBILISER': 28, 'Swift ZDi BSIV': 29, 'Jeep CL 500 MDI': 30, 'City i DTEC VX': 31, 'Indica DLS': 32, 'EON Magna Plus': 33, 'Tavera Neo LS B3 - 7(C) seats BSIII': 34, 'Corolla Altis Diesel D4DG': 35, 'Scorpio 1.99 S6 Plus': 36, 'Indigo Classic Dicor': 37, 'Indica Vista Quadrajet LS': 38, 'Swift 1.3 VXi': 39, 'Civic 1.8 V AT': 40, 'i10 Sportz 1.2': 41, 'Rapid 1.5 TDI Elegance': 42, 'Getz GLS': 43, 'Terrano XL': 44, 'Amaze S i-VTEC': 45, 'Brio S MT': 46, 'S-Class S 350d Connoisseurs Edition': 47, 'XUV500 W8 2WD': 48, 'Duster 85PS Diesel RxL Optional': 49, 'Santro Xing XO': 50, 'Bolero 2011-2019 SLE': 51, 'Avventura MULTIJET Emotion': 52, 'A8 4.2 TDI': 53, 'RediGO 1.0 S': 54, 'Jetta 1.4 TSI Comfortline': 55, 'A4 2.0 TDI 177 Bhp Premium Plus': 56, 'E-Class Exclusive E 200 BSIV': 57, 'X1 sDrive 20d xLine': 58, 'V40 D3 R Design': 59, 'SX4 Zxi BSIII': 60, '7 Series 730Ld': 61, 'Bolero Power Plus SLX': 62, 'Sonata CRDi M/T': 63, 'Micra Active XV Petrol': 64, 'Xylo D4': 65, 'KWID RXT': 66, 'Xylo E4 BS III': 67, 'SX4 ZXI MT BSIV': 68, 'Swift Dzire VDI': 69, 'Scorpio LX BSIV': 70, 'SX4 Vxi BSIII': 71, 'Ertiga VDI': 72, 'Beat Diesel': 73, 'Zen LX': 74, 'Santro Sportz BSIV': 75, 'i20 Magna 1.2': 76}

year_dict = {1992: 0, 1995: 1, 1996: 2, 1997: 3, 1998: 4, 1999: 5, 2000: 6, 2001: 7, 2002: 8, 2003: 9, 2004: 10, 2005: 11, 2006: 12, 2007: 13, 2008: 14, 2009: 15, 2010: 16, 2011: 17, 2012: 18, 2013: 19, 2014: 20, 2015: 21, 2016: 22, 2017: 23, 2018: 24, 2019: 25, 2020: 26}

km_driven_dict = {None: 0, 10000: 1, 20000: 2, 30000: 3, 40000: 4, 50000: 5}

fuel_dict = {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4}

owner_dict = {'First Owner': 0, 'Second Owner': 1, 'Above Three': 2, 'Test Drive Car': 3}

# Sidebar inputs
Make = st.sidebar.selectbox("Brand", [None] + list(Make_dict.keys()))
Model = st.sidebar.selectbox("Model", [None] + list(Model_dict.keys()))
year = st.sidebar.selectbox("Year", [None] + list(year_dict.keys()))
km_driven = st.sidebar.selectbox("Number of Kilometers", [None] + list(km_driven_dict.keys())[1:])
fuel = st.sidebar.selectbox("Fuel Type", [None] + list(fuel_dict.keys()))
owner = st.sidebar.selectbox("Owner", [None] + list(owner_dict.keys()))

# Button to trigger prediction
button = st.sidebar.button("Get Price")

# Ensure all inputs are provided
f = [Make, Model, year, km_driven, fuel, owner]

if None not in f and button:
    try:
        Features = [[Make_dict[Make], Model_dict[Model], year_dict[year], km_driven_dict[km_driven], fuel_dict[fuel], owner_dict[owner]]]
        
        # Debugging print statements to check the Features array
        st.write("Features for prediction:", Features)
        
        # Load the saved model 
        Model = pickle.load(open('LinearJhoom.pkl', 'rb'))
        
        # Ensure the features array is 2D as expected by the model
        Features_df = pd.DataFrame(Features, columns=['Make', 'Model', 'Year', 'Kilometers_Driven', 'Fuel_Type', 'Owner_Type'])
        prediction = Model.predict(Features)[0]

        st.markdown(f"<h2 style='text-align: center; color: #6A3BFF;'>Vijay Used Car Price Prediction</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; color: #6A3BFF;'>Your Approximate Car Price is Rs. {round(prediction)}/-</h3>", unsafe_allow_html=True)
        st.image("car.png", width=200, caption="Drive Safe!", use_column_width=True)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.markdown(f"<h2 style='text-align: center; color: white;'>Enter all the values to get your car price</h2>", unsafe_allow_html=True)
