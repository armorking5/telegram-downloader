#!/usr/bin/env python3.6
from setup import *

# Flag per individuare la presenza di user specificati
const.ME = 0

# PARSER
# Creo il parser degli argomenti con tutte le opzioni del caso
parser = argparse.ArgumentParser(description="Downloads by default 50 files from the history of a chat in Telegram")
parser.add_argument("-u","--user",dest="user", help="Username of the chats from where to begin to download files, by default will be used the logged username", default=const.ME)
parser.add_argument('-b')
parser.add_argument("-p", "--path", dest="exec_path", help="executible path of telegram-cli if is not on PATH",default=const.DEFAULT_PATH)
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False, help="print info messages")

args = parser.parse_args()

telegram = TG(args.exec_path)

cmd = '$path -C -R -N --permanent-msg-ids -W --json -e "history $USER 50"'

if args.user == 0:
	user = telegram.get_main_user()
else:
	user = args.user


Template(cmd).substitute(path=args.path,USER=user)
