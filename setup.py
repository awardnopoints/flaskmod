from setuptools import setup

setup(
	name='flaskmod',
	version='0.1',
	author='Eoin',
	packages=['package'],
	entry_points={
		'console_scripts':['flaskmod=package.app:app.run']
	}
)
