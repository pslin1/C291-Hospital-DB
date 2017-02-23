INSERT INTO staff VALUES("00001", 'A', "Robert Mildrid", "robert", "ecb453d83da2067efeb1243964d2b00aca62a7230c64e39ce69ac555");
INSERT INTO staff VALUES("00002", 'A', "Michael Cote", "michael", "e0acbfeee1e118a26a026dc6496838c8340fc9601ac29e1f45d05c80");
INSERT INTO staff VALUES("00003", 'A', "Lamar Odom", "lamar", "77a8837457013cf080b5e5a6e7c82bdeadd6105e677fec277424b3fb");
INSERT INTO staff VALUES("00004", 'D', "Matt Leblanc", "matt", "f99260285cd6f9d6949f2c66f2d724dc90d15c469bf23e50ba88248c");
INSERT INTO staff VALUES("00005", 'D', "Jennifer Aniston", "jennifer", "ea45e41c3501079b35865a220c52d0501f49e4f3c10a5c2fc4c663e3");
INSERT INTO staff VALUES("00006", 'D', "Matthew Perry", "matthew", "d3d8fb38251ed79ce6a4f283f5711a9b79f722cb3ed100b23a3f75b3");
INSERT INTO staff VALUES("00007", 'N', "Bill Nye", "bill", "3dae10987fcd94f89d1b2de400e867251a8017f203c3b8177b9b5e39");
INSERT INTO staff VALUES("00008", 'N', "George Lucas", "george", "d3bb8886b6a4fc05aad3275c20332d59c200862c0c4f75ccd95d6dbf");
INSERT INTO staff VALUES("00009", 'N', "Snoop Dogg", "snoop", "1acd3aa9baa358312c75adf86875623c60d9e1446fa57a12edbeba23");

INSERT INTO patients VALUES("00001", "Marco Polo", "16-18", "10127 121 ST NW, Edmonton", "780-893-1234", "780-123-4567");
INSERT INTO patients VALUES("00002", "Ferris Bueller", "16-18", "10128 121 ST NW, Edmonton", "780-123-1234", "780-123-4567");
INSERT INTO patients VALUES("00003", "Rupert Rubio", "16-18", "10129 121 ST NW, Edmonton", "780-678-1234", "780-123-4567");
INSERT INTO patients VALUES("00004", "Mario Versace", "16-18", "10130 121 ST NW, Edmonton", "780-232-1234", "780-123-4567");
INSERT INTO patients VALUES("00005", "Enrique Valequez", "20-22", "10131 121 ST NW, Edmonton", "780-231-1234", "780-123-4567");
INSERT INTO patients VALUES("00006", "Jimmy Castro", "20-22", "10132 121 ST NW, Edmonton", "780-098-1234", "780-123-4567");
INSERT INTO patients VALUES("00007", "Phil Bing", "22-24", "10133 121 ST NW, Edmonton", "780-234-1234", "780-123-4567");
INSERT INTO patients VALUES("00008", "Ester Rupka", "22-24", "10134 121 ST NW, Edmonton", "780-213-1234", "780-123-4567");
INSERT INTO patients VALUES("00009", "Johan Masters", "22-24", "10135 121 ST NW, Edmonton", "780-312-1234", "780-123-4567");

INSERT INTO charts VALUES("00001", "00001", "2016-10-01", "2016-10-02");
INSERT INTO charts VALUES("00002", "00002", "2016-10-02", "2016-10-03");
INSERT INTO charts VALUES("00003", "00001", "2016-10-03", "2016-10-04");
INSERT INTO charts VALUES("00004", "00004", "2016-10-10", "2016-10-12");
INSERT INTO charts VALUES("00005", "00003", "2016-10-13", "2016-10-14");
INSERT INTO charts VALUES("00006", "00006", "2016-10-15", "2016-10-15");
INSERT INTO charts VALUES("00007", "00001", "2016-10-17", NULL);
INSERT INTO charts VALUES("00008", "00005", "2016-10-19", NULL);

INSERT INTO symptoms VALUES("00001", "00001", "00007", "2016-10-02", "Cough");
INSERT INTO symptoms VALUES("00003", "00002", "00008", "2016-10-03", "Sore Joints");
INSERT INTO symptoms VALUES("00001", "00003", "00007", "2016-10-04", "Hair Loss");
INSERT INTO symptoms VALUES("00002", "00004", "00009", "2016-10-12", "Bleeding Nose");
INSERT INTO symptoms VALUES("00002", "00005", "00008", "2016-10-14", "Excessive Vommiting");
INSERT INTO symptoms VALUES("00001", "00006", "00009", "2016-10-15", "Loss of vision");
INSERT INTO symptoms VALUES("00001", "00007", "00007", "2016-10-17", "Hallucinating");
INSERT INTO symptoms VALUES("00001", "00008", "00008", "2016-10-19", "Sore Back");

