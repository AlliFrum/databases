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

my_dboard = dash.Dashboard()

bar_id = fileId_from_url(bar)

#pie_id = fileId_from_url(pie)

#scatter_id = fileId_from_url(scatter)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': bar_id,
    'title': 'Query 1'
}

my_dboard.insert(box_1)

py.dashboard_ops.upload(my_dboard, 'My First Dashboard with Python')

cursor.close()
connection.close()
