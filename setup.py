from distutils.core import setup

setup(
	name="lambda_tools",
	version="0.0.1",
	author="Sigurd Naess",
	author_email="sigurdkn@astro.uio.no",
	packages=["lambda_tools"],
	scripts=["bin/reproject_map"],
	description="Python utilities for the LAMBDA CMB archive",
	long_description="""A set of python modules and command-line utilities
made for dealing with reprojection of maps from the LAMBDA CMB archive.""",
	download_url = 'https://github.com/amaurea/lambda_tools/0.0.1',
	license = "CC0",
	keywords = "lambda cmb fits astronomy",
	url = "http://packages.python.org/lambda_tools",
	classifiers=[
		"Topic :: Scientific/Engineering",
		"License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
	],
)
