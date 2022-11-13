import os
import random

import pymysql
import streamlit as st

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
# GUI Login Screen
st.header("Doctor Prescription System")
st.write("# Dashboard")
st.write("## Create Prescription")
st.sidebar.header("Doctor Prescription System")
st.sidebar.button("Create Prescription")
st.sidebar.button("Medicines")
update=st.sidebar.button("Update Prescription")
if update:
    st.write("## Update Prescription")
    pat_id = st.text_input("Enter Patient ID")
    st.write("## Enter Medicines")
    med1 = st.selectbox("Medicine 1", result)
    med2 = st.selectbox("Medicine 2", result)
    med3 = st.selectbox("Medicine 3", result)
    update_pres = st.button("Confirm")
    if update_pres:
        query2 = "UPDATE PatientPres SET Medicine_1='%s',Medicine_2='%s',Medicine_3='%s' WHERE Pat_ID='%s'" % (
            med1, med2, med3, pat_id)
        cursor.execute(query2)
        st.success("Prescription Updated")
        st.balloons()
        os.system("streamlit run pres.py")
with st.form("my_form"):
    patient_id = random.randint(1000, 9999)
    patient_name = st.text_input("Patient Name")
    patient_age = st.text_input("Patient Age")
    medicine_1 = st.selectbox("Medicine 1", result[0:747])
    medicine_1 = medicine_1.split(" ")[0]
    st.write("Medicine 1", medicine_1)
    medicine_2 = st.selectbox("Medicine 2", result[0:747])
    medicine_2 = medicine_2.split(" ")[0]
    st.write("Medicine 2", medicine_2)
    medicine_3 = st.selectbox("Medicine 3", result[0:747])
    medicine_3 = medicine_3.split(" ")[0]
    st.write("Medicine 3", medicine_3)
    button = st.form_submit_button("Submit")
    if button:
        st.write("Thank you for submitting the form")
        query2 = 'INSERT INTO `PatientPres`(`Pat_ID`, `Pat_Name`, `Pat_Age`, `Medicine_1`,`Medicine_2`,`Medicine_3`) VALUES (%s,"%s",%s,"%s","%s","%s");' % (
        patient_id, patient_name, patient_age, medicine_1, medicine_2, medicine_3)
        cursor.execute(query2)
        st.write("Added to database")
        os.system("streamlit run pres.py")
