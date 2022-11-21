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


def update_pres():
    with st.expander("View Patient's Data"):
        view_query = "SELECT Pat_ID,Pat_Name,Medicine_1,Medicine_2,Medicine_3 FROM PatientData"
        cursor.execute(view_query)
        view_result = cursor.fetchall()
        st.dataframe(view_result)
    query = "SELECT `Medicine Name` FROM MedicineDB"
    cursor.execute(query)
    result = cursor.fetchall()
    result = [i['Medicine Name'] for i in result]
    pat_query = "SELECT `Pat_ID` FROM PatientData"
    cursor.execute(pat_query)
    pat_result = cursor.fetchall()
    pat_result = [i['Pat_ID'] for i in pat_result]
    # st.write("## Update Datacription")
    pat_id = st.selectbox("Patient ID", pat_result)
    # st.write("## Enter Medicines")
    med1 = st.selectbox("Medicine 1", result)
    med2 = st.selectbox("Medicine 2", result)
    med3 = st.selectbox("Medicine 3", result)
    update_Data = st.button("Confirm")
    if update_Data:
        query2 = "UPDATE PatientData SET Medicine_1='%s',Medicine_2='%s',Medicine_3='%s' WHERE Pat_ID='%s'" % (
            med1, med2, med3, pat_id)
        cursor.execute(query2)
        st.success("Description Updated")
