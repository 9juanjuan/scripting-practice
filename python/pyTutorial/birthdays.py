birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
       print('Enter a name: (blank to quit)')
       name = input()
       if name == '':
           break
       if name in birthdays: 
           print(birthdays[name] + ' is the birthday of ' + name)
       else:
           print('No bday information\n What is their birthday?')
           bday = input()
           birthdays[name] = bday
           print('Bday database update')
           print(birthdays[name])