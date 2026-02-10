print("kuch bhi yaha likhenge wo same print hoga output me")
# yadi app print ke andar sirf no. likhana chahate hai so "" lagao ya na lagao it is doesn't matter
# aapako next line me proceed karne ke liye 
#\n  use karna padega 
# and yadi aap chahate hai ki next line me space na chhute to please type like this \nand then whatever you like to proceed 

#             escape sequence:-
# \n is an escape sequence used for go to new line 

# is a comment
# comment is used for show a message to fellow developer
# comment is not excecuted by python 

# and comment ko uncomment karne ke liye short cut hai :- ctrl + / but afsos python IDLE me nai chalata
# this short cut is work on vs code

# multi line comment ke liye 
# 1) triple single quote me enclose karna 
''' then whatever you like to proceed or type'''
# 2)triple double quote me enclose karna    
""" then whatever you like to proceed or type"""

print("hey i am a good boy\nand this viewer is also a good boy/girl")
# is me aapko good boy ko " " me lana hai so app direct laga do ge " " and then error ayenga so error se bachane ne ke liye 
# we can use double quote escape sequence just like this \"good boy\"
print("hey i am a \"good boy\"\nand this viewer Is also a good boy/girl")


# hum single quote ke andar single quote ese hi nahi dal sakte hame uske liye \' ka use karna padega
# just like \" jo hum double quote me double quote dalne ke liye karate hai


# separate character chizo ko separate karta hai
# for an example code is 
print("hey",6,7)
# so hum ise $ se separate karne ke liye use karenge separate character
print("hey",6,7, sep="$")

# so out put Is
# hey$6$7

# and ye separater chizo ko join karta hai

print("hey",6,7,end="kuchh bhi")
# so end is basically is print statement ke last me kya print karna hai
# and also aap agale print statement ko isse join kar sakte ho
# yadi app ne kuchh bhi ke baad\n nahi lagaya to agala print statement new line se start nahi hoga


# variable

# numeric data :- 1) int = 0123456789........
#                 2) float = 1.1, 2.3 (for decimal)
#                 3)complex = 1+2i

# text :- str mean string

# True False is :- bool mean boolean data

# list is a list of item of different different datatype
# tupel is almost same as list but difference is , it is not changeable after created or fixed or immutable


# mapped data :- dic


# arthmetic operatiors

# + :- addition
# - :- subtraction
# * :- multiplication
# / :- division 
# % :- modulus
# // :- floor division
# ** :- exponential

# *******type casting**** 
# to change string to int 
# or basically conversion of one data type to other data type
# type casting is a two type 

# 1) explicit conversion :- hum python ko data type conversion ke liye bolte hai wo 
# 2) implicit conversion :- and isme python hamare liye conversion karta hai 
# for an example
a = 1.9
b = 8
print (a+b)

# so basically a is float 
# b is integer 
# and final output is float


# 1) explicit conversion ka example

a = "1"
b = "2"

print(int (a)+ int (b))



# taking user input

a = input("enter your name : ") 
print("hi", a)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x+y)


print(int(x)+int(y))

# string in python

# app python me kuch bhi double quote and also single quote me likh do string ban jayenga

# app ko string ke bich me double quote ("") lagana hai to app poore string ko single quote me enclose kare 
# and also we can use escape sequence (\") .


# app multi line string banana chahate hai to app triple single quote or triple double quote ka use kar sakte hai


# for an example 
name = "naishal"
friend = "rohan"
anotherfriend = 'lovish'
apple = ''' he said, 
hey i am good 
nice
"i want to eat an apple" '''
print ("hello ,"+ name)
print (apple)


# so output is 

# hello ,naishal
#  he said, 
# hey i am good 
# nice
# "i want to eat an apple" 

# ***indexing

# in indexing counting is start from 0 not 1 so be carefull!!!!!

name = "naishal"
print(name[0])


# so output is n


# ***loop in string

# so hum log loop ki help se python ki string me sabhi ek ek character print karwa sakte hai
# for an example
name = "naishal"
for character in name:
    print(character)


# so output is
# n
# a
# i
# s
# h
# a
# l


# and ye to small tha but jyada text ke liye loop ka use kiya jata hai.


# ******string slicing & operations

# length of a string

fruit="Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word")

# so out put is 

# Mango is a 4 letter word


# so basically len se hum log poore string ki length bina gine nikal sakte hai . and wo bhi python se.


# and for slicing
#  hum log use karenge


names = "naishal"
print(names[0:5])

# output is 

# naish 

# ek notice karne wali baat ye hai ki hum python ko 0 se 5 tak ki range denge fir bhi python 0 se 4 tak hi print karata hai so be carefull

# and ek dusari baat ye ki yadi hum [:5]
# ese bhi likhe to bhi koi farak nahi padata python is smart wo naish ye print karenga 
# or we can say in sort as same as [0:5].
# and aur ek baat ki app total count karke likhe ya fir sirf[:] ye likhe dono same hi hai.

# so lets discussing negative slicing so 
# for an example
names = "naishal"
print(names[0:-3])#this both are  
print(names[0:len(names)-3])#same

# so output is 

# nais
# nais


# so isse hume pata chalta hai ki hum
# ese likhe print(names[0:-3])
# ya ese print(names[0:len(names)-3])
# dono same hi hai.

# now both negative
# for an example
names = "naishal"
print(names[-3:-1])

# so output is
# sh


# so basically python me negative slicing me python total length mese se given value ko minus karata hai jese ki

names = "naishal"
print(names[-3:-1])

# total length is 7
# in this 7-3 = 4
# 7-1 = 6
# so yaha hame range mili hai 4:6 tak and as always python last wale ko ignore karta hai and in this wo last wala is 6.
# so output is sh

# main and important thing that 3 parts me confuse nai hona hai
# basically usme esa hota hai ki
# ye [::-1] wala concept simple aur clear Hindi mein samjhaata hoon.
# Yeh teen parts hote hain:
# L[start : stop : step]

