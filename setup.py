from distutils.core import setup

setup(
	name = 'DeadPyDaylight',
	version = '0.1',
	description = 'Script tool to auto ready-up in Dead By Daylight',
	url = 'https://github.com/Aidid51/DeadPyDaylight',
	author = 'Aidid51',
	license = 'MIT',
	packages = ['DeadPyDaylight'],
	install_requires = [
		'pyautogui',
	],
	zip_safe =False)