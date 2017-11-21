from setup import *
import const
class TG:
	
	const.DEFAULT_PATH = 'telegram-cli'
	real_cmd = '-C -R -N --permanent-msg-ids -W --json -e "$cmd"'
	user = 'Ste'

	def __init__(self,path='',user=''):
		if path is not '':
			self.path = path.strip(' \t\n\r')
		else:
			self.path = const.DEFAULT_PATH

		if user is not '':
			self.user = user.strip(' \t\n\r')

	def get_main_user(self):
		text = self.exec('get_self')

		
	def exec(self,cmd):

		exec_cmd = Template(self.path + ' ' + self.real_cmd).safe_substitute(cmd=cmd)
		
		exec_cmd = Template(exec_cmd).safe_substitute(USER=self.user)

		proof = subprocess.run(self.path + ' ' + exec_cmd,shell=True,stdout=subprocess.PIPE).stdout.decode('utf-8')

		
		print(proof)
