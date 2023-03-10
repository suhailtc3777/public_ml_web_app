# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:57:03 2023

@author: suhail
"""
import pandas as pd
import numpy as np
import pickle
import streamlit as st

#load saved model
load_model = pickle.load(open("finalized_model.sav","rb"))

# Creating a function for prediction
    
def telecom_pred(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person will not be churned'
    else:
      return 'The person will be churned'
  
def main():
    
    # giving a titile
    #st.title("telecom Churn Prediction")
   
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Telcecom churn app </h2>
    </div>
    """
    
    # getting the input data from user
    st.markdown(html_temp,unsafe_allow_html=True)
    account_length = st.sidebar.slider("Account Length",1,243)
    voice_plan = st.sidebar.radio("Voice_plan",[0,1])
    voice_messages = st.sidebar.slider("Voice_message",0,52)
    intl_plan = st.sidebar.radio("International_plan",[0,1])
    customer_calls = st.sidebar.slider("Customer_service_calls",0,9)
    total_charges= st.sidebar.slider("total_charges",22,96)
    total_calls= st.sidebar.slider("total_calls",191,416)
    total_mins= st.sidebar.slider("total_minutes",284,885)

  
       
    
    st.subheader('User Input parameters')
    #st.write({'Account Length':account_length},{'Voice Mail Plan':voice_plan},{'Voice Mail Message':voice_messages},{'Internation Plan':intl_plan},{'Customer Calls':customer_calls},{'Total Charge':total_charges},{'total calls':total_calls},{'total minutes':total_mins})   
    st.write(pd.DataFrame({
    'Account Length': [account_length],
    'Voice Mail Plan': [voice_plan],
    'Voice Mail Messages': [voice_messages],
    'international Plan': [intl_plan],
    'Customer Calls': [customer_calls],
    'Total Charges': [total_charges],
    'Total Calls': [total_calls],
    'Total minutes': [total_mins]}))
    
    
    #account_length = st.text_input("Account Length")
    #voice_plan = st.text_input("Voice plan")
    #voice_messages = st.text_input("Voice Messages")
    #intl_plan = st.text_input("International Plan")
    #customer_calls = st.text_input("Customer Calls")
    #total_charges = st.text_input("Total Charges")
    #total_calls = st.text_input("total calls")
    #total_mins = st.text_input("Total Minutes")
    
    # code for prediction
    tele_churn = " "
    
    # creating a Button for prediction
     
    if st.button("Submit"):
        tele_churn = telecom_pred([account_length,voice_plan,voice_messages,intl_plan,customer_calls,total_charges,total_calls,total_mins])
    
    
    st.success(tele_churn)
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    