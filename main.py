import streamlit as st
import time
import pymysql
import os
# config for the database
connection = pymysql.connect(host='localhost',
                             user='ala',
                             password='ala',
                             db='DoctorPres',
                             cursorclass=pymysql.cursors.DictCursor)
connection.autocommit(True)
cursor = connection.cursor()
query = "SELECT `Medicine Name` FROM MedicineDB"
cursor.execute(query)
result = cursor.fetchall()
st.write(result)
result = [i['Medicine Name'] for i in result]
st.write(result)
# GUI Login Screen
st.header("Doctor Prescription System")
st.write("## Dashboard")
st.sidebar.header("Navbar")
button_pres = st.button("Create Patient Prescription")
if button_pres:
    with st.form("my_form"):
        patient_name = st.text_input("Patient Name")
        patient_age = st.text_input("Patient Age")
        medicine_1 = st.selectbox("Medicine 1",result[0:747])
        button=st.form_submit_button("Submit")
