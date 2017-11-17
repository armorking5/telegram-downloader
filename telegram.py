from setup import *
import const
class TG:
	
	const.DEFAULT_PATH = 'telegram_cli'

	def __init__(self,path=''):
		if path is not '':
			self.path = path
		else:
			self.path = self.DEFAULT_PATH
