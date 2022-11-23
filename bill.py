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
def bill_pres():
  st.header("Bill")
  st.header("Enter the Patient ID")
  Pat_ID = st.text_input("Patient ID")
  query="SELECT `Pat_Name`,`Pat_Age`,`Medicine_1`,`Medicine_2`,`Medicine_3` FROM `PatientData` WHERE `Pat_ID` = %s;"
  cursor.execute(query, Pat_ID)
  result = cursor.fetchall()
  st.table(result)
  st.header("Enter the Doctor's Fee")
  doc_fee = st.number_input("Doctor's Fee",min_value=50,max_value=1000000,step=50)
  doc_fee = float(doc_fee)
  st.write("### Doctor's Fee: ",doc_fee)
  medicine_1 = result[0]['Medicine_1']
  medicine_2 = result[0]['Medicine_2']
  medicine_3 = result[0]['Medicine_3']
  query3="SELECT `MRP` FROM `MedicineDB` WHERE `Medicine Name` = %s;"
  cursor.execute(query3, medicine_1)
  result3 = cursor.fetchone()
  st.write("### Cost of Medicine 1 : ",result3.get('MRP'))
  query4="SELECT `MRP` FROM `MedicineDB` WHERE `Medicine Name` = %s;"
  cursor.execute(query4, medicine_2)
  result4 = cursor.fetchone()
  st.write("### Cost of Medicine 2 : ",result4.get('MRP'))
  query5="SELECT `MRP` FROM `MedicineDB` WHERE `Medicine Name` = %s;"
  cursor.execute(query5, medicine_3)
  result5 = cursor.fetchone()
  st.write("### Cost of Medicine 3 : ",result5.get('MRP'))
  total = float(result3.get('MRP')) + float(result4.get('MRP')) + float(result5.get('MRP')) + doc_fee
  st.write("# Total Bill: ",total)
  but1=st.button("Generate Bill")
  if but1:
    query2="INSERT INTO `PatientBill` (`Pat_ID`,`Medicine_1`,`Medicine_2`,`Medicine_3`,`Cost_1`,`Cost_2`,`Cost_3`,`Doctor_Fees`,`Total`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(query2, (Pat_ID,medicine_1,medicine_2,medicine_3,result3.get('MRP'),result4.get('MRP'),result5.get('MRP'),doc_fee,total))
    st.success("Bill Generated Successfully")
