principal = int(input('Enter the principal amount: '))
rate = float(input('Enter the savings rate : '))
years = int(input('Enter the number of years to save: '))

amount = 0

for year in range(years):
    amount = principal * (1 + rate) ** year
    print(year + 1, end=' ')
    print(round(amount,2))