# Part	Matlab
# start	Kahan se shuru karna hai (index number)
# stop	Kahan tak jaana hai (lekin stop waala index include nahi hota)
# step	Kitne index ka jump lena hai. + matlab aage, - matlab peeche


cha = ['A', 'B', 'C', 'D', 'E']
# Index:    0    1    2    3    4
# Negative: -5  -4   -3   -2   -1

# 🔸 Example 2: 
cha[::2]
# start, stop empty chhoda hai → poori list

# step = 2 → Har doosra element uthao

# ['A', 'B', 'C', 'D', 'E']
#    ↑         ↑         ↑
#    0         2         4

# Output: ['A', 'C', 'E']

# 🔸 Example 3: 
L[::-1] #(Jo aapne poocha tha)
# start, stop khali

# step = -1 → List ko peeche se aage read karo

# ['A', 'B', 'C', 'D', 'E']
#    ↓   ↓   ↓   ↓   ↓
#    E   D   C   B   A

# Output: ['E', 'D', 'C', 'B', 'A']

# 🧠 Rule yaad rakho:
# step = +1 → List normal order mein chalegi

# step = -1 → List reverse ho jaayegi

# Aapka original code:


ch = ['TIC', 'TAC']
print(L[::-1])


# output is
# ['TAC', 'TIC']



# ****string ko upper case letter me kese convert kare to iska solution hai ki


a = "Naishal"
print(a.upper())

# so output is 

# NAISHAL


# and also hum lower case letter me bhi convert kar sakte 

print(a.lower())

# so out put is 
# naishal

# note:- strings are immutable it means you can't change . isko replicate or nayi string bolenge jo humne abhi banayi


# **yadi hume traling character ko remove karna hai so hum use karenge rstrip

a = "naishal!!!!!!"
print(a.rstrip("!"))

# so output is 
# naishal


# note:- agar ! ye aage hota to python usse print karega
# for an example

a = "!!!!naishal!!!!"
print(a.rstrip("!"))


# so output is 
# !!!!naishal

# and hume kuchh replace karna hai to hum use karenge

a = "!!!naishal!!!"
print(a.replace("naishal","random"))
 


# so output is 
# !!!random!!!

# one more example


a = "!!!naishal!!!naishal!!!"
print(a.replace("naishal","random"))

# so output is 
# !!!random!!!random!!!
 

# ***split 

# so basically ye list bana deti hai .
# and bich me space honi chahiye
# for an example

a = "!!!naishal !!! naishal!!!"
print(a.split(" "))

# so basically output is

# ['!!!naishal', '!!!', 'naishal!!!']


# **capitalize 
# basically isme first letter capital me ho jata hai.


# for an example


heading = "hey there i am your personal voice assistant"
print(heading.capitalize())

# so basically output is 

# Hey there i am your personal voice assistant

# and ye capitalize basically is condition me kaam ata hai 
# for an example:-

heading = "hey thEre I am yOur perSOnal Voice assiStant"
print(heading.capitalize())

# out put is 
# Hey there i am your personal voice assistant

# so capitalize is basically help karta hai hume is tarah se
# proper sentence kar ke diya hume first block and baki sare small me
# jaise ki jaha innecessary koi block letter hai sentence ke bich me to use wo small karke fix kar deta hai

# *center 

# so ye sentence ko bich me aline kar deta hai 
# for an example


str1 = "welcome to the console!!!"
print(str1.center(50))
 
# so output is 
            # welcome to the console!!!    


# **count
# so hum count ki help se kuchh bhi dekh sakte hai ki wo kitani baar hai string me
# for an example

a = "!!!naishal!!!naishal!!!"
print(a.count("naishal"))

# so output is 
# 2

# ***endswith

# Ends with Say in a term of true or false. 
# ends with hume ye true or false me batata hai ki humne usse jo chiz(context or word) boli hai wo hamri given string me end ho rahi hai or end me aati hai
# for an Example
STR1 = " Welcome to the console!!!"
print(STR1.endswith("!!!"))

# so output is 
# true


# and also hum isse range bata ke bhi puchh sakte hai 
# for an example

STR1 = " Welcome to the console!!!"
print(STR1.endswith("to",4,10))

# explanation:- so humne ise 4 se 10 ke bich ki range de di and puchha ki "to " end ho raha hai  4:10 ki range me
# output is
# true


# ***find se hum kuchh find kar sakte hai
# it mean ki hum string me hamari given chiz kaha pe index kar rahi hai wo pata kar sakte hai
# for an example

str1 ="he's name is dan. he is an honest man."
print(str1.find("is"))

# out put
# 10

# so isne hume is sabse pahle kaha aata hai wo bata diya
# and hamri given chiz string me nahi hogi to python -1 print karenga.


# ****index is almost same as find but one difference present.
# index se hum kuchh esa puchte hai ki wo string me na ho to wo error create karata hai instead of print -1 as find do this thing.
str1 = "hello i am you virtual assistant"
print(str1.index("ishh"))
# error ayega


# ***isalnum
# mean A-Z,a-z,0-9 se bani hui string

# ex:-
str1 = "WelcomeToTheConsole"
print(str1.isalnum())


# output
# true


# ****isalpha
# mean presence of A-Z , a-z 

# ex:- 
str1 = "Welcome"
print(str1.isalpha())

# output
# true


# *****islower
# yadi aapke string me sabhi letter small hai to ye true print karega warna false

# for an example
str1 = "we wish you a Merry Christmas"
print(str1.islower())

# output
# false


# **isprintable
# so ye basically ye batata hai ki string me jo kuchh likha hai wo printable hai ki nai 
# for an example:-
str1 = "We wish you a Merry Christmas"
print(str1)
print(str1.isprintable())


# so output is 
# true 


# so you are wondering about ki hmm we are understanding this thing but what the thing about not printable ? what things we are type and output is false? or false kab ayega?
# so the answer is ki 
# hum jab kuchh different character use karenge just like \n
# for an example:-

