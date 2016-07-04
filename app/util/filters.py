from .. import app

@app.template_filter('make_caps')
def caps(text):
	"""Convert a string to all caps."""
	return text.uppercase()