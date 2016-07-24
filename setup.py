from distutils.core import setup

setup(
	name = 'DeadPyDaylight',
	version = '0.1',
	description = 'Script tool to auto ready-up in Dead By Daylight',
	url = 'http://github.com/LoganGirard/DeadPyDaylight',
	author = 'Logan Girard',
	license = 'MIT',
	packages = ['DeadPyDaylight'],
	install_requires = [
		'pyautogui',
	],
	zip_safe = False)