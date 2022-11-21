-- COUNT (Number of Patients)
SELECT COUNT(Pat_ID) FROM PatientPres;

-- MIN (Patient with Minimum Age)
SELECT MIN(Pat_Age),Pat_Name FROM PatientPres;

-- MAX (Patient with Maximum Age)
SELECT MAX(Pat_Age),Pat_Name FROM PatientPres;

-- AVG (Average Patient Age that visits the Doctor)
SELECT AVG(Pat_Age) FROM PatientPres;
