import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Calorie Calculator", page_icon="🔥")
model = pickle.load(open('model.pkl','rb'))
st.title("Calories Burned Calculator")
gender = st.selectbox("Select Gender",("Male","Female"))
if (gender == "Male"):
    g = 0
else:
    g = 1
age = st.number_input("Enter age: ")
height = st.number_input("Enter Height (cms): ")
weight = st.number_input("Enter Weight (kg): ")
duration = st.slider("Enter Workout Duration (mins): ",min_value=0,max_value=180)
heartrate = st.number_input("Enter HeartRate (bpm): ")
bodytemp = st.number_input("Enter Body Temperature (°C): ")
prediction = model.predict(pd.DataFrame(columns = ['Gender','Age','Height','Weight',
                                                   'Duration','Heart_Rate','Body_Temp'],
                                        data = np.array([g,age,height,weight,duration,heartrate,bodytemp]).reshape(1,7)))
if st.button("Predict"):
    st.success(f"🔥 Calories burned:  {prediction[0]} kcal")