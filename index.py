import detectEnglish
import unicodedata



if __name__=='__main__':
	# s=input('Enter a string:\t')
	s="WORD"
	st=''
	if ' ' in s:
		for n in range(len(s)):
			if s[n]==' ':
				break
			st+=s[n]
		if not detectEnglish.isEnglish(st):
			raise ValueError("String '%s' is not in english!"%(st))
	else:
		if not detectEnglish.isEnglish(s):
			raise ValueError("String '%s' is not in english!"%(s))
