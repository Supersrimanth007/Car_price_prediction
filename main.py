import streamlit as st
import pickle
import pandas as pd

st.sidebar.title("Vijay Used Car Price Prediction!!!")

# Brand
Make = st.sidebar.selectbox("Brand", [None] + ['Maruti', 'Hyundai', 'Datsun', 'Honda', 'Tata', 'Chevrolet', 'Toyota', 'Jaguar', 'Mercedes-Benz', 'Audi', 'Skoda', 'Jeep', 'BMW', 'Mahindra', 'Ford', 'Nissan', 'Renault', 'Fiat', 'Volkswagen', 'Volvo', 'Mitsubishi', 'Land', 'Daewoo', 'MG', 'Force', 'Isuzu', 'OpelCorsa', 'Ambassador', 'Kia'])
Make_dict = {'Maruti': 0, 'Hyundai': 1, 'Datsun': 2, 'Honda': 3, 'Tata': 4, 'Chevrolet': 5, 'Toyota': 6, 'Jaguar': 7, 'Mercedes-Benz': 8, 'Audi': 9, 'Skoda': 10, 'Jeep': 11, 'BMW': 12, 'Mahindra': 13, 'Ford': 14, 'Nissan': 15, 'Renault': 16, 'Fiat': 17, 'Volkswagen': 18, 'Volvo': 19, 'Mitsubishi': 20, 'Land': 21, 'Daewoo': 22, 'MG': 23, 'Force': 24, 'Isuzu': 25, 'OpelCorsa': 26, 'Ambassador': 27, 'Kia': 28}

# Model
Model = st.sidebar.selectbox("Model", [None] + [
    '800 AC', 'Wagon R LXI Minor', 'RediGO T Option', 'Amaze VX i-DTEC', 'Indigo Grand Petrol', 'Sail 1.2 Base',
    'Corolla Altis 1.8 VL CVT', 'Ciaz VXi Plus', 'Enjoy TCDi LTZ 7 Seater', 'New C-Class 220 CDI AT',
    'Vitara Brezza ZDi Plus AMT', 'Q5 2.0 TDI', 'City V MT', 'A6 2.0 TDI Design Edition', 'Superb Ambition 2.0 TDI CR AT',
    'Corolla Altis G AT', 'Compass 1.4 Sport Plus BSIV', 'E-Class E 200 CGI Elegance', 'i10 Magna 1.1L',
    'Q7 35 TDI Quattro Premium', 'Elantra CRDi S', 'Scorpio 1.99 S10', 'City i DTEC V', 'Scorpio LX', 'Santro Xing GLS',
    'Alto LXi', 'Swift Dzire VDI Optional', 'Eeco 5 Seater AC BSIV', 'Omni Maruti Omni MPI STD BSIII 5-STR W/ IMMOBILISER',
    'Swift ZDi BSIV', 'Jeep CL 500 MDI', 'City i DTEC VX', 'Indica DLS', 'EON Magna Plus', 'Tavera Neo LS B3 - 7(C) seats BSIII',
    'Corolla Altis Diesel D4DG', 'Scorpio 1.99 S6 Plus', 'Indigo Classic Dicor', 'Indica Vista Quadrajet LS',
    'Swift 1.3 VXi', 'Civic 1.8 V AT', 'i10 Sportz 1.2', 'Rapid 1.5 TDI Elegance', 'Getz GLS', 'Terrano XL', 'Amaze S i-VTEC',
    'Brio S MT', 'S-Class S 350d Connoisseurs Edition', 'XUV500 W8 2WD', 'Duster 85PS Diesel RxL Optional', 'Santro Xing XO',
    'Bolero 2011-2019 SLE', 'Avventura MULTIJET Emotion', 'A8 4.2 TDI', 'RediGO 1.0 S', 'Jetta 1.4 TSI Comfortline',
    'A4 2.0 TDI 177 Bhp Premium Plus', 'E-Class Exclusive E 200 BSIV', 'X1 sDrive 20d xLine', 'V40 D3 R Design',
    'SX4 Zxi BSIII', '7 Series 730Ld', 'Bolero Power Plus SLX', 'Sonata CRDi M/T', 'Micra Active XV Petrol', 'Xylo D4',
    'KWID RXT', 'Xylo E4 BS III', 'SX4 ZXI MT BSIV', 'Swift Dzire VDI', 'Scorpio LX BSIV', 'SX4 Vxi BSIII', 'Ertiga VDI',
    'Beat Diesel', 'Zen LX', 'Santro Sportz BSIV', 'i20 Magna 1.2'
])
Model_dict = {'800 AC': 0, 'Wagon R LXI Minor': 1, 'RediGO T Option': 2, 'Amaze VX i-DTEC': 3, 'Indigo Grand Petrol': 4, 'Sail 1.2 Base': 5, 'Corolla Altis 1.8 VL CVT': 6, 'Ciaz VXi Plus': 7, 'Enjoy TCDi LTZ 7 Seater': 8, 'New C-Class 220 CDI AT': 9, 'Vitara Brezza ZDi Plus AMT': 10, 'Q5 2.0 TDI': 11, 'City V MT': 12, 'A6 2.0 TDI Design Edition': 13, 'Superb Ambition 2.0 TDI CR AT': 14, 'Corolla Altis G AT': 15, 'Compass 1.4 Sport Plus BSIV': 16, 'E-Class E 200 CGI Elegance': 17, 'i10 Magna 1.1L': 18, 'Q7 35 TDI Quattro Premium': 19, 'Elantra CRDi S': 20, 'Scorpio 1.99 S10': 21, 'City i DTEC V': 22, 'Scorpio LX': 23, 'Santro Xing GLS': 24, 'Alto LXi': 25, 'Swift Dzire VDI Optional': 26, 'Eeco 5 Seater AC BSIV': 27, 'Omni Maruti Omni MPI STD BSIII 5-STR W/ IMMOBILISER': 28, 'Swift ZDi BSIV': 29, 'Jeep CL 500 MDI': 30, 'City i DTEC VX': 31, 'Indica DLS': 32, 'EON Magna Plus': 33, 'Tavera Neo LS B3 - 7(C) seats BSIII': 34, 'Corolla Altis Diesel D4DG': 35, 'Scorpio 1.99 S6 Plus': 36, 'Indigo Classic Dicor': 37, 'Indica Vista Quadrajet LS': 38, 'Swift 1.3 VXi': 39, 'Civic 1.8 V AT': 40, 'i10 Sportz 1.2': 41, 'Rapid 1.5 TDI Elegance': 42, 'Getz GLS': 43, 'Terrano XL': 44, 'Amaze S i-VTEC': 45, 'Brio S MT': 46, 'S-Class S 350d Connoisseurs Edition': 47, 'XUV500 W8 2WD': 48, 'Duster 85PS Diesel RxL Optional': 49, 'Santro Xing XO': 50, 'Bolero 2011-2019 SLE': 51, 'Avventura MULTIJET Emotion': 52, 'A8 4.2 TDI': 53, 'RediGO 1.0 S': 54, 'Jetta 1.4 TSI Comfortline': 55, 'A4 2.0 TDI 177 Bhp Premium Plus': 56, 'E-Class Exclusive E 200 BSIV': 57, 'X1 sDrive 20d xLine': 58, 'V40 D3 R Design': 59, 'SX4 Zxi BSIII': 60, '7 Series 730Ld': 61, 'Bolero Power Plus SLX': 62, 'Sonata CRDi M/T': 63, 'Micra Active XV Petrol': 64, 'Xylo D4': 65, 'KWID RXT': 66, 'Xylo E4 BS III': 67, 'SX4 ZXI MT BSIV': 68, 'Swift Dzire VDI': 69, 'Scorpio LX BSIV': 70, 'SX4 Vxi BSIII': 71, 'Ertiga VDI': 72, 'Beat Diesel': 73, 'Zen LX': 74, 'Santro Sportz BSIV': 75, 'i20 Magna 1.2': 76}

