# print(type('hello world'))
# print(type("hello world"))
# print(type('''hello world'''))
# print(type("""hello world"""))

'''working with int, flot and string'''
# print(type(9+10.9)) 
# print(type(7+5))
# print(24.7)

# print('hello' , 'world') #hello world
# print('hello' '  world')
# print('hello'+8) #the answer will be type error coz we cant concatenate str to int
# print('hello'+9.7) #the answer will be type error coz we cant concatenate str to float

# print('hello'*10) #we can multiply str with int.
# print('hello'*2.5) #but we cant multilply str with float 

# print("hello "*3) #when we need space in output for hello
# print("hello\n"*3) #when the output need horizontally 

# print("hello python\n"*4) #at last line we will get blank line
# print("hello python\n"*4 , end="") #at last line we will not get any blank line
# print("hello python\n"*4 , end='') #at last line we will not get any blank line

""" this concept is name is seperate (sep='') if we want more than 2 spaces """
# # print(1,2,3,4,5)
# print(1,2,3,4,5,sep='') #without no space
# print(1,2,3,4,5,sep=' ') #with one space only
# print(1,2,3,4,5,sep='  ') #with two space only
# print(1,2,3,4,5,sep='-') #with hyfen


"string cancatention"

# print('hell'+'world')
# print('hello '+'world') #at next line dont touch the first str
# print('hello'+' world') #at next lint dont touch the 1st & 2ns str
# print('hello','world')

print('hello'+''+'world') #without space
print('hello'+' '+'world') #one  space
print('hello'+'  '+'world') #two space
print('hello'+'-'+'world')  #with hifen