user = input("enter anything: ")
upper = 0
lower = 0
digit = 0
symbols = 0
for i in user:
  if i.isupper():
    upper +=1
  elif i.islower():
    lower += 1
  elif i.isdigit():
    digit += 1
  else:
    symbols +=1
print('total number of upper letters {}'.format(upper))
print('total number of lower letters {}'.format(lower))
print('total number of digits {}'.format(digit))
print('total number of symbols {}'.format(symbols))
