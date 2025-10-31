USE `Gallery` ;

-- -----------------------------------------------------
-- Insert Sample Data
-- -----------------------------------------------------
USE `Gallery`;


INSERT INTO Photographer (PhotographerName, Email)
VALUES 
    ('Alice Johnson', 'alice.johnson@example.com'),
    ('Michael Davis', 'michael.davis@example.com'),
    ('Sara Thompson', 'sara.thompson@example.com'),
    ('David Lee', 'david.lee@example.com');


INSERT INTO Album (AlbumName, CreationDate)
VALUES
    ('Nature Wonders', '2024-01-15'),
    ('Urban Exploration', '2024-02-10'),
    ('Portrait Sessions', '2024-03-05'),
    ('Wildlife Shots', '2024-04-20');

INSERT INTO Photo (Photodate, idPhotographer, idAlbum)
VALUES
    ('2024-01-20', 1, 1),  
    ('2024-01-22', 1, 1),
    ('2024-02-17', 2, 2),  
    ('2024-02-19', 2, 2),
    ('2024-03-10', 3, 3),  
    ('2024-03-12', 3, 3),
    ('2024-04-25', 4, 4),  
    ('2024-04-26', 4, 4);


INSERT INTO AlbumPhotographer_xref (idAlbum, idPhotographer)
VALUES
    (1, 1), 
    (1, 3),  

    (2, 2),  
    (2, 4),  

    (3, 3),  
    (3, 1),  

    (4, 4),  
    (4, 2);  
