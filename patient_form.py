import streamlit as st
import time
import pymysql
import os
# DBMS part

# config for the database
connection = pymysql.connect(host='localhost',
                             user='ala',
                             password='ala',
                             db='DoctorPres',
                             cursorclass=pymysql.cursors.DictCursor)
connection.autocommit(True)
cursor = connection.cursor()
# GUI part
with st.form("my_form", clear_on_submit=True):
    st.title("Patient Detail Form")
    patient_name = st.text_input("Enter Patient Name")
    patient_age = st.text_input("Enter Patient Age")
    symptoms = st.text_input("Please enter your symptoms")
    address= st.text_input("Please enter your address")
    # TODO 
    # Will add upload image later
    # camera=st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("### Thank you for your response :-) ")
        st.write("This is to test my db is working")
        query = "INSERT INTO `PatientDB`(`Name`, `Age`, `Symptoms`,`Address`) VALUES ('%s','%s','%s','%s')" % (patient_name, patient_age, symptoms,address)
        cursor.execute(query)

