import streamlit as st
import pickle
import os
import numpy as np

st.sidebar.title("Vijay Used Car Price Prediction!!!")

# Dictionaries for mapping inputs
Make_dict = {'Maruti': 0, 'Hyundai': 1, 'Datsun': 2, 'Honda': 3, 'Tata': 4, 'Chevrolet': 5, 'Toyota': 6, 'Jaguar': 7, 'Mercedes-Benz': 8, 'Audi': 9, 'Skoda': 10, 'Jeep': 11, 'BMW': 12, 'Mahindra': 13, 'Ford': 14, 'Nissan': 15, 'Renault': 16, 'Fiat': 17, 'Volkswagen': 18, 'Volvo': 19, 'Mitsubishi': 20, 'Land': 21, 'Daewoo': 22, 'MG': 23, 'Force': 24, 'Isuzu': 25, 'OpelCorsa': 26, 'Ambassador': 27, 'Kia': 28}
Model_dict = { ... }  # Include the full Model_dict here
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
        model_path = 'LinearRegression.pkl'
        if not os.path.exists(model_path):
            st.error(f"Model file not found. Please ensure '{model_path}' is in the correct path.")
        else:
            with open(model_path, 'rb') as file:
                Model = pickle.load(file)
            
            # Ensure the features array is 2D as expected by the model
            Features = np.array(Features).reshape(1, -1)
            prediction = Model.predict(Features)[0]

            st.markdown(f"<h2 style='text-align: center; color: #6A3BFF;'>Vijay Used Car Price Prediction</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center; color: #6A3BFF;'>Your Approximate Car Price is Rs. {round(prediction)}/-</h3>", unsafe_allow_html=True)
            st.image("car.png", width=200, caption="Drive Safe!", use_column_width=True)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.markdown(f"<h2 style='text-align: center; color: white;'>Enter all the values to get your car price</h2>", unsafe_allow_html=True)
