import streamlit as st
import pickle
import numpy as np

car = pickle.load(open(r'C:/Users/HP/Documents/CSV files/car3.pkl', 'rb'))


def main():
    st.title("Toyota Car Prediction App")
    model = st.radio("pick your model", [' GT86', ' Corolla', ' RAV4', ' Yaris', ' Auris', ' Aygo', ' C-HR',
       ' Prius', ' Avensis', ' Verso', ' Hilux', ' PROACE VERSO',
       ' Land Cruiser', ' Supra', ' Camry', ' Verso-S', ' IQ',
       ' Urban Cruiser'])
    if model == 'Land Cruiser':
        model_Land_Cruiser = 1
    else:
        model_Land_Cruiser = 0
    if model == 'C-HR':
        model_C_HR = 1
    else:
        model_C_HR = 0
    if model == 'Prius':
        model_Prius = 1
    else:
        model_Prius = 0
    if model == 'RAV4':
        model_RAV4 = 1
    else:
        model_RAV4 = 0   
    year = st.slider("year", 1998, 2020)
    transmission = st.selectbox("transmission", ['Automatic', 'Manual', 'Other', 'Semi-Auto'])
    if transmission == 'Manual':
        transmission_Manual= 1
    else:
        transmission_Manual= 1
    mileage = st.slider("mileage", 50 , 100000)
    tax = st.slider("tax", 0 , 30000)
    mpg = st.slider("mpg", 0 , 100000)
    engineSize = st.slider("engine size", 0, 10)
    
    if st.button('Predict'):
        pred = car.predict([[year, mileage, tax, mpg, engineSize, model_C_HR, model_Land_Cruiser, model_Prius, model_RAV4, transmission_Manual]])
        st.success("The price of your car is {}".format(pred)) 
if __name__ == '__main__':
    main()