str1 = "We wish you a Merry Christmas\n"
print(str1)
print(str1.isprintable())


# so now output is 
# false


# ***isspace 
# so ye bahot easy hai string poori khali hai means string me space hai just like given example

# ex:- 
str1 = "       " #using spacebar
print(str1.isspace())
str2 = "  " #using tab
print(str2.isspace())


# so output is 
# true 
# true


# **istitle

# so ye basically hame ye batata hai ki poori string me sabhi word ke first letter capital hai ki nai hai to true warna false
# ex:-

str1 = "World Health Organization"
print(str1.istitle())


# output 
# true

# ex:-
str2 = "To kill a mocking bird"
print(str2.istitle())


# output is 
# false


# ***isupper
# so ye basically hame ye batata hai ki poori string me sabhi word capital hai ki nai hai to true warna false.
# ex:-

str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())

# output is
# true


# ****startswith

# start with Say in a term of true or false. 
# start with hume ye true or false me batata hai ki humne usse jo chiz(context or word) boli hai wo hamri given string me starting me aati hai.
# for an Example
STR1 = "Welcome to the console!!!"
print(str1.startswith("welcome"))

# so output is 
# true


# and also hum isse range bata ke bhi puchh sakte hai 
# for an example

STR1 = " Welcome to the console!!!"
print(str1.startwith("ome",4,10))

# explanation:- so humne ise 4 se 10 ke bich ki range de di and puchha ki ome se start hota hai 4:10 ki range me
#  output is
# true


# ****swapcase
# so ye basically lower case ko upper case and upper case ko lower case me convert kar deta hai
# for an example:-
str1 = "Python is a Interpreted Language"
print(str1.swapcase())

# output is
# pYTHON IS A iNTERPRETED lANGUAGE


# ***title
# use for convert simple sentence to title and in title all words 1 letter is converted to block letter or capital.
str1 = "his name is dan. dan is an honest man"
print(str1.title())

# output is 
# His Name Is Dan. Dan Is An Honest Man.


# *******if else******


# conditional operator
# <,>,<=,>=,==,!=


# if ,else and elif me condition check hoti hai python interpreter uper se check karta hai and jaha condition Match ho gayi waha pe ruk jayega aage nahi check karne jayega wo 
# for an example
num = int(input("Enter the value of num: "))
if (num<0):
    print("Number is negative.")
elif(num==0):
    Print ("Number is zero.")
elif(num == 999):
    Print ("number is special.")
else:
    print ("number is positive.")

print(" I am happy now")

# output

# Enter the value of num: 999
# number is special.
#  I am happy now

# Enter the value of num: -10
# Number is negative.
#  I am happy now

# Enter the value of num: 10
# number is positive.
#  I am happy now


# Enter the value of num: 0
# Number is zero.
#  I am happy now


# *******match case statement


x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
        #case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)


# ******loops*********

# 1) for loop 
# 2) while loop


# 1) for loop
# ex:- 

name = "Abhishek"

for i in name:
    print(i)
    if(i=="b"):
        print("This is something special!")


# so output is 
# A
# b
# This is something special!
# h
# i
# s
# h
# e
# k



# ex:-

colors = ["Red","Green","Blue","Yellow"]
for color in colors:
    print(color)


# so basically output is 

# Red 
# Green
# Blue
# Yellow


# ex:- 


