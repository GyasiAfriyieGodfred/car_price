# importing the libraries

import streamlit as st
import time as t
import pandas as pd
import joblib

# importing saved the model
model = joblib.load('car_price_predictor')

# setting the page configuration
st.set_page_config(layout='wide',initial_sidebar_state='expanded') #for full screen widget

# making the string input for car_make, numeric for the ml model
car_make = {'Porsche':23,'Lamborghini':14,'Ferrari':10,'Audi':5,'McLaren':18,'BMW':6,
             'Mercedes-Benz':20, 'Chevrolet':8, 'Ford':11, 'Nissan':21, 'Aston Martin':4,
             'Dodge':9, 'Jaguar':12, 'Lexus':15, 'Lotus':16, 'Maserati':17,'Alfa Romeo':1,
             'Ariel':3, 'Bentley':7, 'Mercedes-AMG':19, 'Polestar':22, 'Acura':0,
       'Rolls-Royce':24, 'Toyota':27, 'TVR':26, 'Subaru':25, 'Kia':13, 'Alpine':2}


st.title('Car Price Prediction :car:')
with st.sidebar:
    st.header('Input Car Specification')

    carmake = st.selectbox('Choose Car Preference',options=list (car_make.keys()))
    engine_size = st.number_input('Engine Size',key ="input1")
    horse_power = st.number_input('Horse Power',key ="input2")
    Torque= st.number_input('Torque',key ="input3")
    MPH_time=  st.number_input('MPH_Time',key ="input4")
    Age = st.slider('Age',0,15,30)

your_data = {'car_make': carmake,
          'Engine size':engine_size,
          'horsepower':horse_power,
         'Torque':Torque,
         'MPH_Time':MPH_time,
        'Age':Age,
        
          }


# making the car_make input a numeric value for the model
your_data_entry = pd.DataFrame(your_data, index=[0])
your_data_entry['car_make'].replace(['Porsche','Lamborghini','Ferrari','Audi','McLaren','BMW',
             'Mercedes-Benz', 'Chevrolet', 'Ford', 'Nissan', 'Aston Martin',
             'Dodge', 'Jaguar', 'Lexus', 'Lotus', 'Maserati','Alfa Romeo',
             'Ariel', 'Bentley', 'Mercedes-AMG', 'Polestar', 'Acura',
       'Rolls-Royce', 'Toyota', 'TVR', 'Subaru', 'Kia', 'Alpine'],
       (23,14,10,5,18,6,20,8,11,21,4,9,12,15,16,17,1,3,7,19,22,0,24,27,26,25,13,2)
,inplace=True)

st.write(your_data_entry)


# creating a button for the prediction

if st.button('Your Car Price'):
    with st.spinner('processing....please wait'):
        t.sleep(3)    
    price=model.predict(your_data_entry)  
    st.write(price)     
    st.success('Thank You for the purchase') 
    st.balloons()
    
    
st.markdown('---')
# st.divider()
st.markdown("[***Powered By DolphWhale Technologies***](https://youtube.com)")
st.markdown('```Email: gyasi.afriyie@gmail.com```')