import pymysql
import streamlit as st
import os
import random
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
