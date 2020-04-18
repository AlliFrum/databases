CREATE TABLE CASTLE (
	castle VARCHAR2 (26 BYTE) NOT NULL,
	unit_name VARCHAR2 (26 BYTE) NOT NULL
);

CREATE TABLE UNITS (
	unit_name VARCHAR2 (26 BYTE) NOT NULL,
	attack NUMBER (38,0) NOT NULL,
	defence NUMBER (38,0) NOT NULL,
	speed NUMBER (38,0) NOT NULL,
	gold NUMBER (38,0) NOT NULL
);

CREATE TABLE UNIT_LEVELS (
	unit_level VARCHAR2 (26 BYTE) NOT NULL,
	unit_name VARCHAR2 (26 BYTE) NOT NULL
);


ALTER TABLE CASTLE ADD CONSTRAINT pk_castle PRIMARY KEY (castle);
ALTER TABLE UNITS ADD CONSTRAINT pk_units PRIMARY KEY (unit_name);
ALTER TABLE UNIT_LEVELS ADD CONSTRAINT pk_unit_levels PRIMARY KEY (unit_level);

ALTER TABLE CASTLE
ADD CONSTRAINT fk_castle FOREIGN KEY (unit_name) REFERENCES UNITS (unit_name);
ALTER TABLE UNIT_LEVELS
ADD CONSTRAINT fk_unit_levels FOREIGN KEY (unit_name) REFERENCES UNITS (unit_name);