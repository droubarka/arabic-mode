from setuptools import setup, find_packages

setup(
	name='arabicmode',
	version='1.0.0',
	packages=find_packages(),
	package_data={'arabicmode': ['dicts/*']},
	author='Mohamed A. Oubarka',
	author_email='droubarka@gmail.com',
	url='https://github.com/droubarka/arabic-mode.git',
	description='Arabic Typing Solution: Overcome keyboard limitations and type in Arabic with ease. This package provides English-to-Arabic transliteration and customizable character mapping for seamless Arabic text input.',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
	],
	keywords=(
		'text processing'
		'character mapping ascii unicode'
		'transliteration support'
		'keyboard typing arabic language'
	),
	license='MIT License',
	install_requires=[],
	entry_points={
		'console_scripts': [
			'arabic-mode=arabicmode.__main__:main',
		]
	},
	zip_safe=False
)
