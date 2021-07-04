INSERT INTO mydb.wizard (name, house, pet, year) VALUES ('Harry Potter', 'Gryffindor', 'Hedwig', '5');
INSERT INTO mydb.wizard (name, house, pet, year) VALUES ('Hermione Granger', 'Gryffindor', 'Crookshanks', '5');
SELECT * FROM mydb.wizard WHERE id = 1;
SELECT * FROM mydb.wizard WHERE house = 'Gryffindor';
UPDATE mydb.wizard SET year = '6' WHERE id = 1;
