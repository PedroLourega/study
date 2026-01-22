INSERT INTO tbl_collections (collectionSetName, releaseDate, totalCardsInCollection)
VALUES 
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62);

INSERT INTO tbl_types (typeName)
VALUES 
('Fire'),
('Water'),
('Grass'),
('Electric'),
('Psychic'),
('Fighting');

INSERT INTO tbl_stages (stageName)
VALUES 
('Basic'),
('Stage 1'),
('Stage 2');

INSERT INTO tbl_cards 
(hp, name, info, attack, damage, weak, ressis, retreat, cardNumberInCollection, collection_id, type_id, stage_id)
VALUES
(150, 'Charizard', 'It is said that Charizard''s fire burns hotter if it has experienced harsh battles.', 'Fire Spin', '200', 'Water x2', 'Fighting -20', '3', '11/108', 1, 1, 3),
(60, 'Bulbasaur', 'A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.', 'Vine Whip', '20', 'Fire x2', '', '1', '44/102', 1, 3, 1),
(70, 'Pikachu', 'When several of these Pokémon gather, their electricity could build and cause lightning storms.', 'Thunder Jolt', '30', 'Fighting x2', 'Metal -20', '1', '58/102', 1, 4, 1),
(100, 'Gyarados', 'Rarely seen in the wild. Huge and vicious, it is capable of destroying entire cities in a rage.', 'Dragon Rage', '50', 'Electric x2', '', '2', '6/102', 1, 2, 2),
(80, 'Scyther', 'Leaps out of tall grass and slices prey with its scythes. The movement is so quick, it is almost invisible.', 'Slash', '30', 'Fire x2', 'Fighting -30', '2', '10/64', 2, 3, 1);
