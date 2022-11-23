DELIMITER $$
CREATE DEFINER=`ala`@`localhost` PROCEDURE `huge_payments`()
BEGIN
SELECT * FROM PatientBill WHERE PatientBill.Total>2000;
END$$
DELIMITER ;

DELIMITER $$
CREATE DEFINER=`ala`@`localhost` PROCEDURE `senior_citizens`()
BEGIN
	SELECT * FROM PatientData WHERE PatientData.Pat_Age > 60;
END$$
DELIMITER ;