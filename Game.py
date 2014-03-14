class Engine(object):
	def __init__(self, themap):
		self.themap = themap
	
	def play(self):
		next = 'central_corridor'
		while True:
			print "\n=========\n"
			room = getattr(self.themap, next)
			next = room()

amap = Map()
engine = Engine(amap)
engine.play()

