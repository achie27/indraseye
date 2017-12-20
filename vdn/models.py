from views import orm

class Location(orm.Model):

	__tablename__ = "locations"

	id = orm.Column(orm.Integer, primary_key=True)
	lan = orm.Column(orm.Integer, nullable=False)
	lon = orm.Column(orm.Integer, nullable=False)
	email = orm.Column(orm.String, nullable=False)
	
	def __init__(self, lan, lon, email):
		self.lan = lan
		self.lon = lon
		self.email = email

	def __repr__(self):
		return '<lan: {0}, lon: {1}, email: {2}>'.format(self.lan, self.lon, self.email)
