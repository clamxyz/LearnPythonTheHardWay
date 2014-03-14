
DIRECTIONS = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
VERBS = ['go', 'stop', 'kill', 'eat']
STOPS = ['the', 'in', 'of', 'from', 'at', 'it']
NOUNS = ['door', 'bear', 'princess', 'cabinet']

def conver_number(s):
	try:
		return int(s)
	except ValueError:
		return None

def scan(user_input): 
	result = []
	words = user_input.split()
	for word in words:
		if word in DIRECTIONS:
			result.append(('direction', word))
		elif word in VERBS:
			result.append(('verb', word))
		elif word in STOPS:
			result.append(('stop', word))
		elif word in NOUNS:
			result.append(('noun', word))
	#	elif num != None: 
		elif word.isdigit(): 
			num = conver_number(word)
			result.append(('number', num))
		else:
			result.append(('error', word))

	return result


