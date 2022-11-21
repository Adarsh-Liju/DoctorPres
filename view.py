import os
import random
import pymysql
import streamlit as st
import matplotlib.pyplot as plt
# config for the database
connection = pymysql.connect(host='localhost',
                             user='ala',
                             password='ala',
                             db='DoctorPres',
                             cursorclass=pymysql.cursors.DictCursor)
connection.autocommit(True)
cursor = connection.cursor()


def view_pres():
    query = "SELECT `Pat_ID`,`Pat_Name`,`Pat_Age`,`Medicine_1`,`Medicine_2`,`Medicine_3`,Date(`Date`) FROM `PatientData`;"
    cursor.execute(query)
    result = cursor.fetchall()
    with st.expander("View All Prescriptions"):
        st.subheader("Prescriptions")
        st.table(result)

    Pat_ID = st.text_input("Enter Patient ID")
    if Pat_ID:
        query = "SELECT `Pat_ID`,`Pat_Name`,`Pat_Age`,`Medicine_1`,`Medicine_2`,`Medicine_3`,Date(`Date`) FROM `PatientData` WHERE `Pat_ID` = %s;"
        cursor.execute(query, Pat_ID)
        result = cursor.fetchall()
        query2 = "SELECT `Pat_ID`,`Pat_Name`,`Pat_Age`,`Medicine_1`,`Medicine_2`,`Medicine_3`,Date(`Date`) FROM `PatientData` WHERE `Pat_ID` = %s;"
        cursor.execute(query2, Pat_ID)
        result2 = cursor.fetchall()
        st.table(result2)


def plot_pres():
    query = "SELECT Pat_Age FROM PatientData;"
    cursor.execute(query)
    result = cursor.fetchall()
    st.subheader("Patient Age Graph")
    st.bar_chart(result)
    st.subheader("Adult and Child Ratio")
    query2 = "SELECT COUNT(*) FROM PatientData WHERE Pat_Age>18;"
    cursor.execute(query2)
    result2 = cursor.fetchone()
    query3 = "SELECT COUNT(*) FROM PatientData WHERE Pat_Age<18;"
    cursor.execute(query3)
    result3 = cursor.fetchone()
    fig, ax = plt.subplots()
    ax.pie([result2["COUNT(*)"], result3["COUNT(*)"]], labels=["Adult", "Child"], autopct="%1.1f%%")
    st.pyplot(fig)
