INSERT INTO UNITS(unit_name, attack, defence, speed, gold) VALUES ('Archangel', 30, 30, 18, 5000);
INSERT INTO UNITS(unit_name, attack, defence, speed, gold) VALUES ('GoldDragon', 27, 27, 16, 4000);
INSERT INTO UNITS(unit_name, attack, defence, speed, gold) VALUES ('Titan', 24, 24, 11, 5000);
INSERT INTO UNITS(unit_name, attack, defence, speed, gold) VALUES ('ArchDevil', 26, 28, 17, 4500);
INSERT INTO UNITS(unit_name, attack, defence, speed, gold) VALUES ('BlackDragon', 25, 25, 15, 4000);


INSERT INTO CASTLE (castle, unit_name) VALUES ('Castle', 'Archangel');
INSERT INTO CASTLE (castle, unit_name) VALUES ('Rampart', 'GoldDragon');
INSERT INTO CASTLE (castle, unit_name) VALUES ('Tower', 'Titan');
INSERT INTO CASTLE (castle, unit_name) VALUES ('Inferno', 'ArchDevil');
INSERT INTO CASTLE (castle, unit_name) VALUES ('Dungeon', 'BlackDragon');


INSERT INTO UNIT_LEVELS (unit_level, unit_name) VALUES ('7+', 'Archangel');
INSERT INTO UNIT_LEVELS (unit_level, unit_name) VALUES ('7+', 'GoldDragon');
INSERT INTO UNIT_LEVELS (unit_level, unit_name) VALUES ('7+', 'Titan');
INSERT INTO UNIT_LEVELS (unit_level, unit_name) VALUES ('7+', 'ArchDevil');
INSERT INTO UNIT_LEVELS (unit_level, unit_name) VALUES ('7+', 'BlackDragon');

