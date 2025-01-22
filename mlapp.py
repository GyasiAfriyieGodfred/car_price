# importing the libraries

import streamlit as st
import time as t
import pandas as pd
import joblib
import os
import openpyxl 


# Initialize session state variables
if 'data' not in st.session_state:
    st.session_state.data = []

if 'price' not in st.session_state:
    st.session_state.price = None  # Initialize as none or an empty list

# importing the saved model
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

col1,col2 = st.columns(2,gap='small')
with col1:
    if engine_size ==0 and horse_power==0:
        st.warning('Please Enter engine_size and horse_power')
    else:

        # creating a button for the prediction

        if st.button('Your Car Price'):
            with st.spinner('processing....please wait'):
                t.sleep(3)    
            price=model.predict(your_data_entry)
            price =price.round(2)  # this is for rounding array or dataframe
            st.session_state['price'] = price
            st.write(f"Car Price: {price[0]}")     
            st.success('Thank You for the purchase')

        if 'your_data_entry' not in st.session_state:
            st.session_state.data = []

        if st.session_state.data:
                your_data_entry = pd.DataFrame(st.session_state.data)

# saving the numeric value of car_make as a string in excel file
# Reverse mapping dictionary to convert numeric car_make back to string
reverse_car_make = {v: k for k, v in car_make.items()}

# Convert numeric car_make back to string
your_data_entry['car_make'] = your_data_entry['car_make'].map(reverse_car_make)

# Combine your_data_entry and price
price_df = pd.DataFrame(st.session_state['price'], columns=['predicted_price'])
# input_and_price = pd.concat([your_data_entry, price_df], axis=1)

with col2:        
    

    if st.button('Save Data'):
         if st.session_state['price'] is None:
            st.error("No specifications entered. Please enter car specs!.")
         else:
    
        
            output_directory = 'C:\\Users\\LAPTOP\\Desktop\\streamlitTk_input' 
                # make  directory 
            os.makedirs(output_directory,exist_ok = True) #this creates a new directory 
                #specify the file  name
            filename= 'sportscardatainput.xlsx'
            file_path = os.path.join(output_directory,filename)

        # adding the your_data_entry and price 
            price_df = pd.DataFrame(st.session_state['price'],columns=['car_price'])  
            input_and_price = pd.concat([your_data_entry.reset_index(drop=True),price_df],axis=1) 

            if os.path.exists(file_path):
                # Read the existing data and append the new data
                try:
                     existing_data = pd.read_excel(file_path, engine='openpyxl')
                     updated_data = pd.concat([existing_data, input_and_price], ignore_index=True)
                except Exception as e:
                    st.error(f"Error reading the existing file: {e}")
                    st.stop()
            
            else:
            # If the file doesn't exist, use the new data
                updated_data = input_and_price
        
        # Save the updated data to the file
            try:
                updated_data.to_excel(file_path, index=False, engine='openpyxl')
                st.success("Data saved successfully ")
                st.balloons()
            except PermissionError:
                st.error("Permission denied while trying to write to the file. Ensure the file is closed.")

        
st.markdown('---')
# st.divider()
st.markdown("[***Powered By DolphWhale Technologies***](https://youtube.com)")
st.markdown('```Email: gyasi.afriyie@gmail.com```')