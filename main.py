import os
import random
from delete import delete_pres
import pymysql
import streamlit as st
crud=["Create","Read","Update","Delete"]
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
option=st.sidebar.selectbox("Operations", crud)
print(option)
if option=="Update":
    pass
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

if option=="Delete":
    delete_pres()