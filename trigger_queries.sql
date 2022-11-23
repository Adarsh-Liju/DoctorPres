CREATE TRIGGER `age_verify` BEFORE INSERT ON `PatientPres`
 FOR EACH ROW IF new.`Pat_Age` < 18 then set new.`Adult` = 'C';
ELSEIF new.`Pat_Age` > 18 then set new.`Adult` = 'A';
END IF