# Year
year = st.sidebar.selectbox("Year", [None] + list(range(1992, 2021)))
year_dict = {1992: 0, 1993: 1, 1994: 2, 1995: 3, 1996: 4, 1997: 5, 1998: 6, 1999: 7, 2000: 8, 2001: 9, 2002: 10, 2003: 11, 2004: 12, 2005: 13, 2006: 14, 2007: 15, 2008: 16, 2009: 17, 2010: 18, 2011: 19, 2012: 20, 2013: 21, 2014: 22, 2015: 23, 2016: 24, 2017: 25, 2018: 26, 2019: 27, 2020: 28}

# Fuel Type
fuel = st.sidebar.selectbox("Fuel Type", [None] + ['Petrol', 'Diesel', 'CNG'])
fuel_dict = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}

# Transmission
transmission = st.sidebar.selectbox("Transmission", [None] + ['Manual', 'Automatic'])
transmission_dict = {'Manual': 0, 'Automatic': 1}

# KM Driven
km_driven = st.sidebar.number_input("Kilometers Driven", min_value=0, max_value=500000, step=1000)

# Owner Type
owner = st.sidebar.selectbox("Owner Type", [None] + ['First', 'Second', 'Third', 'Fourth & Above'])
owner_dict = {'First': 0, 'Second': 1, 'Third': 2, 'Fourth & Above': 3}

# Load model
model = pickle.load(open('LinearJoohm.pkl','rb'))

# Predict function
def predict_price(make, model, year, fuel, transmission, km_driven, owner):
    features = pd.DataFrame({
        'Make': [make],
        'Model': [model],
        'Year': [year],
        'Fuel_Type': [fuel],
        'Transmission': [transmission],
        'Kilometers_Driven': [km_driven],
        'Owner_Type': [owner]
    })

    # Convert categorical variables to numerical
    features['Make'] = features['Make'].map(Make_dict)
    features['Model'] = features['Model'].map(Model_dict)
    features['Year'] = features['Year'].map(year_dict)
    features['Fuel_Type'] = features['Fuel_Type'].map(fuel_dict)
    features['Transmission'] = features['Transmission'].map(transmission_dict)
    features['Owner_Type'] = features['Owner_Type'].map(owner_dict)

    prediction = Model.predict(features)[0]
    return prediction

# Predict button
if st.sidebar.button("Predict"):
    if Make and Model and year and fuel and transmission and owner:
        make = Make_dict[Make]
        model = Model_dict[Model]
        year = year_dict[year]
        fuel = fuel_dict[fuel]
        transmission = transmission_dict[transmission]
        owner = owner_dict[owner]

        predicted_price = predict_price(make, model, year, fuel, transmission, km_driven, owner)
        st.write(f"Predicted Price: ₹{predicted_price:.2f}")
    else:
        st.write("Please fill in all the details to get a prediction.")
