"""
1. Take the number of points one team is ahead.
2. Subtract three.
3. Add a half-point if the team that is ahead has the ball, and
   subtract a half-point if the other team has the ball.
   (Numbers less than zero become zero).
4. Square that.
5. If the result is greater than the number of seconds left in the game,
   the lead is safe.
"""
lead = int(input('Enter the lead in points: '))
possession = input('Do the lead team have the ball (Yes or No): ')
seconds = int(input('Enter the number of seconds remaining: '))

calculation = lead - 3

if possession == 'Yes' or 'yes':
    calculation += 0.5
else:
    calculation -= 0.5

result = calculation**2

percent_safe = (result/seconds) * 100

final_percent = round(percent_safe, 2)

if result > seconds:
    print(f'Lead is safe.')
    print(f'{final_percent}% percent safe, {calculation} safety point margin')
else:
    print(f'Lead is NOT safe.')
    print(f'{final_percent}% percent safe, {calculation} safety point margin')