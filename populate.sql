INSERT INTO UNITS(unit_name, attack, defence, speed, gold) VALUES ('Angel', 20, 20, 12, 3000);
INSERT INTO UNITS(unit_name, attack, defence, speed, gold) VALUES ('Cyclops', 15, 12, 6, 750);
INSERT INTO UNITS(unit_name, attack, defence, speed, gold) VALUES ('Gorgon', 10, 14, 5, 525);
INSERT INTO UNITS(unit_name, attack, defence, speed, gold) VALUES ('Medusa', 9, 9, 5, 300);
INSERT INTO UNITS(unit_name, attack, defence, speed, gold) VALUES ('StoneGolem', 7, 10, 3, 150);


INSERT INTO CASTLE (castle, unit_name) VALUES ('Castle', 'Angel');
INSERT INTO CASTLE (castle, unit_name) VALUES ('Stronghold', 'Cyclops');
INSERT INTO CASTLE (castle, unit_name) VALUES ('Tower', 'StoneGolem');
INSERT INTO CASTLE (castle, unit_name) VALUES ('Fortress', 'Gorgon');
INSERT INTO CASTLE (castle, unit_name) VALUES ('Dungeon', 'Medusa');


INSERT INTO UNIT_LEVELS (unit_level, unit_name) VALUES ('7', 'Angel');
INSERT INTO UNIT_LEVELS (unit_level, unit_name) VALUES ('6', 'Cyclops');
INSERT INTO UNIT_LEVELS (unit_level, unit_name) VALUES ('5', 'Gorgon');
INSERT INTO UNIT_LEVELS (unit_level, unit_name) VALUES ('4', 'Medusa');
INSERT INTO UNIT_LEVELS (unit_level, unit_name) VALUES ('3', 'StoneGolem');