INSERT INTO diagnoses VALUES("00001", "00001", "00004", "2016-10-01", "Flu");
INSERT INTO diagnoses VALUES("00001", "00002", "00004", "2016-10-02", "Cancer");
INSERT INTO diagnoses VALUES("00001", "00003", "00004", "2016-10-03", "Cold Sore");
INSERT INTO diagnoses VALUES("00001", "00004", "00004", "2016-10-10", "Diabetes");
INSERT INTO diagnoses VALUES("00001", "00005", "00004", "2016-10-13", "Cold");
INSERT INTO diagnoses VALUES("00001", "00006", "00004", "2016-10-15", "Flu");

INSERT INTO drugs VALUES('ABC', 'anti-inflammatory');
INSERT INTO drugs VALUES('XXX', 'anti-inflammatory');
INSERT INTO drugs VALUES('DEF', 'anti-inflammatory');
INSERT INTO drugs VALUES('niacin', 'anti-inflammatory');
INSERT INTO drugs VALUES('Adravil', 'fictional');
INSERT INTO drugs VALUES("Tylenol", "Pain Killer");
INSERT INTO drugs VALUES("Vicodin", "Pain Killer");

INSERT INTO dosage VALUES('ABC', '20-22', 100);
INSERT INTO dosage VALUES('ABC', '22-24', 200);
INSERT INTO dosage VALUES('ABC', '16-18', 40);
INSERT INTO dosage VALUES('XXX', '20-22', 123);
INSERT INTO dosage VALUES('XXX', '22-24', 324);
INSERT INTO dosage VALUES('XXX', '16-18', 55);
INSERT INTO dosage VALUES('DEF', '20-22', 34);
INSERT INTO dosage VALUES('DEF', '22-24', 23);
INSERT INTO dosage VALUES('DEF', '16-18', 12);
INSERT INTO dosage VALUES('niacin', '20-22', 3421);
INSERT INTO dosage VALUES('niacin', '22-24', 2313);
INSERT INTO dosage VALUES('niacin', '16-18', 1000);
INSERT INTO dosage VALUES('Adravil', '20-22', 800);
INSERT INTO dosage VALUES('Adravil', '22-24', 1000);
INSERT INTO dosage VALUES('Adravil', '16-18', 1200);
INSERT INTO dosage VALUES('Tylenol', '20-22', 4);
INSERT INTO dosage VALUES('Tylenol', '22-24', 3);
INSERT INTO dosage VALUES('Tylenol', '16-18', 2);
INSERT INTO dosage VALUES('Vicodin', '20-22', 3);
INSERT INTO dosage VALUES('Vicodin', '22-24', 2);
INSERT INTO dosage VALUES('Vicodin', '16-18', 1);

INSERT INTO medications VALUES("00001", "00001", "00007", "2016-10-02", "2016-10-02", "2016-10-09", 2313, 'niacin');
INSERT INTO medications VALUES("00003", "00002", "00008", "2016-10-03", "2016-10-03", "2016-10-10", 1000, 'niacin');
INSERT INTO medications VALUES("00001", "00003", "00007", "2016-10-04", "2016-10-04", "2016-10-11", 1500, 'Adravil');
INSERT INTO medications VALUES("00002", "00004", "00009", "2016-10-12", "2016-10-12", "2016-10-19", 5, 'Tylenol');
INSERT INTO medications VALUES("00002", "00005", "00008", "2016-10-14", "2016-10-14", "2016-10-21", 1, 'Vicodin');
INSERT INTO medications VALUES("00001", "00006", "00009", "2016-10-15", "2016-10-15", "2016-10-22", 25, 'DEF');
INSERT INTO medications VALUES("00001", "00007", "00007", "2016-10-17", "2016-10-17", "2016-10-24", 100, 'XXX');
INSERT INTO medications VALUES("00001", "00008", "00008", "2016-10-19", "2016-10-19", "2016-10-26", 150, 'ABC');

INSERT INTO reportedallergies VALUES
('00001', 'Adravil'),
('00002', 'XXX'),
('00002', 'Adravil'),
('00003', 'XXX'),
('00004', 'Adravil'),
('00001', 'XXX'),
('00006', 'Adravil'),
('00005', 'XXX'),
('00007', 'Vicodin'),
('00009', 'Tylenol'),
('00009', 'Vicodin'),
('00004', 'niacin');


INSERT INTO inferredallergies VALUES
('Adravil', 'XXX'),
('Vicodin', 'Tylenol'),
('ABC', 'niacin'),
('Adravil', 'niacin');






