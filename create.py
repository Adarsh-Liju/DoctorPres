import os
import random
import pymysql
import streamlit as st
import time
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
result = [i['Medicine Name'] for i in result]

date = time.strftime("%d-%m-%Y")


def create_pres():
    with st.form("my_form"):
        patient_id = random.randint(1000, 9999)
        patient_name = st.text_input("Patient Name")
        patient_age = st.text_input("Patient Age")
        symptoms = st.text_area("Symptoms")
        prescription = st.text_area("Prescription")
        button = st.form_submit_button("Submit")
        if button:
            st.write("Thank you for submitting the form")
            query2 = 'INSERT INTO PatientData (Pat_ID,Pat_Name,Pat_Age,Symptoms,Prescription) VALUES ("%s","%s","%s","%s","%s")'
            cursor.execute(query2 % (patient_id, patient_name,patient_age, symptoms, prescription))

            st.write("### Your Patient ID is ", patient_id)
            st.success("Added to database")