colors = ["Red","Green","Blue","Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)



# so now output is

# Red
# R
# e
# d
# Green
# G
# r
# e
# e
# n
# Blue
# B
# l
# u
# e
# Yellow
# Y
# e
# l
# l
# o
# w


# ***how you can print a 0 to 20000 number easily or just in a 2 line code
# so answer is :- to using a loop we can do it easily


for i in range (0,20000):
   print(i)

# so python interpret 1 2 3 4 5 6 ko type karega just like this
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# and note:- yadi hamne range 5 tak rakhi or to be precise we type (5) or (0,5)
# so python hume 4 tak type kar ke dega  ok


# aur hume python se print karwana hai ki jitane humne likhe hai number wo sare print ho for an example humne 5 tak bola
# so hum do chiz kar sakte hai firstly doing this:-
for i in range(0,5):
    print(i+1)
# or hum direct 6 hi likhenge ki python hume 5 tak print kar ke de


# ****while loop****

# so is me hum pahle variable ka use karte hai and then while for an example i am  trying understand thi
# ex:-

i = 0
while(i<3):
  print(i)
  i = i+1
# so output ayega
# 0
# 1
# 2



# ex (2):-
i = 0
while(i<=3):
    print(i)
    i = i+1


# so output ayega
# 0
# 1
# 2
# 3


# while loop number  se jyada complex condition me kaam ata hai

# ex:-
i = int(input("Enter the number: "))
while(i<= 38):
   i = int(input("Enter the number: "))
   print(i)


print("done with the loop")


# ****decremental while loop

# ex:

count = 5
while(count>0):
	print(count)
	count = count-1

# so out put is 
# 5
# 4
# 3
# 2
# 1


# in this case python interpreter first check count 5 ke barabar hai then count>0 ye condition match ho tab tak program  ko chalana hai
# then  print count
# and count is value de di hai last me count = count-1

# and hum isme count ki value count-1 ke bajaye count+1 kar de to ye infinite loop ban jayega


# *******else with while loop*******



count = 5
while(count>0):
	print(count)
	count = count-1
else:
   print("i am inside else")


# so is code me else last me kaam karega jab  while loop ki condition match nahi hogi tab


# so basically output is
# 5
# 4
# 3
# 2
# 1
# i am inside else


# *******function ******


# ex:-

def calculateGmean(a,b):
  mean = (a*b)/(a+b)
  print(mean)

a = 9
b = 8
#gmean1 = (a*b)/(a+b)
#print(gmean1)
calculateGmean(a,b)
c = 8
d = 7

#gmean2 = (c*d)/(c+d)
#print(gmean2)
calculateGmean(c,d)


#  so output is 
# 4.2325
# 3.73333333333

# now hum if ka bhi use karenge
# ex:-

def calculateGmean(a,b):
  mean = (a*b)/(a+b)
  print(mean)

a = 9
b = 8
if(a>b):
	print("First number is greater")

else:
	print("Second number is greater or equal ")
#gmean1 = (a*b)/(a+b)
#print(gmean1)
calculateGmean(a,b)
c = 8
d = 7
if(c>d):
	print("Fist number is greater")
else:
	print("Second number is greater or equal")
#gmean2 = (c*d)/(c+d)
#print(gmean2)
calculateGmean(c,d)


# also hum greater ke liye bhi function bana sakte hai for an example:-

def calculateGmean(a,b):
  mean = (a*b)/(a+b)
  print(mean)
def isGreater(a,b):
	if(a,b):
		print("first number is greater")
	else:
		print("second number is greater or equal")


a = 9
b = 8
isGreater(a,b)
calculateGmean(a,b)
#gmean1 = (a*b)/(a+b)
#print(gmean1)

c = 8
d = 70
isGreater(c,d)
#gmean2 = (c*d)/(c+d)
#print(gmean2)
calculateGmean(c,d)


# hum program ki body nai likhani to hum pass ka use karke usko execute nahi hone dege
# just like this

def calculateGmean(a,b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a,b):
	if(a,b):
		print("first number is greater")
	else:
		print("second number is greater or equal")

def islesser(a,b):
	pass


a = 9
b = 8
isGreater(a,b)
calculateGmean(a,b)
#gmean1 = (a*b)/(a+b)
#print(gmean1)

c = 8
d = 7
isGreater(c,d)
#gmean2 = (c*d)/(c+d)
#print(gmean2)
calculateGmean(c,d)


# that actually we seen in islesser body not excecute or islesser not execute


# *****break and continue statements

# 1) break statement


# this statement help to end the loop 
# for an example:-

for i in range (12):
	print("5 X", i+1,"=",5*(i+1))
	if(i== 10):
		break

print("Loop ko chodkar nikal gaya")


# so output is:-


# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 5 X 10 = 50
# Loop ko chhodkar nikal gaya

# 2)continue statement


# note:- difference between break statements and continue statements so in break Statement skip the loop and in continue  statement skip the iteration.


# example:-

for i in range(12):
	if(i==10):
		print("skip the iteration")
		continue
	print("5 X",i+1,"=",5*(i+1))

# so output is 


# 5 X 0 = 0
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# skip the iteration
# 5 X 11 = 55


# *****do while loop*****

# do while loop is loop in which set of instructions will execute at least once(irrespective of the condition)
# and then the repetition of loop's body will depend on the condition passes at the end of the while loop.
# it is also known as an exit-controlled loop.

# for an example:-

while True:
	number = int(input("Enter a positive number: "))
	print(number)
	if not number > 0:
		break

# ******function arguments******

# 4 type of argument

# 1)default argument

# we can provide a default value creating a function. this way the function assume a default value even
# if a value is not provided in the function call for that argument. 
# so basically isme value a and b ki value di ho pahel se and hum a ki ya b ki value baad me de to wo last wali value add hogi and rest (baki ki value)
# default argument se aayega 

# 2)keyword argument

# we can provide arguments with key = value , this way the interpreter recognizes the arguments by the parameter name.
# hence , the order in which the arguments are passed does not matter.
# so hum isme key and value denge so order also doesn't matter


# 4)required argument

# poore code me kisi particular chiz ki value missing ho 
# so wo required argument ban jayega

# in case we don't pass the argument with a key = value 
# syntax, then it is necessary to pass the argument in the correct
# positional order and the number of arguments passed should match with function definition.

# 5) variable length argument

# sometimes we may need to pass more arguments than those defined in the actual functions. this can be done by using
# variable length argument


#case 1)
def average(a,b):
	print("The average is ", (a+b)/2)
average (4,6)


# so output is :-
# The average is 5.0


# note:- in this a and b are required arguments 

#case 2)
def average(a=9,b=1):
	print("The average is " , (a+b)/2)

average ()

# so output is 
# The average is 5.0

#case 3)
def average(a=9,b=1):
	print("The average is " , (a+b)/2)

average (1,5)

# so output is :-
# The average is 3.0

# in this (#3) case) python intrpeter ignore 
# def average(a=9,b=1): this line or value and execute average (1,5)
# this line's value

# default argument so isme hum let us suppose 
# hum isme a ki value ko edit kar sakte hai for an example:-

def average(a=9,b=1):
	print("The average is " , (a+b)/2)
#average (4,6)
average (5)

# so output is 
# The average is 3.0


# and hum sirf b ki value dena chahte hai so
# type 

def average(a=9,b=1):
	print("The average is " , (a+b)/2)
#average (4,6)
average (b=9)

# so output is 
# The average is 9.0

# *********default argument 
# means aapne koi ek do value di and then baki ki sari value as default same as it is aajayegi

# ******keyword argument
#  means aap ne value di uska aap order change kar ke bhi likh sakte ho 
# for an example pahle c likh diya then a likh diya then e likh diya

# *****required argument 
# so isme hume kisi bhi particular variable ki value deni hi padegi
# for an example


def average(a,b=1):
	print("The average is " , (a+b)/2)
#average (4,6)
average (b=9)


# humne isme a ki value nahi di hai so hame a ki value last me to last me deni hi padegi
# varna error ayega

# ***variable length argument

def average(*numbers):
 sum = 0
 for i in numbers:
    sum= sum + i
 print(type(numbers))
 print("Average is: ", sum/len (numbers))
	
average (5,6)
	


# so output is
# <class 'tuple'>
# average is: 5.5


# *****keyword arbitary argument

def name(**name):
	print(type(name))
	print("Hello,", name["fname"],name["mname"],name["lname"])
name(mname= "buchanan", lname= "barnes", fname="james")

# so output is
# <class'dict'>
# Hello, james buchanan barnes

# *****return statement
# the return statement is used to return the value of the expression back to the calling function.
# example:

def name(fname,mname,lname):
	return"hello, " + fname + " " + mname + " " + lname
print(name("james","buchanan","barnes"))

# so output is
# hello, james buchanan barnes


# ****list chapter:-


marks = [3,5,6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])


