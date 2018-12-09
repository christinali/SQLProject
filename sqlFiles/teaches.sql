INSERT INTO Teaches 
SELECT DISTINCT class_id1, professor_id1, semester1 FROM Teaches1;