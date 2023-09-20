import ctypes
import logging
import socket
import sys
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from pathlib import Path

import urllib3

from tools import update_credentials, json_read, prevent_auto_lock, PostHandler, get_hostname

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
prevent_auto_lock()

root_path = Path(__file__).parent

local_path = Path.home().joinpath(f'AppData\\Local\\.rpa')
local_env_path = local_path.joinpath('env.json')
local_env_data = json_read(local_env_path)

global_path = Path(local_env_data['global_path'])
global_username = local_env_data['global_username']
global_password = local_env_data['global_password']
update_credentials(global_path, global_username, global_password, clear=True)
global_env_path = global_path.joinpath('env.json')
global_env_data = json_read(global_env_path)

orc_host = global_env_data['orc_host']
smtp_host = global_env_data['smtp_host']
smtp_author = global_env_data['smtp_author']
sprut_username = global_env_data['sprut_username']
sprut_password = global_env_data['sprut_password']
odines_username = global_env_data['odines_username']
odines_password = global_env_data['odines_password']
odines_username_rpa = global_env_data['odines_username_rpa']
odines_password_rpa = global_env_data['odines_password_rpa']
owa_username = global_env_data['owa_username']
owa_password = global_env_data['owa_password']
owa_username_compl = global_env_data['owa_username_compl']
owa_password_compl = global_env_data['owa_password_compl']
sed_username = global_env_data['sed_username']
sed_password = global_env_data['sed_password']
process_list_path = local_path.joinpath('process_list.json')
tg_token = global_env_data['tg_token']

basic_format = '%(asctime)s||%(levelname)s||%(message)s'
date_format = '%Y-%m-%d,%H:%M:%S'
logging.basicConfig(level=logging.INFO, format=basic_format, datefmt=date_format)
logger_name = 'orchestrator'
logger = logging.getLogger(logger_name)
formatter = logging.Formatter(basic_format, datefmt=date_format)
post_handler = PostHandler(f'{orc_host}/log')
post_handler.setFormatter(formatter)
post_handler.setLevel(logging.INFO)

project_name = 'robot-1p'

config_path = global_path.joinpath(f'.agent\\robot-1p\\{socket.gethostbyname(socket.gethostname())}\\config.json')
config_data = json_read(config_path)
download_path = Path.home().joinpath('downloads')
working_path = r'\\172.16.8.87\d\.rpa\.agent\robot-1p\Output'
for_stat_reports_path = r'\\172.16.8.87\d\.rpa\.agent\robot-1p\Output\Для стата'
# for_stat_reports_path.mkdir(exist_ok=True, parents=True)
chat_id = config_data['chat_id']

if ctypes.windll.user32.GetKeyboardLayout(0) != 67699721:
    __err__ = 'Смените раскладку на ENG'
    logger.exception(__err__)
    raise Exception(__err__)