# so output is
# [3,5,6]
# <class 'list'>
# 3
# 5
# 6


# list are ordered collection of data items.
# they store multiple items in a single variable.
# list items are separated by commas and enclosed within square brackets.
# list are changeable mean by we can alter them after creation.
# note:- tuple not changeable 

# list me hum string , boolian , and also integer add kar sakte hai .

# for an example:-

marks = [3,5,6,"naishal",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])


# so output is

# [3,5,6,'naishal',True]
# 3
# 5
# 6
# naishal
# True


# so in list string single quote me milata hai hume output me
# for an example
# 'naishal'

# ******negative  index***********

marks = [3,5,6,"naishal",True]
print(marks[-3])#negative indexing
print(marks[len(marks)-3])#positive  indexing
print(marks[5-3])#positive indexing
print(marks[2])


# so output is 
# 6
# 6
# 6
# 6

# we can also check something is present or absent
# **check whether an item in present in the list??


marks = [3,5,6,"naishal",True]
if 7 in marks:
	print("Yes")
else :
	print("No")

# so output is 
# No


marks = [3,5,6,"naishal",True]
if "6" in marks:
	print("Yes")
else :
	print("No")
# so output is 
# No

# it is because ki 6 hamari list me integer me hai na ki string ke form me
# so hamne  python interpreter se puchha ki 6 as string hai ki nai so obviously python interpreter say no

# we can also check this ki i mean:
#same thing applies for string  as well!
marks = [3,5,6,"naishal",True]
if "na" in  "naishal":
	print("Yes")


# output is
# Yes 


# *slicing and jump index***

# for an example:-
marks = [3,5,6,"naishal",True,12,45,51,4,54,65]
print(marks)
print(marks[1:9])
print(marks[1:9:3])

# so ouput is:-
# [3,5,6,'naishal',True,12,45,51,4,54,65]
# [5,6,'naishal',True,12,45,51,4]
# [5,True,51]

print(marks[:])   = print(marks)
# yadi app semi colon ke aage khali jagah chhodte ho to pyhton interpreter usse by default 0 ki index de dega and last me chhodte hoto by default usse len(marks) consider karega


# **list comprehension****
lst = [i for i in range(4)]
print(lst)


# output
# [0,1,2,3]


lst = [i*i for i in range(4)]
print(lst)


# so output is
# [0,1,4,9]

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

# so output is
# [0,1,4,9,16,25,36,49,64,81]
# [0,4,16,36,64]


# list method****


# 1) list.sort:-

# so basically isme list increasing order me set ho jati hai for an example


l = [11,45,1,2,4,6]
print(l)
l.sort()
print(l)

# so output is
# [11,45,1,2,4,6]
# [1,2,4,6,11,45]

# and reverse order  me karana ho to 
l = [11,45,1,2,4,6]
print(l)
l.sort(reverse=True)
print(l)


# so output is
# [11,45,1,2,4,6]
# [45,11,6,4,2,1]

# 2) l.reverse :-

# ye hamari original list ko ulta kar deta hai.
# for an example 
l = [11,45,1,2,4,6]
print(l)
l.reverse()
print(l)

# so output is 
# [11,45,1,2,4,6]
# [6,4,2,1,45,11]

# 3)index()

l = [11,45,1,2,4,6]
print(l)
print(l.index(1))

# so output is 
# [11,45,1,2,4,6]
# 2


# 4)count()

l = [11,45,1,2,4,6]
print(l)
print(l.count(1))

# so output is
# [11,45,1,2,4,6]
# 1

l = [11,45,1,2,4,4,4,4,4,6]
print(l)
print(l.count(4))

# so output is
# [11,45,1,2,4,6]
# 5


# 5)copy()

l = [11,45,1,2,4,6]
print(l)
m = l.copy()
m[0]=0
print(l)
print(m)

# so output is
# [11, 45, 1, 2, 4, 6]
# [11, 45, 1, 2, 4, 6]
# [0, 45, 1, 2, 4, 6]


# 6)append()

# so basically is list ke method ki help se hum log list me kuchh bhi add kar sakte hai 
# for an example

l = [11,45,1,2,4,6]
print(l)
l.append(7)
print(l)

# so output is
# [11, 45, 1, 2, 4, 6]
# [11, 45, 1, 2, 4, 6, 7]


# 7)insert()

# so hum is list method ki help se koi bhi index pe kuchh  bhi value change kar sakte hai 
# for an example
l = [11,45,1,2,4,6]
print(l)
l.insert(1,889)
print(l)

so output is 
[11,45,1,2,4,6]
[11,899,1,2,4,6]


8)extend()
so hum is list method se do list ko jod sakte hai for an example


l = [11,45,1,2,4,6]
print(l)
m = [900,1000,1100]
l.extend(m)
print(l)


so output is
[11,45,1,2,4,6]
[11,45,1,2,4,6,900,1000,1100]

*************concatenating two list******

isme hume ye ek plus point milta hai ki hamari origianl list me ki change nai hota
for an example:-
l = [11,45,1,2,4,6,1,1]
print(l)
m = [900,1000,1100]
k = l + m
print(k)
print(l)

so output is
[11,45,1,2,4,6,1,1]
[11,45,1,2,4,6,1,1,900,1000,1100]
[11,45,1,2,4,6,1,1]


***tuples****
tup = (1,5,6)
print(type(tup),tup)


so ouput is 
<class 'tuple'> (1,5,6)

hum ese hi 1 number ka tuple banaye to wo integer hoga na ki tuple
use tuple banane ke liye hume 
ese banana padega
for an example:-


