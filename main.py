import cx_Oracle

username = 'MYONLINEEDU'
password = 'RV-81-19-14f'
database = 'localhost/xe'
connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()


print("Castle - gold")
query1 = """
SELECT CASTLE.CASTLE, SUM(UNITS.GOLD) AS TOTAL_GOLD
FROM CASTLE JOIN UNITS
ON CASTLE.UNIT_NAME = UNITS.UNIT_NAME
GROUP BY CASTLE.CASTLE
ORDER BY TOTAL_GOLD ASC
"""
cursor.execute(query1)

for row in cursor:
    print(row)


print("\nCastle - percent")
query2 = """
SELECT CASTLE.CASTLE, round ((SUM(UNITS.GOLD) + 0.0) / tg.TOTAL * 100, 2) AS PERCENT_
FROM 
(
    SELECT SUM(UNITS.GOLD) AS TOTAL
    FROM UNITS
)tg, CASTLE JOIN UNITS ON CASTLE.UNIT_NAME = UNITS.UNIT_NAME
GROUP BY CASTLE.CASTLE, tg.TOTAL
ORDER BY PERCENT_ ASC
"""
cursor.execute(query2)

for row in cursor:
    print(row)


print("\nLevel - max attack")
query3 = """
SELECT UNIT_LEVELS.UNIT_LEVEL, MAX(UNITS.ATTACK) AS MAX_ATTACK
FROM UNIT_LEVELS JOIN UNITS
ON UNIT_LEVELS.UNIT_NAME = UNITS.UNIT_NAME
GROUP BY UNIT_LEVELS.UNIT_LEVEL
ORDER BY UNIT_LEVELS.UNIT_LEVEL
"""
cursor.execute(query3)

for row in cursor:
    print(row)

cursor.close()
connection.close()
