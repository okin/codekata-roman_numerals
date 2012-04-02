class ArabicRomanConverter:
	number_pattern = (
					(1, 'I'),
					(5, 'V'),
					(10, 'X'),
					(50, 'L'),
					(100, 'C'),
					(500, 'D'),
					(1000, 'M')
					)

	@classmethod
	def convert(cls, arabic,returnstring=None):
		if returnstring is None:
			returnstring = ''

		if(arabic and abs(arabic) == arabic):
			print arabic
			for (number, roman) in reversed(cls.number_pattern):
				if(number == arabic):
					returnstring += roman
					break
				elif(arabic % number == 0):
					returnstring += cls.convert(number - arabic, returnstring)
					break
				elif(arabic % number != 0):
					rest = int(arabic / number)
					returnstring += cls.convert(number - rest * arabic, returnstring)
					break

		return returnstring

