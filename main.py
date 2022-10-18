import mysql.connector
from mysql.connector import Error
import streamlit as st
import time
connection = mysql.connector.connect(host='localhost',port=3308,database='DoctorPres',user='ala',password='ala')
print("Connected to Server - DoctorPres")
mycursor = connection.cursor()

st.header("Doctor Prescription System")
st.title("Medicine List")
patient_name=st.text_input("Enter Patient Name")
st.write("You entered:",patient_name)
patient_age=st.text_input("Enter Patient Age")
st.write("You entered:",patient_age)
symptoms=st.text_input("Please enter your symptoms")
st.write("You entered",symptoms)

# mycursor.execute("SELECT * FROM `Medicine`;")
# myresult = mycursor.fetchall()
# st.dataframe(myresult)
