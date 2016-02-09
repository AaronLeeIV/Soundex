def soundex(s): 
	if not s:
		return s

	replacements = (('bfpv',		'1'),
					('cgjkqsxz',	'2'),
					('dt',			'3'),
					('l',			'4'),
					('mn',			'5'),
					('r',			'6'))
	
	result, count = [s[0]], 1
	lastValue = None

	for key, value in replacements:
		if s[0].lower() in key:
			lastValue = value
			break

	for character in s[1:]:
		for key, value in replacements:
			if character.lower() in key:
				if value != lastValue:
					result.append(value)
					count += 1
					lastValue = value
					break
				else:
					lastValue = None
		if count == 4:
			break

	result += '0'*(4-count)
	return ''.join(result)
