import const
from setup import *


class TG:

    const.DEFAULT_PATH = 'telegram-cli'
    real_cmd = '-C -R -N -I -D -f --log-level=0 --permanent-msg-ids -W --json -e "$cmd"'
    user = 'Ste'

    def __init__(self, path='', user=''):
        if path != '':
            self.path = path.strip(' \t\n\r')
        else:
            self.path = const.DEFAULT_PATH

        if user != '':
            self.user = user.strip(' \t\n\r')

    def get_main_user(self):
        text = self.exec('get_self')

    def exec(self, cmd):

        exec_cmd = Template(
            self.path + ' ' + self.real_cmd).safe_substitute(cmd=cmd)

        exec_cmd = Template(exec_cmd).safe_substitute(USER=self.user)

        if const.VERBOSE:
            print(exec_cmd)

        content = subprocess.run(self.path + ' ' + exec_cmd, shell=True,
                                 stdout=subprocess.PIPE).stdout.decode('utf-8')

        # TODO: Add content first line examination that analyses if it's a valid json and returns
        #       Output error and exit if any error occurs

        print(content)