tup = (1,)
print(type(tup),tup)

so output is
<class'tuple'>(1,)

hum comma nai lagate to integer consider karta python interpreter

for an example:-
tup = (1)
print(type(tup),tup)


so output is
<class'int'>(1)



NOTE:- TUPLE CAN'T CHANGEABLE

tup = (1,2,76,342,32,"green",True)
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

so output is 
<class'tuple'>(1,2,76,342,32,'green',True)
1
2
76
342

**check for item:-

tup = (1,2,76,342,32,"green",True)
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
if 342 in tup:
	print("Yes 342 is present in this tuple")

so output is 
<class'tuple'>(1,2,76,342,32,'green',True)
1
2
76
342
Yes 342 is present in this tuple

tuple me bhi slicing kar sakte  hai but isme naya tuple ban jayega


tup = (1,2,76,342,32,"green",True)
print(type(tup),tup)
tup2 = tup[1:4]
print(tup2)


so output is:
<class'tuple'>(1,2,76,342,'green',True)
(2,76,342)


NOTE:-
tuples are immutable.
strings are immutable.
BUT

		LIST ARE MUTABLE

so we can chnage list .
we can't change string and tuple


****tuple methods******
tuples are immutable , hence if you want to add , remove or change tuple items, then first you must convert the tuple to alist.
then perform operation on that list and convert it back to tuple.

example:-
countries = ("spain","italy","india","England","germany")
temp = list(countries)
temp.append ("Russia")		#add item
temp.pop(3)			#remove item
temp[2] = "Finland"		#change  item
countries = tuple(temp)
print(countries)


so output is
('spain','italy','Finland','germany','Russia')

so basically hum tuple ko change nahi kar sakte but nayi tuple bana sakte hai .
jaise humne  uper banaya  so usme changes karne ke liye hum 3 feature ka use karenge.

add karne ke liye append ka use kiya.
remove karne ke liye pop ka use kiya.
change karne ke liye a[index] = "new value"


hum do tuple ko concatenate karege to hume tisara tuple milenaga
for an example:-


countries = ("Pakistan","Afghanistan","Bangladesh","shri lanka")
countries2 = ("Vietnam","India","china")
southeastasia = countries + countries2
print(sounteastasia)


so ouput is
('Pakistan','Afghanistan','Bangladesh','shri lanka','Vietnam','India','china')


tuple method 
no 1)
count()

so basically isse hum tuple me koi given chiz kitani baar aati hai wo dekh sakte hai .
for an example:-
tuple1 = (0,1,2,3,2,3,1,3,2,3)
a = tuple1.count(3)
print('count of 3 in tuple1 is:',a) 


so output is :
count of 3 in tuple1 is: 4


no 2)
index()

tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = tuple1.index(3)
print('index of 3 in tuple1 is:',res) 

so output is:

index of 3 in tuple1 is: 3

tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = tuple1.index(3,4,8)
print('index of 3 in tuple1 is:',res) 


so output is
index of 3 in tuple1 is: 5

#first occurence hoga wo dikhayega

****f-strings


letter="hey my name is {} and i am from  {}"
country="india"
name="harry"

print(letter.format(name,country))

so output Is

hey my name is harry and i am from india


so hum ese likhte so


letter="hey my name is {} and i am from  {}"
country="india"
name="harry"
print(letter.format(country,name))

so output is
hey my name is india and i am from harry 

so hum f string ki help se hum string me variable daal sakte hai 

for an example:

letter="hey my name is {1} and i am from  {0}"
country="india"
name="harry"
print(f"hey my name is {name} and i am from  {country}")

so output is:
hey my name is harry and i am from india

so hum isme point ke baad 2 digit chahiye so hum ese use kar sakte hai

txt = "for only {price:.2f}dollars!"
print(txt.format(price = 49.09999))


so output is

for only 49.10 dollars!

so .2f lagane se hum do decimal tak print kar sakte hai

so abhi humne complicated type kiya hum ise f string me 
ese likh sakte hai


price = 49.09999
txt = f"for only {price:.2f}dollars!"
print(txt)

so ab output aayega

for only 49.10 dollars!

hum calcualtion as string bhi kar sakte hai with help of f string

print(f"{2*30}")

so output is 
60
 

and hum type dekh sakte hai 

print(type(f"{2*30}"))


so output is

<class 'str'>


so hum variable ko ese print kar sakte hai
so hum variable ko print karane ke liye hum double curly brackets use karenge  

print(f"hey my name is {{name}} and i am from {{country}}")


so output is
hey my name is {name} and i am from {country}

****doc  string
doc string is present at just below the function line

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)


so output is 
25

doc string ko print karne ke liye hum command denge

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

print(square.__doc__)

so output is
25
Takes in a number n, returns the square of n



doc string hamesha funcion ke just niche aayega

comment change karne se program change nai hota but doc string change karne se program change ho sakta hai

***zen of python****
so hum 
import this 
likhte hai so output ye aata hai
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


******recursion******
in python, we know that a funcion can call other functions. it is even possible for the function to call itself. these types of construct are termed as recursive functions.

factorial 0 is 1
for an example:

def factorial(n):
 if(n==0 or n==1):
  return 1
 else:
  return n*factorial(n-1)


print(factorial(3))
print(factorial(4))
print(factorial(5))

so output is
6
24
120

fibonacci sequence is completed

*****sets in python*****


s={2,4,2,6}
print(s)

so output is 
{2,4,6}

set me ek chiz or number repeat nai hota

set culry bracket me band hoge 
set is unchangable 
set do not contain duplicate item 

just like list sets me bhi multiple data type aa skate hai 

for an example:

info ={"carla",19,False,5.9,19}
print(info)

sets me order ki koi gerrunty nai hai 
output is 
{False, 19, 5.9, 'carla'}

so to make empty set
we do like this


n=set()
print(type(n))

so now ouput is 
<class'set'>

