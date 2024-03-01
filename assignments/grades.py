number_grade = int(input('Enter your grade in number form: '))

if number_grade >= 93:
    letter_grade = 'A-'

elif number_grade >= 90 and number_grade <= 92:
    letter_grade = 'A-'

elif number_grade >= 87 and number_grade <= 89:
    letter_grade = 'B+'

elif number_grade >= 83 and number_grade <= 86:
    letter_grade = 'B'

elif number_grade >= 80 and number_grade <= 82:
    letter_grade = 'B-'

elif number_grade >= 77 and number_grade <= 79:
    letter_grade = 'C+'

elif number_grade >= 73 and number_grade <= 76:
    letter_grade = 'C'

elif number_grade >= 70 and number_grade <= 72:
    letter_grade = 'C-'

elif number_grade >= 67 and number_grade <= 69:
    letter_grade = 'D+'

elif number_grade >= 63 and number_grade <= 66:
    letter_grade = 'D'

elif number_grade >= 60 and number_grade <= 62:
    letter_grade = 'D-'

else:
    letter_grade = 'F'
print(f'Your letter grade for {number_grade} is {letter_grade}.')


