
def string_remapper(text: str, char_map: dict, escape_map: dict, escape_char: str = '\\') -> str:
	"""
	Remaps characters in a string according to two mapping dictionaries.

	Args:
		text: The input string to be remapped.
		char_map: A dictionary mapping characters to their replacements.
		escape_map: A dictionary mapping escaped characters to their replacement.
		escape_char: The escape character. Default to '\\' (backslash).

	Returns:
		The remapped string.
	"""
	translated_text = ""
	escaped = False
	for char in text:
		if (not escaped) and (char == escape_char):
			escaped = True
			continue

		if not escaped:
			translated_text += ( \
				mapped_char if (mapped_char:=char_map.get(char)) else char)
		else:
			translated_text += ( \
				mapped_char if (mapped_char:=escape_map.get(char)) else char)
			escaped = False

	return translated_text
