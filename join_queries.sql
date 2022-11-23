-- Simple Join
SELECT * FROM PatientPres JOIN PatientData WHERE PatientPres.Pat_Age = PatientData.Pat_Age;

-- INNER JOIN
SELECT * FROM PatientPres INNER JOIN PatientData ON PatientPres.Pat_Age = PatientData.Pat_Age;

-- LEFT JOIN
SELECT * FROM PatientPres LEFT JOIN PatientData ON PatientPres.Pat_Age = PatientData.Pat_Age;

-- RIGHT JOIN
SELECT * FROM PatientPres RIGHT JOIN PatientData ON PatientPres.Pat_Age = PatientData.Pat_Age;

-- CROSS JOIN
SELECT * FROM PatientPres CROSS JOIN PatientData;

-- UNION
SELECT Pat_Name FROM PatientPres UNION SELECT Pat_ID FROM PatientData;

-- UNION ALL
SELECT Pat_Name FROM PatientPres UNION ALL SELECT Pat_ID FROM PatientData;

-- INTERSECT
SELECT Pat_Name FROM PatientPres INTERSECT SELECT Pat_Name FROM PatientData;

-- EXCEPT
SELECT Pat_Name FROM PatientPres EXCEPT SELECT Pat_Name FROM PatientData;