year=int(input('which year do you want: '))
l=year/4
y=year/100
leap_year=year/400
if l%2==0 and leap_year%2==0:
  print('Leap Year.')
elif y%2==0:
  print('Leap Year.')
else:
  print('Not A Leap Year.')
