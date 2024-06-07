#!/usr/bin/python3

dict_1 = {
	'a': 'ا', 'b': 'ب', 't': 'ت', 'j': 'ج',
	'7': 'ح', 'd': 'د', 'r': 'ر', 'z': 'ز',
	's': 'س', 'x': 'ش', '3': 'ع', '4': 'غ',
	'f': 'ف', 'q': 'ق', 'k': 'ك', 'l': 'ل',
	'm': 'م', 'n': 'ن', 'h': 'ه', 'w': 'و',
	'y': 'ي'
}

dict_2 = {
	'a': 'أ', 'k': 'خ', 'd': 'ذ', 's': 'ص',
	't': 'ط', '8': 'ض', '9': 'ظ', '0': 'ث',
}

def translate_to_arabic(text: str):
	translated_text = ""
	escaped = False
	for char in text:
		if (not escaped) and ('\\' == char):
			escaped = True
			continue

		if not escaped:
			translated_text += (mchar if (mchar:=dict_1.get(char)) else char)
		else:
			translated_text += (mchar if (mchar:=dict_2.get(char)) else char)
			escaped = False

	return translated_text
