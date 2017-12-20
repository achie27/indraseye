# from math import sqrt, pow
# from views import orm
# from models import Location
from db import connect


def locate(lan, lon):
	print("locating closest location")
	conn = connect()
	cur = conn.cursor()
	cur.execute('select lan, lon, email from locations order by sqrt(pow(%f - lan, 2) - pow(%f - lon, 2))'%(lan, lon));
	# data = orm.session.query(Location).order_by('sqrt(pow(Location.lan - lan,2) + pow(Location.lon - lon,2))')
	result = [dict(lan=row[0],lon=row[1],emil=row[2]) for row in cur]
	# print(data.value('lan'))
	return result.email 