how to access set items so now we do this to access are set item 

info ={"carla",19,False,5.9,19}
print(info)
for item in info:
  print(item)


so output is 
{False, 19, 5.9, 'carla'}
False
19
5.9
carla

iska order kuchh bhi ho sakta hai 

*****set method***

1)union() and update()


union method ki help se hum do sets ko merge kar skate hai
for an example:

s1 = {1,2,5,6}
s2 = {3,6,7}

print(s1.union(s2))

so output is 
{1,2,3,5,6,7}

and hum update method ki help se set ko update kar sakte hai 

for an example

s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)


so now output is 
{1,2,3,5,6,7}
{1,2,3,5,6,7} {3,6,7}


cities = {"tokyo","madrid","berlin","delhi"}
cities2 = {"tokyo","seoul","kabul","madrid"}
cities3 = cities.union(cities2)
print(cities3)


so output Is
{'madrid', 'delhi', 'tokyo', 'kabul', 'berlin', 'seoul'}

2)intersection and intersection_update 


so basically intersection me ash hota hai ki koi bhi value dono sets me hoto
wo print hogi sirf aur sirf
cities = {"tokyo","madrid","berlin","delhi"}
cities2 = {"tokyo","seoul","kabul","madrid"}
cities3 = cities.intersection(cities2)
print(cities3)


so output Is
{'tokyo','madrid'}


so with the help of intersection_update hum log sets ko update kar pate hai so jo dono sets me 
common value hogi wo value sirf print hogi and baki ki value remove ho jaayegi


cities = {"tokyo","madrid","berlin","delhi"}
cities2 = {"tokyo","seoul","kabul","madrid"}
cities.intersection_update(cities2)
print(cities)


so output Is
{'tokyo','madrid'}


so now lets move forwad 
3) symmetric_differnce and symmetric_differnce_update

so with the helpof symmetric_differnce hum log jo non common thing hoti ahi usko hum print kara sakte  hai 
 
 for an example:


cities = {"tokyo","madrid","berlin","delhi"}
cities2 = {"tokyo","seoul","kabul","madrid"}
cities3=cities.symmetric_differnce(cities2)
print(cities3)

so ouput is
{'berlin','kabul','seoul','delhi'}

cities = {"tokyo","madrid","berlin","delhi"}
cities2 = {"tokyo","seoul","kabul","madrid"}
cities.symmetric_differnce_update(cities2)
print(cities)

so output is 
{'berlin', 'seoul', 'kabul', 'delhi'}

3)isdisjoint():

disjoint ki help se hum ye check kar sakte hai ki dono sets completly match nai khate 
match khaye to False and match na khaye to True
cities = {"tokyo","madrid","berlin","delhi"}
cities2 = {"tokyo","seoul","kabul","madrid"}
print(cities.isdisjoint(cities2))

so output is 
False


4) issuperset
so isse hum ye dekh sakte hai ki koi ek set me jo value hai wo dusare set me present hai 

for an example:
cities = {"tokyo","madrid","berlin","delhi"}
cities2 = {"seoul","madrid"}
print(cities.issuperset(cities2))
cities3 = {"seoul","madrid","kabul"}
print(cities.issuperset(cities3))

so output is 
False
False

5) issubset

so basically it is opposite to issuperset.

cities = {"tokyo","madrid","berlin","delhi"}
cities2 = {"seoul","madrid"}
print(cities.issuperset(cities2))
cities3 = {"seoul","madrid","kabul"}
print(cities.issuperset(cities3))


6)add()

cities = {"tokyo","madrid","berlin","delhi"}
cities.add("helsiniki")
print(cities)

so output is 
{'tokyo','madrid','berlin','helsiniki','delhi'}

7)remove()

cities ={"tokyo","madrid","berlin","delhi"}
cities.remove("tokyo")
print(cities)

so output Is
{'delhi', 'madrid', 'berlin'}

8)pop()

cities = {"tokyo","madrid","berlin","delhi"}
item = cities.pop()
print(cities)
print(item)

so output is 
{'tokyo', 'berlin', 'delhi'}madrid


9) del
so hum iski help se set ko delete kar skate hai

cities = {"tokyo","madrid","berlin","delhi"}
del cities
print(cities)

so now cities is not print and an error occured

10) clear
so with the help of this we can clear our sets
or empty set formed

cities = {"tokyo","madrid","berlin","delhi"}
cities.clear
print(cities)

11) check if item exists


info = {"carla",19,False,5.9}
if "carla" in info:
  print("carla is present")
else:
  print("carla is absent")


so output is 
carla is present 


*****dictionary*****

dic = {
  "harry" = "human being"
  "spoon" = "object"
}

print(dic["harry"])

so output is 

human being

or 

dic = {
  344 = "harry"
  56 = "shubham"
  678 = "zakir"
  567 = "neha"
}

print(dic[567])

so output is 
neha

info = {'name':'karan', 'age':19,'eligible':'True'}
print(info)
print(info['name'])
print(info.get('eligible'))

so output is 
('name':'karan', 'age':19,'eligible':'True')
karan
True


so hum info.get type se karate hai so error nahi aate hai
for an example

info = {'name':'karan', 'age':19,'eligible':'True'}
print(info)
print(info['name'])
print(info.get('eligible'))
print(info.get('name'))
print(info.get('name2'))

so output Is

('name':'karan', 'age':19,'eligible':'True')
karan
True
karan
None

so hum ese karate to error aati 

info = {'name':'karan', 'age':19,'eligible':'True'}
print(info)
print(info['name2'])
print(info.get('eligible'))
print(info.get('name'))
print(info.get('name2'))

so output is error

{'name': 'karan', 'age': 19, 'eligible': 'True'}
Traceback (most recent call last):
  File "c:\Users\NAISHAL NADIYA\OneDrive\Desktop\python practice\dictionary in python.py", line 3, in <module>
    print(info['name2'])
          ~~~~^^^^^^^^^
