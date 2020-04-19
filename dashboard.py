import cx_Oracle
import chart_studio
import plotly
import plotly.graph_objects as go
import chart_studio.plotly as py
import re
import chart_studio.dashboard_objs as dash
chart_studio.tools.set_credentials_file(username='a.frumovych', api_key='GxqJZQysYWqzouu9uiwG')


def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
    return raw_fileId.replace('/', ':')


username = 'MYONLINEEDU'
password = 'RV-81-19-14f'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

#First query
castles1 = []
values1 = []
query1 = """
SELECT CASTLE.CASTLE, SUM(UNITS.GOLD) AS TOTAL_GOLD
FROM CASTLE JOIN UNITS
ON CASTLE.UNIT_NAME = UNITS.UNIT_NAME
GROUP BY CASTLE.CASTLE
ORDER BY TOTAL_GOLD ASC
"""
cursor.execute(query1)

for row in cursor.fetchall():
    castles1.append(row[0])
    values1.append(row[1])
bar = go.Bar(x=castles1, y=values1)
bar = py.plot([bar], auto_open=True, file_name="Plot1")



#Second query
castles2 = []
values2 = []
query2 = '''
SELECT CASTLE.CASTLE, round ((SUM(UNITS.GOLD) + 0.0) / tg.TOTAL * 100, 2) AS PERCENT_
FROM 
(
    SELECT SUM(UNITS.GOLD) AS TOTAL
    FROM UNITS
)tg, CASTLE JOIN UNITS ON CASTLE.UNIT_NAME = UNITS.UNIT_NAME
GROUP BY CASTLE.CASTLE, tg.TOTAL
ORDER BY PERCENT_ ASC
'''

cursor.execute(query2)


for row in cursor.fetchall():
    castles2.append (row[0])
    values2.append(row[1])
pie = go.Pie (labels = castles2, values = values2)
pie = py.plot([pie],auto_open = True, file_name = "Plot2")


#Third query
level = []
attack = []
query3 = '''
SELECT UNIT_LEVELS.UNIT_LEVEL, MAX(UNITS.ATTACK) AS MAX_ATTACK
FROM UNIT_LEVELS JOIN UNITS
ON UNIT_LEVELS.UNIT_NAME = UNITS.UNIT_NAME
GROUP BY UNIT_LEVELS.UNIT_LEVEL
ORDER BY UNIT_LEVELS.UNIT_LEVEL
'''

cursor.execute(query3)

for row in cursor.fetchall():
    level.append (int(row[0]))
    attack.append(row[1])
scatter = go.Scatter (x = level, y = attack)
scatter = py.plot([scatter],auto_open = True, file_name = "Plot3")


my_dboard = dash.Dashboard()
bar_id = fileId_from_url(bar)
pie_id = fileId_from_url(pie)
scatter_id = fileId_from_url(scatter)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': bar_id,
    'title': 'Query 1'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': pie_id,
    'title': 'Query 2'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': scatter_id,
    'title': 'Query 3'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'Lab_2')

cursor.close()
connection.close()
