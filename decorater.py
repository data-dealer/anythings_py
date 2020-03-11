class chicken:
	def _gay(foo):
		def voice(self,*args):
			print('o o o ...') 
			foo(self,*args)
			print('head deach')
		return voice

	@_gay
	def gay1(self):
		print('ec ec ec')
	@_gay
	def gay2(self,hi):
		print('vcl')
		print(hi*2)
	
gatrong = chicken()
gatrong.gay1()
gatrong.gay2('test')