KeyError: 'name2'

so sari key ko access karne ke liye hum use karenge ye 

info = {'name':'karan', 'age':19,'eligible':'True'}
print(info)
print(info.keys())

so output is 
{'name': 'karan', 'age': 19, 'eligible': 'True'}
dict_keys(['name', 'age', 'eligible'])


hum for ka bhi use kar sakte hai 

info = {'name':'karan', 'age':19,'eligible':'True'}
print(info)
print(info.keys())
for key in info.keys():
  print(info[key])
  
output is 
{'name': 'karan', 'age': 19, 'eligible': 'True'}
dict_keys(['name', 'age', 'eligible'])
karan
19
True

also we use value 

info = {'name':'karan', 'age':19,'eligible':'True'}
print(info)
print(info.keys())
print(info.values())
for key in info.keys():
  print(info[key])

so output is 
{'name': 'karan', 'age': 19, 'eligible': 'True'}
dict_keys(['name', 'age', 'eligible'])
dict_values(['karan', 19, 'True'])
karan
19
True

f string use :

info = {'name':'karan', 'age':19,'eligible':'True'}
print(info)
print(info.keys())
print(info.values())
for key in info.keys():
  print(f"the value corresponding to the key {key} is {info[key]}")

so output is

{'name': 'karan', 'age': 19, 'eligible': 'True'}
dict_keys(['name', 'age', 'eligible'])
dict_values(['karan', 19, 'True'])
the value corresponding to the key name is karan
the value corresponding to the key age is 19
the value corresponding to the key eligible is True

also we use item

info = {'name':'karan', 'age':19,'eligible':'True'}
print(info.items())
for key, value in info.items():
  print(f"the value corresponding to the key {key} is {value}")


so output is 

dict_items([('name', 'karan'), ('age', 19), ('eligible', 'True')])
the value corresponding to the key name is karan
the value corresponding to the key age is 19
the value corresponding to the key eligible is True

*****dictionary method****

1) update() 

ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}

ep1.update(ep2)
print(ep1)

so output is 
{122:45,123:89,567:69,670:69,222:67,566:90}

dictionary follows order but sets do not follow order


2)clear()

hum clear method ka use tab karte hai jab hum empty dictionary print karani ho 
ya fir poori dictionary khali karni ho without deleting

for an example:

ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.clear()
print(ep1)

so output is 
{}

or hum empty dictionary kuchh ese bhi bana sakte hai 

empt={}
print(empt)

so out put Is
{}

3)pop()

the pop() method removes the key-value pair whose key is passed as a parameter.

for an example:

ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.pop(122)
print(ep1)

so output is 

{123:89,567:69,670:69}


4)popitem()

so ye basically last wali item pair ko remove kar deta hai 

ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.popitem()
print(ep1)

so output is 
{122:45,123:89,567:69,}

5)del:

we can also use the del keyword to remove a dictionary item.

so hum del ki help se dictionaryko delete kar sakte hai 

ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.popitem()
del ep1
print(ep1)

so error occur becausewe delete ep 1 and then print ep 1

if key is not provided , then the del keyword will delete the  dictionary entirely.

ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.popitem()
del ep1[122]
print(ep1)

so output is 
{123:89,567:69,670:69}


***for loop with else**

for i in []:
  print(i)
else:
  print("sorry no i")


so output is
sorry no i

for i in range (6):
  print(i)
  if i == 4:
   break

else:
   print("sorry no i")



in this case else is not execute because if is successfuly excecuted

so ouput is
0
1
2
3
4

i=0
while i<7:
 print(i)
 i = i+1
 if i == 4
  break

else:
 print("sorry no i")


so output is same as for loop
0
1
2
3
4

if hum log ise break na kare to else print hoga 

i=0
while i<7:
 print(i)
 i = i+1

else:
 print("sorry no i")

so now  output is 
0
1
2
3
4
5
6

for x in range(5):
  print("iteration no{} in for loop".format(x+1))

else:
  print("else block in loop")

print("Out of loop")

so output Is

iteration no 1 in for loop 
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop 
Out of loop 

*****exception handling in python*****

we can build a table 

a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")


for i in range(1,11):
     print(f"{int(a)} X {i} = {int(a)*i}")

so output is 
Enter the number: 1
Multiplication table of 1 is: 
1 X 1 = 1
1 X 2 = 2
1 X 3 = 3
1 X 4 = 4
1 X 5 = 5
1 X 6 = 6
1 X 7 = 7
1 X 8 = 8
1 X 9 = 9
1 X 10 = 10


so now we enter the input like this 
harry or other thing except integer
so we get a error so now as developer 
we fix this error like this

try:
    a = input("Enter the number: ")
    print(f"Multiplication table of {a} is: ")


    for i in range(1,11):
         print(f"{int(a)} X {i} = {int(a)*i}")

except ValueError:
     print("value error occured! please type integer.")



one more example

try:
    a = input("Enter the number: ")
    print(f"Multiplication table of {a} is: ")


    for i in range(1,11):
         print(f"{int(a)} X {i} = {int(a)*i}")

except Exception as e:
     print(e)


this handled all exception


handling multiple exception
try:
     num=int(input("Enter an integer: "))
     a = [6,3]
     print(a[num])
except ValueError:
     print("Number entered is not an integer.")
except IndexError:
     print("Index Error")


***finally clause****

try:
    l=[1,5,6,7]
    l=int(input("Enter the index: "))
    print(l(i))
except:
    print("Some error occurred")

finally:
    print("I am always executed")


so basically error aaye na aaye kuchh bhi ho finally block chalega hi chalega 
and especially ye function me jyada kaam ata hai


***custom error**


a= int(input("Enter any value between 5 and 9"))

if(a<5 or a>9):
  raise ValueError("value should be between 5 and 9")


*****build kbc**********

questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")


short hand if else statement****

a=330
b=3303
print("A") if a>b else print("=")
if a==b else print("B")

print(9) if a>b else ""


***pending***