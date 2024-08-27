class Blob():
	def __init__(self, width = 800, height=600):

		self.w = 100
		self.h = 100

		self.x = width/2 - self.w/2; 
		self.y = height - self.h 

		self.vx = -10
		self.vy = -10

		self.color = (200,0,0)


	def get_coords(self):
		return (self.x, self.y)

	def get_dims(self):
		return (self.w, self.h)

	def update(self):
		self.x += self.vx

		self.x = max(0, min(self.x, self.x + self.w))
		self.y = max(0, min(self.y, self.y + self.h))  
