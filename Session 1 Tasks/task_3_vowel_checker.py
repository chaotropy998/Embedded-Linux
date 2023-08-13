letter = input("Please enter a letter to check:")
vowels = ['a','e','i','o','u','A','E','I','O','U']

if letter in vowels:
    print('Letter "{}" is a vowel'.format(letter))
else:
    print('Letter "{}" is not a vowel'.format(letter))
