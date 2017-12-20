# from flask_wtf import Form
from wtforms import Form, StringField, FileField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, URL


class URLForm(Form):
	# task_id = IntegerField()
	q = StringField('q', validators=[URL(False, message="URL IS NOT VALID!")])

class FileForm(Form):
	file = FileField('Upload Video to test if accident is present or not. ', validators=[FileRequired(), FileAllowed(['mp4', 'mkv', 'wmv', 'avi'], 'Videos only!')])