
from .arabicmode import string_remapper
from sys import argv

import pkg_resources
import json

def main():
	# load character map from json file
	char_map_json = pkg_resources.resource_string('arabicmode', 'dicts/char_map.json')
	char_map = json.loads(char_map_json.decode('utf-8'))

	# load escape map from json file
	escape_map_json = pkg_resources.resource_string('arabicmode', 'dicts/escape_map.json')
	escape_map = json.loads(escape_map_json.decode('utf-8'))

	# iterate over command-line arguments
	for text in argv[1:]:
		# remap the argument using the character and escape maps and print it
		remapped_string = string_remapper(text, char_map, escape_map, escape_char='\\')
		print(remapped_string)
