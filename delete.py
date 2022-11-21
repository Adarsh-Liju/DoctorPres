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
def delete_pres():
    query = "SELECT `PatID`,`Pat_Name`,`Pat_Age`,`Medicine_1`,`Medicine_2`,`Medicine_3` FROM `PatientPres`;"
    cursor.execute(query)
    result = cursor.fetchall()
    st.table(result)
    delete_id=st.text_input("Enter Patient ID to delete")
    delete=st.button("Delete")
    if delete:
        query2 = "DELETE FROM PatientPres WHERE PatID='%s'" % (delete_id)
        cursor.execute(query2)
        st.success("Patient Deleted")