# DBMS Project Report - Doctor Prescription System

- [DBMS Project Report - Doctor Prescription System](#dbms-project-report---doctor-prescription-system)
  - [**Short Description and Scope of the Project**](#short-description-and-scope-of-the-project)
  - [**ER Diagram**](#er-diagram)
  - [**Relational Schema**](#relational-schema)
  - [**DDL statements - Building the database**](#ddl-statements---building-the-database)
  - [**Populating the Database**](#populating-the-database)
  - [**Join Queries**](#join-queries)
- [Aggregate Functions](#aggregate-functions)
- [Set Operations](#set-operations)
- [Functions and Procedures](#functions-and-procedures)
- [Triggers and Cursors](#triggers-and-cursors)
- [Frontend](#frontend)
    - [Home Page - Create Operation](#home-page---create-operation)
    - [Read Operation](#read-operation)
    - [Update Operation](#update-operation)
    - [SQL Query Page](#sql-query-page)
    - [Bill Page](#bill-page)


## **Short Description and Scope of the Project**

The main agenda of this project is to make a fast,responsive and robust Doctor Prescription System whereby Doctors can issue medicines and give advice in the form of prescription to Patients

Most of the already existing systems are handwritten and do not have a proper database for storing Doctor’s Prescriptions and Bills. Storing in a database has a lot of advantages as the entire system is digitalized and electronically stored for future purposes.

Due to the scaling properties of MySQL this system can work with a very large amount of data. Triggers and Procedures help in easing a lot of jobs that were initially cumbersome and tedious.

## **ER Diagram**

![Untitled](DBMS%20Project%20Report%20-%20Doctor%20Prescription%20System%2093125754905e43fd9a1b8859cef1089e/Untitled.png)

## **Relational Schema**

![Untitled](DBMS%20Project%20Report%20-%20Doctor%20Prescription%20System%2093125754905e43fd9a1b8859cef1089e/Untitled%201.png)

## **DDL statements - Building the database**

```sql
CREATE TABLE `DoctorDB` (  `Pat_ID` int(11) NOT NULL,  `Doc_id` int(11) NOT NULL,  `Name` text NOT NULL,  `Qualification` text NOT NULL,  `Signature` longblob NOT NULL,  `Age` int(11) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;CREATE TABLE `ExpiredDB` (  `Pat_ID` int(11) NOT NULL,  `Name` text DEFAULT NULL,  `Age` int(11) DEFAULT NULL,  `Address` text DEFAULT NULL,  `Symptoms` text DEFAULT NULL,  `Medicines` text DEFAULT NULL,  `Prescription` text DEFAULT NULL,  `Timestamp` date NOT NULL DEFAULT current_timestamp()) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;CREATE TABLE `LoginCreds` (  `user_name` varchar(6) DEFAULT NULL,  `user_pwd` varchar(6) DEFAULT NULL,  `access` int(1) DEFAULT NULL,  `user_id` int(1) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8;---- Table structure for table `MedicineDB`--CREATE TABLE `MedicineDB` (  `ID` int(3) DEFAULT NULL,  `Medicine Name` varchar(53) DEFAULT NULL,  `Prescription` varchar(21) DEFAULT NULL,  `Type of Sell` varchar(35) DEFAULT NULL,  `Manufacturer` varchar(44) DEFAULT NULL,  `Salt` varchar(142) DEFAULT NULL,  `MRP` varchar(8) DEFAULT NULL,  `Uses` varchar(242) DEFAULT NULL,  `Alternate Medicines` varchar(230) DEFAULT NULL,  `Side Effects` varchar(324) DEFAULT NULL,  `How to Use` varchar(397) DEFAULT NULL,  `Chemical Class` varchar(59) DEFAULT NULL,  `Habit Forming` varchar(3) DEFAULT NULL,  `Therapeutic Class` varchar(27) DEFAULT NULL,  `Action Class` varchar(63) DEFAULT NULL,  `How It Works` varchar(1034) DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8;CREATE TABLE `PatientBill` (  `Pat_ID` int(11) DEFAULT NULL,  `Bill_ID` int(11) NOT NULL,  `Medicine_1` text NOT NULL,  `Medicine_2` text NOT NULL,  `Medicine_3` text NOT NULL,  `Cost_1` int(11) NOT NULL,  `Cost_2` int(11) NOT NULL,  `Cost_3` int(11) NOT NULL,  `Doctor_Fees` int(11) NOT NULL,  `Total` int(11) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;CREATE TABLE `PatientData` (  `Pat_ID` int(11) NOT NULL,  `Pat_Name` text DEFAULT NULL,  `Pat_Age` int(11) DEFAULT NULL,  `Adult` char(11) DEFAULT NULL,  `Symptoms` text DEFAULT NULL,  `Prescription` text DEFAULT NULL,  `Medicine_1` text DEFAULT NULL,  `Medicine_2` text DEFAULT NULL,  `Medicine_3` text DEFAULT NULL,  `Timestamp` time DEFAULT current_timestamp()) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;---- Indexes for table `DoctorDB`--ALTER TABLE `DoctorDB`  ADD PRIMARY KEY (`Pat_ID`),  ADD UNIQUE KEY `Doc_id` (`Doc_id`);---- Indexes for table `ExpiredDB`--ALTER TABLE `ExpiredDB`  ADD PRIMARY KEY (`Pat_ID`);---- Indexes for table `LoginCreds`--ALTER TABLE `LoginCreds`  ADD PRIMARY KEY (`user_id`);---- Indexes for table `PatientBill`--ALTER TABLE `PatientBill`  ADD PRIMARY KEY (`Bill_ID`);---- Indexes for table `PatientData`--ALTER TABLE `PatientData`  ADD PRIMARY KEY (`Pat_ID`);---- AUTO_INCREMENT for dumped tables------ AUTO_INCREMENT for table `DoctorDB`--ALTER TABLE `DoctorDB`  MODIFY `Doc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;---- AUTO_INCREMENT for table `PatientBill`--ALTER TABLE `PatientBill`  MODIFY `Bill_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;COMMIT;
```

## **Populating the Database**

```sql
INSERT INTO `DoctorDB` (`Pat_ID`, `Doc_id`, `Name`, `Qualification`, `Signature`, `Age`) VALUES(4160, 2, 'Aditya Balasubramaniyam', '- Medicine \r\n- MBBS', 0x89504e470d0a1a0a0000000d494844520000011d000000b10803000000ce1d996800000087504c5445ffffff000000f9f9f9131313f2f2f2b1b1b1e7e7e7f7f7f7bdbdbdeeeeeed7d7d7929292dbdbdbc0c0c03a3a3ad0d0d0adadad8585857f7f7f6868689c9c9c6363631a1a1ae1e1e1d1d1d1414141535353a5a5a5080808b7b7b77777772a2a2a3131314d4d4d8d8d8d7070702222227b7b7b6565655b5b5b2e2e2e9f9f9f4949491717173e3e3e294054b50000081649444154789ced9de97ab23a10801d3617764529105750d4cffbbfbe835a95bd04ec699cf0fe6a2df8847432992dc360d0d3d3d3d3d3d3d3d3d3c31c4359b5d5787b9a9e96da5f8f852934278ed600b039fb61ec19c94f33fdafc7c406da68954c87b1b226d2f33377b90732fac341b1816627222386cb71e12fc20e7ca9e40e6e180676323576d51a1a47c0affed16700c436eb2e09a128533c203889ae99d74ecd15fffc7f0c8631a4bd088b5303b91040fdfdd1b0c570976cdd56b36b2de04b332b7b80ed8f4bea015fc223257373a631f466c6af8d85390280359d916773b3b4cc0d2c1cca7b0268bc0a3f1a2906b0a9efb2800b876b94281c97feb68087d9917c00da4575c3e6607646225cdaf94c536821701f85b06f2938091b10de3a16e6d0d660b4158009f86f1d0b735800bbd637071deefd046ce8a2572ff0f5bea13087e043d441ad9a00ef1b0b732847d876d1aa67cc4ea84620ec727f223a78bdac09e9f8af3fc3f44d43610f193a4ece124079d358982300083a7d81f0afe317304cf28f6f181dad620febf70c853d12852a77fe06ac0ea8d95972060bb27acb50d84369ef763e58a15d5782d1cdce49d0f1aeab10b61dbf411049d7f96595252c861dbf624e48d7af6094318149db7bbf1d070b006bf54edc3a26a35feeda460212bf73440ca1b7de6c4280687b8d23c70048d79510b5dc6c861eb97a0e575340ed6a49328b05ed1685b0116f71b2f87a3bda9a2fa35d6a573044e356d033c75c5620b74c22c424ba573bc5de3b87c318b3765bb14da2ef508e8778768476bb8d0ccff252cc299a2f6853073979197f63b4eed5e05a69d126586a88cf6085893945b36b63a9d864f3fc599dbf6f30cc61b7d8cf7548d5b47b5d83662ce3d067762591a482eba80be146f46984b9985a4c13cc6a27793adad9d133c1a0e9feadc3610ddac2496193398725620debdc0945baeba719a75541bdb0ae4b8bca9ad3205317b8c31a4c7ee051f9d831c9647616cbf70e86395ca078c2256cd2bf4eb086045fa81435375ed6bc99625f580946e364969d0baea34d44a4909a7aa20a904c4da14e7e6338aca1343409e7623696e3a32dd7c9a0340a6169909595312f2788dd265506b9dd7c60d5c54c5d0fd1d429d18fc17793fccb7e10d5099c07a8aa79663fc532ceb946177addc2da01b2d04650bf752df3552c871ae1b06041e9bf318f7259d71c02588b59d91ad7d8d81a44223e43f1541dcf90c54beeda4bf98509c335f130a62aa47945145e58e4f5484d597b0cd671f1ce61318329aecbd4a92ee6b4cea8baacdd01798c6bc74a61c1b6a87e36f995b2ad7c7c33b1bc97780d45418569ce6d9749cef2732bf5ca188cc43ce85aa5c932d20ad4cc31ad23c92db77d5475afb11d264a097396ebd639457dc9cf88e42c69a172739b5ef591823eb4e1a6e46726e66c1bab4a27ebb779d1396800a6ccbee567029bdc9fd615b6def82e532af643e937dc03a8891699e55b099a55b5099b7b9a34e4222c76931f472f14cfed2bd258f6f7e73ee6c28c0c4a0862fefc4d859dfc4ccaa33d8b540288b9c8aa5e1e9d709f9386b95a2e874566ee3c333fdb63e985e4b99e309f4acfb15e7c25ebebf09a1fb7fca49b1f3f537f2d7a3e7d283ab92f93c9997c3b0fa7d2f4e02e9517457c2c3d47fc3c9e6412e366e41dcb76a4515a1755bba8c818432aca25c37c9cb809250b4bcb58402be44d789e3824fdd8c31d9c9c12f75cca6a9a13b6a07215a298750a94399418c2976c4db889b7e34306bd18e40308f37529879cac0c9147301e8405c32ff1c277b974c4ea5fdee98cf165244a1016056f5b25e3c1e418a73675a718af5872e1a42f49c172896f8672aa467e59e65770612dfba470167b715f34e6e3f947a5593f9903e1518ae793a4878739f4fcab72d62b423d067ecd1314cb9eb4d73a0ac57122391571b031feb57529b66f3053992a15aceaaab12fec610ca5e430b699aee6b6eb8edc9a30fb8531b1835a62d42929251c406dd18f12632c35787229cbf7be7cd055f2f0f5b99900440b6b0342170e259faebe4f0e4cd6b7d046505f0b3ef2e1a29a187777a7d492b9d7a76ab3874e0a7f386721988e0fb099ada653542940af5c2c64589c09bcb2a39b261dc314d7c5d5b35ba9da905cc74fbf0a4969dfdbe88359363d14297392f9cc1037ee5f6f60edbe538d50ba63956222ee1b5c814e11df8bb9c9d03cd853285b973be18968f20adee9d7c6c12413aa9a5aabb28c102701cd61da8184fefd2c597c3a55e2776db1fb59a45aec3441c55ca05cc0a42c32313988b2bfd8897487cfc6a8dfd09267bba1bc814a897f3a507dfaaa9c0b476af98bbab6cd6bec957d3ef46f6e8cb92915bc06d469a39c31fae4de0b83ba2793c7cfec08f4ef0858f3a39527f4efdec09e174e21d35b2ff88b0a9ed8d42ef784236b30a68ef5051c791246f931911a0e58df275144a057b1848f364e5724eae6a73ce56c26d4bd73a6c83b7aa6b1a8fd087e8e1c5d6787f28611470b6be0d036e8bcf01455de531655e85cd5a8ac285b0b5df8f1b112c20dd5e54bbe527d33ba1d28e268c34a3850d50c4cb1be27b482034d34e28b23fff34648b141b7f0c93e1c9a5ef621defe67159c9a37887138393d9c426ebcb24caeecc03b5a533f4ba37f0bcee72334f4b34a7b3ee0476c14c150f869249361d564c1689c4ece406ff0964bdaea3044fc6cc4b47b1d220ec29f1e7dca5176afc00f7bbab289b83302d3cceb8447e529c85e86549d96d08ec85e86d002bdc222540e68df144f43b028c9c2b80708394aced420175a488fb6b0e35a1ba7718db5fcb47b94d10ca2532f3729f40344a1ad3a7b0fc03bf56253409397b213e8bc05007b7a7a7a7a7a7a7a7a7a7a7ab8e53fa15856724ce659ad0000000049454e44ae426082, 30),(7014, 4, 'A.K Goyal', '- MBBS \r\n- MD', 0x89504e470d0a1a0a0000000d494844520000011d000000b10803000000ce1d996800000087504c5445ffffff000000f9f9f9131313f2f2f2b1b1b1e7e7e7f7f7f7bdbdbdeeeeeed7d7d7929292dbdbdbc0c0c03a3a3ad0d0d0adadad8585857f7f7f6868689c9c9c6363631a1a1ae1e1e1d1d1d1414141535353a5a5a5080808b7b7b77777772a2a2a3131314d4d4d8d8d8d7070702222227b7b7b6565655b5b5b2e2e2e9f9f9f4949491717173e3e3e294054b50000081649444154789ced9de97ab23a10801d3617764529105750d4cffbbfbe835a95bd04ec699cf0fe6a2df8847432992dc360d0d3d3d3d3d3d3d3d3d3c31c4359b5d5787b9a9e96da5f8f852934278ed600b039fb61ec19c94f33fdafc7c406da68954c87b1b226d2f33377b90732fac341b1816627222386cb71e12fc20e7ca9e40e6e180676323576d51a1a47c0affed16700c436eb2e09a128533c203889ae99d74ecd15fffc7f0c8631a4bd088b5303b91040fdfdd1b0c570976cdd56b36b2de04b332b7b80ed8f4bea015fc223257373a631f466c6af8d85390280359d916773b3b4cc0d2c1cca7b0268bc0a3f1a2906b0a9efb2800b876b94281c97feb68087d9917c00da4575c3e6607646225cdaf94c536821701f85b06f2938091b10de3a16e6d0d660b4158009f86f1d0b735800bbd637071deefd046ce8a2572ff0f5bea13087e043d441ad9a00ef1b0b732847d876d1aa67cc4ea84620ec727f223a78bdac09e9f8af3fc3f44d43610f193a4ece124079d358982300083a7d81f0afe317304cf28f6f181dad620febf70c853d12852a77fe06ac0ea8d95972060bb27acb50d84369ef763e58a15d5782d1cdce49d0f1aeab10b61dbf411049d7f96595252c861dbf624e48d7af6094318149db7bbf1d070b006bf54edc3a26a35feeda460212bf73440ca1b7de6c4280687b8d23c70048d79510b5dc6c861eb97a0e575340ed6a49328b05ed1685b0116f71b2f87a3bda9a2fa35d6a573044e356d033c75c5620b74c22c424ba573bc5de3b87c318b3765bb14da2ef508e8778768476bb8d0ccff252cc299a2f6853073979197f63b4eed5e05a69d126586a88cf6085893945b36b63a9d864f3fc599dbf6f30cc61b7d8cf7548d5b47b5d83662ce3d067762591a482eba80be146f46984b9985a4c13cc6a27793adad9d133c1a0e9feadc3610ddac2496193398725620debdc0945baeba719a75541bdb0ae4b8bca9ad3205317b8c31a4c7ee051f9d831c9647616cbf70e86395ca078c2256cd2bf4eb086045fa81435375ed6bc99625f580946e364969d0baea34d44a4909a7aa20a904c4da14e7e6338aca1343409e7623696e3a32dd7c9a0340a6169909595312f2788dd265506b9dd7c60d5c54c5d0fd1d429d18fc17793fccb7e10d5099c07a8aa79663fc532ceb946177addc2da01b2d04650bf752df3552c871ae1b06041e9bf318f7259d71c02588b59d91ad7d8d81a44223e43f1541dcf90c54beeda4bf98509c335f130a62aa47945145e58e4f5484d597b0cd671f1ce61318329aecbd4a92ee6b4cea8baacdd01798c6bc74a61c1b6a87e36f995b2ad7c7c33b1bc97780d45418569ce6d9749cef2732bf5ca188cc43ce85aa5c932d20ad4cc31ad23c92db77d5475afb11d264a097396ebd639457dc9cf88e42c69a172739b5ef591823eb4e1a6e46726e66c1bab4a27ebb779d1396800a6ccbee567029bdc9fd615b6def82e532af643e937dc03a8891699e55b099a55b5099b7b9a34e4222c76931f472f14cfed2bd258f6f7e73ee6c28c0c4a0862fefc4d859dfc4ccaa33d8b540288b9c8aa5e1e9d709f9386b95a2e874566ee3c333fdb63e985e4b99e309f4acfb15e7c25ebebf09a1fb7fca49b1f3f537f2d7a3e7d283ab92f93c9997c3b0fa7d2f4e02e9517457c2c3d47fc3c9e6412e366e41dcb76a4515a1755bba8c818432aca25c37c9cb809250b4bcb58402be44d789e3824fdd8c31d9c9c12f75cca6a9a13b6a07215a298750a94399418c2976c4db889b7e34306bd18e40308f37529879cac0c9147301e8405c32ff1c277b974c4ea5fdee98cf165244a1016056f5b25e3c1e418a73675a718af5872e1a42f49c172896f8672aa467e59e65770612dfba470167b715f34e6e3f947a5593f9903e1518ae793a4878739f4fcab72d62b423d067ecd1314cb9eb4d73a0ac57122391571b031feb57529b66f3053992a15aceaaab12fec610ca5e430b699aee6b6eb8edc9a30fb8531b1835a62d42929251c406dd18f12632c35787229cbf7be7cd055f2f0f5b99900440b6b0342170e259faebe4f0e4cd6b7d046505f0b3ef2e1a29a187777a7d492b9d7a76ab3874e0a7f386721988e0fb099ada653542940af5c2c64589c09bcb2a39b261dc314d7c5d5b35ba9da905cc74fbf0a4969dfdbe88359363d14297392f9cc1037ee5f6f60edbe538d50ba63956222ee1b5c814e11df8bb9c9d03cd853285b973be18968f20adee9d7c6c12413aa9a5aabb28c102701cd61da8184fefd2c597c3a55e2776db1fb59a45aec3441c55ca05cc0a42c32313988b2bfd8897487cfc6a8dfd09267bba1bc814a897f3a507dfaaa9c0b476af98bbab6cd6bec957d3ef46f6e8cb92915bc06d469a39c31fae4de0b83ba2793c7cfec08f4ef0858f3a39527f4efdec09e174e21d35b2ff88b0a9ed8d42ef784236b30a68ef5051c791246f931911a0e58df275144a057b1848f364e5724eae6a73ce56c26d4bd73a6c83b7aa6b1a8fd087e8e1c5d6787f28611470b6be0d036e8bcf01455de531655e85cd5a8ac285b0b5df8f1b112c20dd5e54bbe527d33ba1d28e268c34a3850d50c4cb1be27b482034d34e28b23fff34648b141b7f0c93e1c9a5ef621defe67159c9a37887138393d9c426ebcb24caeecc03b5a533f4ba37f0bcee72334f4b34a7b3ee0476c14c150f869249361d564c1689c4ece406ff0964bdaea3044fc6cc4b47b1d220ec29f1e7dca5176afc00f7bbab289b83302d3cceb8447e529c85e86549d96d08ec85e86d002bdc222540e68df144f43b028c9c2b80708394aced420175a488fb6b0e35a1ba7718db5fcb47b94d10ca2532f3729f40344a1ad3a7b0fc03bf56253409397b213e8bc05007b7a7a7a7a7a7a7a7a7a7a7ab8e53fa15856724ce659ad0000000049454e44ae426082, 35);INSERT INTO `ExpiredDB` (`Pat_ID`, `Name`, `Age`, `Address`, `Symptoms`, `Medicines`, `Prescription`, `Timestamp`) VALUES(0, NULL, NULL, NULL, NULL, NULL, NULL, '2022-11-22'),(1209, NULL, NULL, NULL, NULL, NULL, NULL, '2022-11-22'),(3710, 'Anirudh ', 5000, NULL, ' - hand not able', NULL, '- get new hand', '2022-11-22');INSERT INTO `LoginCreds` (`user_name`, `user_pwd`, `access`, `user_id`) VALUES('ala', 'ala', 0, 1),('admin', 'admin', 1, 2),('adarsh', 'adarsh', 1, 3);INSERT INTO `MedicineDB` (`ID`, `Medicine Name`, `Prescription`, `Type of Sell`, `Manufacturer`, `Salt`, `MRP`, `Uses`, `Alternate Medicines`, `Side Effects`, `How to Use`, `Chemical Class`, `Habit Forming`, `Therapeutic Class`, `Action Class`, `How It Works`) VALUES(1, 'Augmentin 625 Duo Tablet', 'Prescription Required', '10 tablets in 1 strip', 'Glaxo SmithKline Pharmaceuticals Ltd', 'Amoxycillin  (500mg) +  Clavulanic Acid (125mg),', '201.71', 'Treatment of Bacterial infections,', 'Moxikind-CV 625 Tablet,Moxiforce-CV 625 Tablet,Mega-CV 625 Tablet,Fightox 625 Tablet,Duet 625 Tablet,', 'Vomiting,Nausea,Diarrhea,', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Augmentin 625 Duo Tablet is to be taken with food.', 'Not Listed', 'No', 'ANTI INFECTIVES', 'Not Listed', 'Augmentin 625 Duo Tablet is a combination of two medicines: Amoxycillin  and  Clavulanic Acid. Amoxycillin  is an antibiotic. It works by preventing the formation of the bacterial protective covering which is essential for the survival of bacteria.  Clavulanic Acid is a beta-lactamase inhibitor which reduces resistance and enhances the activity of Amoxycillin  against bacteria.'),(2, 'Azithral 500 Tablet', 'Prescription Required', '5 tablets in 1 strip', 'Alembic Pharmaceuticals Ltd', 'Azithromycin (500mg),', '119.5', 'Treatment of Bacterial infections,', 'Ibithral 500mg Tablet,Azibest 500mg Tablet,Zeethrom 500 Tablet,Trulimax 500mg Tablet,Zady 500 Tablet,', 'Vomiting,Nausea,Abdominal pain,Diarrhea,', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Azithral 500 Tablet may be taken with or without food, but it is better to take it at a fixed time.', 'Macrolides', 'No', 'ANTI INFECTIVES', 'Macrolides', 'Azithral 500 Tablet is an antibiotic. It works by preventing synthesis of essential proteins required by bacteria to carry out vital functions. Thus, it stops the bacteria from growing, and prevents the infection from spreading.'),(3, 'Ascoril LS Syrup', 'Prescription Required', '100 ml in 1 bottle', 'Glenmark Pharmaceuticals Ltd', 'Ambroxol (30mg/5ml) + Levosalbutamol (1mg/5ml) + Guaifenesin (50mg/5ml),', '108', 'Treatment of Cough with mucus,', 'Solvin LS Syrup,Ambrodil-LX Syrup,Zerotuss XP Syrup,Capex LS Syrup,Asthalin AX Syrup,', 'Nausea,Vomiting,Diarrhea,Upset stomach,Stomach pain,Allergic reaction,Dizziness,Headache,Rash,Hives,Tremors,Palpitations,Muscle cramp,Increased heart rate,', 'Take this medicine in the dose and duration as advised by your doctor. Check the label for directions before use. Measure it with a measuring cup and take it by mouth. Shake well before use. Ascoril LS Syrup may be taken with or without food, but it is better to take it at a fixed time.', 'Not Listed', 'No', 'RESPIRATORY', 'Not Listed', 'Ascoril LS Syrup is a combination of three medicines: Ambroxol, Levosalbutamol and Guaifenesin, which relieves cough with mucus. Ambroxol is a mucolytic which thins and loosens mucus (phlegm), making it easier to cough out. Levosalbutamol is a bronchodilator. It works by relaxing the muscles in the airways and widens airways. Guaifenesin is an expectorant which decreases the stickiness of mucus (phlegm) and helps in its removal from the airways. Together, they make breathing easier.'),(4, 'Allegra 120mg Tablet', 'Prescription Required', '10 tablets in 1 strip', 'Sanofi India  Ltd', 'Fexofenadine (120mg),', '198.93', 'Treatment of Sneezing and runny nose due to allergies,Treatment of Allergic conditions,', 'Lcfex Tablet,Intrafen 120mg Tablet,Nexofex 120mg Tablet,Histafree 120 Tablet,Fexise 120mg Tablet,', 'Headache,Drowsiness,Dizziness,Nausea,', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Allegra 120mg Tablet may be taken with or without food, but it is better to take it at a fixed time.', 'Diphenylmethane Derivative', 'No', 'RESPIRATORY', 'H1 Antihistaminics (second Generation)', 'Allegra 120mg Tablet belongs to a class of medicines called antihistamines. It blocks the release of a chemical called histamine, which is responsible for causing inflammation and its associated symptoms such as itching, redness, swelling, and irritation.'),(5, 'Avil 25 Tablet', 'Prescription Required', '15 tablets in 1 strip', 'Sanofi India  Ltd', 'Pheniramine (25mg),', '9.97', 'Treatment of Allergic conditions,', 'Eralet 25mg Tablet,Apvil 25mg Tablet,', 'Sleepiness,Dryness in mouth,', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Avil 25 Tablet is to be taken with food.', 'Pyridines Derivatives', 'No', 'RESPIRATORY', 'H1 Antihistaminics (First Generation)', 'Avil 25 Tablet is an antiallergic medication. It works by blocking the action of a chemical messenger (histamine). This relieves symptoms of severe allergic reactions due to insect bite/sting, certain medicines, hives (rashes, swelling, etc).'),(6, 'Aciloc 150 Tablet', 'Prescription Required', '30 tablets in 1 strip', 'Cadila Pharmaceuticals Ltd', 'Ranitidine (150mg),', '36.96', 'Treatment of Gastroesophageal reflux disease (Acid reflux),Treatment of Peptic ulcer disease,', 'Ranitas 150mg Tablet,Zynol 150mg Tablet,Ranitin 150 Tablet,Ranizem 150mg Tablet,Histac 150 Tablet,', 'Sleepiness,Headache,Tiredness,Constipation,Diarrhea,', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Aciloc 150 Tablet may be taken with or without food, but it is better to take it at a fixed time.', 'Aralkylamines Derivative', 'No', 'GASTRO INTESTINAL', 'H2 Receptor Blocker', ''),(7, 'Atarax 25mg Tablet', 'Prescription Required', '15 tablets in 1 strip', 'Dr Reddy\'s Laboratories Ltd', 'Hydroxyzine (25mg),', '77.75', 'Treatment of Anxiety,Treatment of Skin conditions with inflammation & itching,', 'Hydin 25mg Tablet,Hizet 25mg Tablet,Hyzox 25 Tablet,Hydil 25mg Tablet,Zyzine 25mg Tablet,', 'Sedation,Nausea,Vomiting,Upset stomach,Constipation,', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Atarax 25mg Tablet may be taken with or without food, but it is better to take it at a fixed time.', 'Piperazine Derivative', 'No', 'RESPIRATORY', 'H1 Antihistaminics (First Generation)', 'Atarax 25mg Tablet is an antihistaminic medication. In allergy, it works by blocking the action of a chemical messenger (histamine). This relieves allergy symptoms such as itching, swelling, and rashes. In short-term anxiety, it works by decreasing the activity in brain, thereby helping you feel relaxed/sleepy.'),(8, 'Amoxyclav 625 Tablet', 'Prescription Required', 'strip of 6 tablets', 'Abbott', 'Amoxycillin  (500mg) +  Clavulanic Acid (125mg),', '113.25', 'Treatment of Bacterial infections,', 'Moxikind-CV 625 Tablet,Moxiforce-CV 625 Tablet,Mega-CV 625 Tablet,Fightox 625 Tablet,Duet 625 Tablet,', 'Vomiting,Nausea,Diarrhea,', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Amoxyclav 625 Tablet is to be taken with food.', 'Not Listed', 'No', 'ANTI INFECTIVES', 'Not Listed', 'Amoxyclav 625 Tablet is a combination of two medicines: Amoxycillin  and  Clavulanic Acid. Amoxycillin  is an antibiotic. It works by preventing the formation of the bacterial protective covering which is essential for the survival of bacteria.  Clavulanic Acid is a beta-lactamase inhibitor which reduces resistance and enhances the activity of Amoxycillin  against bacteria.'),(9, 'Anovate Cream', 'Prescription Required', '20 gm in 1 tube', 'USV Ltd', 'Phenylephrine (0.10% w/w) + Beclometasone (0.025% w/w) + Lidocaine (2.50% w/w),', '122', 'Treatment of Piles,', 'Pilo GO Cream,PileClear Cream,Proctosedyl BD Cream,', 'Application site reactions (burning, irritation, itching and redness),', 'This medicine is for external use only. Use it in the dose and duration as advised by your doctor. Check the label for directions before use. Clean and dry the affected area and apply the cream. Wash your hands after applying, unless hands are the affected area. ', 'Not Listed', 'No', 'DERMA', 'Not Listed', 'Anovate Cream is a combination of three medicines: Phenylephrine, Beclometasone and Lidocaine, which treats piles. Phenylephrine is a decongestant which shrinks the blood vessels in the affected area of skin and decreases swelling. Beclometasone is a steroid which blocks the production of certain chemical messengers (prostaglandins) that make the skin red, swollen and itchy. Lidocaine is a local anesthetic which works by blocking pain signals from the nerves to the brain thereby decreasing pain sensation.'),(10, 'Avomine Tablet', 'Prescription Required', 'strip of 10 tablets', 'Abbott', 'Promethazine (25mg),', '50.89', 'Treatment of Nausea,Treatment of Vomiting,Treatment of Allergic conditions,Treatment of Motion sickness,', 'Propazine Tablet,Progene 25mg Tablet,Proz 25mg Tablet,Prometh 25mg Tablet,Emin 25mg Tablet,', 'Dryness in mouth,Blurred vision,Headache,Dizziness,', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Avomine Tablet may be taken with or without food, but it is better to take it at a fixed time.', 'Phenothiazine Derivative', 'No', 'GASTRO INTESTINAL', 'H1 Antihistaminics (First Generation)', 'Avomine Tablet is an antiallergic medication. When your body is exposed to an allergen (pollen, animal dander, house dust etc.), it produces a chemical called histamine. This causes watery eyes, runny or blocked nose, sneezing, skin rashes, itching etc. Avomine Tablet works by blocking the action of histamine, thereby relieving these symptoms. It also works directly on several areas of the brain to prevent nausea/vomiting and help you feel more relaxed.'),(11, 'Allegra-M Tablet', 'Prescription Required', '10 tablets in 1 strip', 'Sanofi India  Ltd', 'Montelukast (10mg) + Fexofenadine (120mg),', '228.46', 'Treatment of Sneezing and runny nose due to allergies,', 'Emlukast-FX Tablet,Fixar 10mg/120mg Tablet,Histakind-M Tablet,Histafree-M Tablet,Spiromont-F Tablet,', 'Nausea,Diarrhea,Vomiting,Skin rash,Flu-like symptoms,Headache,Drowsiness,Dizziness,', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Allegra-M Tablet may be taken with or without food, but it is better to take it at a fixed time.', 'Not Listed', 'No', 'RESPIRATORY', 'Not Listed', 'Montelukast is a leukotriene antagonist. It works by blocking the action of a chemical messenger called leukotriene. This reduces inflammation (swelling) in the airways and nose and improves symptoms. Fexofenadine is an antiallergic which blocks the action of another chemical messenger (histamine) responsible for runny nose, watery eyes and sneezing.'),(12, 'Alprax 0.25 Tablet', 'Prescription Required', 'strip of 15 tablets', 'Torrent Pharmaceuticals Ltd', 'Alprazolam (0.25mg),', '29', 'Treatment of Anxiety,Treatment of Panic disorder,', 'Alltop 0.25mg Tablet,Alprasafe 0.25mg Tablet,Nindra 0.25mg Tablet,Alora 0.25mg Tablet,Alp 0.25mg Tablet,', 'Lightheadedness,Drowsiness,', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Alprax 0.25 Tablet may be taken with or without food, but it is better to take it at a fixed time.', 'Benzodiazepines Derivative', 'Yes', 'NEURO CNS', 'Benzodiazepines', 'Alprax 0.25 Tablet is a benzodiazepine. It works by increasing the action of a chemical messenger (GABA) which suppresses the abnormal and excessive activity of the nerve cells in the brain.'),(13, 'Arkamin Tablet', 'Prescription Required', '30 tablets in 1 strip', 'Torrent Pharmaceuticals Ltd', 'Clonidine (100mcg),', '66.05', 'Treatment of Hypertension (high blood pressure),', 'Albamine 100mcg Tablet,Arkapres 100 Tablet,Cloud 100mcg Tablet,Closidin 100mcg Tablet,Cata-Dict 0.1 Tablet,', 'Dizziness,Dryness in mouth,Constipation,Headache,Nausea,Fatigue,Insomnia (difficulty in sleeping),', 'Take this medicine in the dose and duration as advised by your doctor. Swallow it as a whole. Do not chew, crush or break it. Arkamin Tablet may be taken with or without food, but it is better to take it at a fixed time.', 'Imidazoline derivative', 'No', 'CARDIAC', 'Alpha 2-adrenoceptors agonist (Central sympatholytics)', 'Arkamin Tablet is an alpha-2 agonist. It works by relaxing blood vessels which makes the heart more efficient at pumping blood around the body.'),(14, 'Alkasol Oral Solution', 'N', 'bottle of 100 ml Oral Solution', 'Stadmed Pvt Ltd', 'Disodium Hydrogen Citrate (1.4gm/5ml),', '115.14', 'Treatment of Gout,Treatment of Kidney stone,', '', 'Stomach pain,Tiredness,Diarrhea,Nausea,Vomiting,Frequent urge to urinate,', 'Take this medicine in the dose and duration as advised by your doctor. Check the label for directions before use. Measure it with a measuring cup and take it by mouth. Shake well before use. Alkasol Oral Solution may be taken with or without food, but it is better to take it at a fixed time.', 'Carboxylic acid derivative', 'No', 'UROLOGY', 'Uricosuric agent-gout', 'Alkasol Oral Solution is a urine alkalizer. It works by increasing the pH of urine which makes it less acidic. This helps the kidneys get rid of excess uric acid, thereby preventing gout and certain types of kidney stones.'),(15, 'Augmentin Duo Oral Suspension', 'Prescription Required', '30 ml in 1 bottle', 'Glaxo SmithKline Pharmaceuticals Ltd', 'Amoxycillin  (200mg) +  Clavulanic Acid (28.5mg),', '60.82', 'Treatment of Resistance Tuberculosis (TB),Treatment of Bacterial infections,', 'Goldclav Oral Suspension,Moxikind-CV Dry Syrup,Tervis DS Oral Suspension,Bestomax Dry Syrup,Amoxyril-CV Dry Syrup,', 'Nausea,Vomiting,Abdominal pain,Diarrhea,Allergy,Skin rash,', 'Take this medicine in the dose and duration as advised by your doctor. Check the label for directions before use. Measure it with a measuring cup and take it by mouth. Shake well before use. Augmentin Duo Oral Suspension is to be taken with food.', 'Not Listed', 'No', 'ANTI INFECTIVES', 'Not Listed', 'Augmentin Duo Oral Suspension is an antibiotic. It has two active agents, amoxycillin and clavulanic acid. Amoxycillin works by preventing the formation of the bacterial protective covering (cell wall) essential for the survival of the bacteria. Whereas, clavulanic acid serves a special purpose of inhibiting an enzyme (beta-lactamase) that is produced by resistant bacteria. This makes the combination of amoxycillin and clavulanic acid an effective line of treatment for many types of infections.');INSERT INTO `PatientBill` (`Pat_ID`, `Bill_ID`, `Medicine_1`, `Medicine_2`, `Medicine_3`, `Cost_1`, `Cost_2`, `Cost_3`, `Doctor_Fees`, `Total`) VALUES(NULL, 1, 'Aciloc 150 Tablet', 'Atarax 25mg Tablet', 'Allegra-M Tablet', 37, 78, 228, 50, 393),(NULL, 2, 'Avil 25 Tablet', 'Atarax 25mg Tablet', 'Nikoran 5 Tablet', 10, 78, 365, 50, 503),(NULL, 3, 'Aciloc 150 Tablet', 'Atarax 25mg Tablet', 'Allegra-M Tablet', 37, 78, 228, 100, 443),(NULL, 4, 'Aciloc 150 Tablet', 'Atarax 25mg Tablet', 'Allegra-M Tablet', 37, 78, 228, 100000, 100343),(1166, 5, 'Augmentin 625 Duo Tablet', 'Augmentin 625 Duo Tablet', 'Augmentin 625 Duo Tablet', 202, 202, 202, 50, 655),(1166, 6, 'Augmentin 625 Duo Tablet', 'Augmentin 625 Duo Tablet', 'Augmentin 625 Duo Tablet', 202, 202, 202, 50, 655),(3238, 7, 'Augmentin 625 Duo Tablet', 'Augmentin 625 Duo Tablet', 'Augmentin 625 Duo Tablet', 202, 202, 202, 50, 655),(3710, 8, 'Augmentin 625 Duo Tablet', 'Levocet Tablet', 'Allegra-M Tablet', 202, 47, 228, 5000, 5477);INSERT INTO `PatientData` (`Pat_ID`, `Pat_Name`, `Pat_Age`, `Adult`, `Symptoms`, `Prescription`, `Medicine_1`, `Medicine_2`, `Medicine_3`, `Timestamp`) VALUES(2580, 'Shenoy', 20, '1', '', NULL, NULL, NULL, NULL, '00:00:00'),(3238, 'Navin Shrinivas', 120, '1', '', NULL, 'Augmentin 625 Duo Tablet', 'Augmentin 625 Duo Tablet', 'Augmentin 625 Duo Tablet', '00:00:00'),(4160, 'adarsh Liju abraham', 19, '1', '', NULL, NULL, NULL, NULL, '00:00:00'),(5148, 'adarsh', 56, NULL, 'sdgsdfg', 'sfdgsfdg', NULL, NULL, NULL, '21:49:48'),(5623, 'yggk', 134, '1', '', NULL, NULL, NULL, NULL, '00:00:00'),(6733, 'adarsh', 56, 'A', 'sdgsdfg', 'sfdgsfdg', NULL, NULL, NULL, '21:52:01'),(7014, 'adarsh', 190, '1', '', NULL, NULL, NULL, NULL, '00:00:00'),(9182, 'adarsh Liju abraham', 19, '1', '', NULL, NULL, NULL, NULL, '00:00:00'),(9425, 'adarsh Liju abraham', 19, '1', '', NULL, NULL, NULL, NULL, '00:00:00');
```

## **Join Queries**

```sql
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
```

# Aggregate Functions

1. Count all the patients that paid their bills - `COUNT`

```sql
SELECT COUNT(Pat_ID) FROM `PatientBill`;
```

1. Maximum Doctor fees - `MAX`

```sql
SELECT MAX(Doctor_Fees) FROM `PatientBill`;
```

1. Average of Total Bill - `AVG`

```sql
SELECT AVG(Total) FROM `PatientBill`;
```

1. Concatenate 3 Medicines to a single String - `GROUP_CONCAT`

```sql
SELECT GROUP_CONCAT(Medicine_1,Medicine_2,Medicine_3) FROM `PatientData` WHERE 1;
```

# Set Operations

Showcase at least 4 Set Operations queries

```sql
-- UNION
SELECT Pat_Name FROM PatientPres UNION SELECT Pat_ID FROM PatientData;

-- UNION ALL
SELECT Pat_Name FROM PatientPres UNION ALL SELECT Pat_ID FROM PatientData;

-- INTERSECT
SELECT Pat_Name FROM PatientPres INTERSECT SELECT Pat_Name FROM PatientData;

-- EXCEPT
SELECT Pat_Name FROM PatientPres EXCEPT SELECT Pat_Name FROM PatientData;
```

# Functions and Procedures

1. Function to check if the person is senior citizen or not

```sql
DELIMITER $$
CREATE DEFINER=`ala`@`localhost` FUNCTION `isSenior`(`age` INT) RETURNS char(50) CHARSET utf8mb4
    DETERMINISTIC
RETURN IF(age>60,"Senior Citizen","Not Senior Citizen")$$
DELIMITER ;
```

1. Procedure to return payments greater than 2000 rupees

```sql
DELIMITER $$
CREATE DEFINER=`ala`@`localhost` PROCEDURE `huge_payments`()
BEGIN
SELECT * FROM PatientBill WHERE PatientBill.Total>2000;
END$$
DELIMITER ;
```

1. Display All senior citizens by integrating the function

```sql
DELIMITER $$
CREATE DEFINER=`ala`@`localhost` PROCEDURE `senior_citizens`()
BEGIN
	SELECT *,isSenior(PatientData.Pat_Age) FROM PatientData;
END$$
DELIMITER ;
```

# Triggers and Cursors

1. Create a backup of Data when a patient has expired

```sql
CREATE TRIGGER `death` BEFORE DELETE ON `PatientData`
 FOR EACH ROW BEGIN
INSERT into ExpiredDB(Pat_ID,Name,Age,Symptoms,Prescription) VALUES (old.Pat_ID,old.Pat_Name,old.Pat_Age,old.Symptoms,old.Prescription);
END
```

1. Classify Adult/Child based on Patient Age

```sql
CREATE TRIGGER `age_verify` BEFORE INSERT ON `PatientData`
 FOR EACH ROW IF new.`Pat_Age` < 18 then set new.`Adult` = 'C';
ELSEIF new.`Pat_Age` > 18 then set new.`Adult` = 'A';
END IF
```

# Frontend

The Frontend was made using `streamlit` and `pymysql` using `python` as the programming language

### Home Page - Create Operation

![Untitled](DBMS%20Project%20Report%20-%20Doctor%20Prescription%20System%2093125754905e43fd9a1b8859cef1089e/Untitled%202.png)

### Read Operation

![Untitled](DBMS%20Project%20Report%20-%20Doctor%20Prescription%20System%2093125754905e43fd9a1b8859cef1089e/Untitled%203.png)

### Update Operation

![Untitled](DBMS%20Project%20Report%20-%20Doctor%20Prescription%20System%2093125754905e43fd9a1b8859cef1089e/Untitled%204.png)

### SQL Query Page

![Untitled](DBMS%20Project%20Report%20-%20Doctor%20Prescription%20System%2093125754905e43fd9a1b8859cef1089e/Untitled%205.png)

### Bill Page

![Untitled](DBMS%20Project%20Report%20-%20Doctor%20Prescription%20System%2093125754905e43fd9a1b8859cef1089e/Untitled%206.png)