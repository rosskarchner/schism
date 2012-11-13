class SchismApp(object):
	def __init__(self, configuration):
		self.configuration=configuration

	def __call__(environ, start_response):
		    start_response('200 OK', [('Content-Type', 'text/plain')])
		        yield 'Hello World\n'


