# https://www.pythontutorial.net/python-basics/

print ("Bienvenu!")
# list: [] ordered, changeable, and allows duplicate members
# tuple: ()
# set: {} does not allow duplicate members
# dictionary: {"a": "b"}

avec_soleil = True
en_semaine = False

if avec_soleil and not en_semaine:
   print("on va à la plage !")
elif avec_soleil and en_semaine:
   print("on va au travail !")
else:
   print("on reste à la maison !")


message = r'C:\python\bin'

help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''
name = 'John'
message = f'Hi {name}'
print(message)

greeting = 'Good ' 'Morning!'

greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)

print(greeting)

str = "Python String"
print(str[0]) # P
print(str[1]) # y

str = "Python String"
print(str[-1])  # g
print(str[-2])  # n


str = "Python String"
str_len = len(str)
print(str_len)


str = "Python String"
print(str[0:2]) # Py


str = "Python String"
new_str = 'J' + str[1:]
print(new_str)

# define main function to print out something
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

# call function main 
main()

# Python keywords:
# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise
#
# import keyword
# print(keyword.kwlist) 


price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = int(price) * int(tax) / 100
print(f'The net price is ${net_price}')


type(100)


