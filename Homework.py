#task---- take list and create new list of even and odd list
#task2 --- login system and show do you want to continue--string

# l = []
# n = int(input("Enter the number of elements in list:\n"))
# for i in range(n):
#     inp= int(input("Enter the element in list:"))
#     l.append(inp)
#     l.sort()
#
# print("list is",l)
# even = []
# odd = []
# for item in l:
#     if item%2==0:
#         even.append(item)
#         even.sort()
#     else:
#         odd.append(item)
#         odd.sort()
#
# print("Even elements in list:",even)
# print("Odd elements in list:",odd)
#
#task2 --- login system and show do you want to continue--string
# s = True
# password = "Anuroop1602"
# while s:
#     i = input("Enter your password:")
#     if i =="Anuroop1602":
#         prompt = input("Password Correct,Do you wish to continue Y for Yes and N for No?:").upper()
#         if prompt == "Y":
#             print("Welcome to the Entertainment system!")
#             break
#         elif prompt == "N":
#             print("GoodBye")
#             break
#         else:
#             print("Invalid Input")
#     else:
#         print("Please enter a Valid Prompt!")
#         continue
#18th Feb
#task 3

##Data Structures
##list---[]
##om=[]
##om=[1,5,2,3,4,5,1,3,7,8,5,'a','b']
##print(om)
##print(type(om))
##fetch [] ---indexing start0
##print(om[4])
##print(om[-1])
##print(om[2:5])
##print(om[-4:-1])
##
##om[4]=10
##print(om)
##
##om.append(23)
##print(om)
##om.append([11,22,33])
##print(om)
##
##om.extend([1,3,5])
##print(om)
##
##om.insert(4,1)
##print(om)

##print(om.pop())
##
##print(om.pop(6))
##
##print(om.remove(5))
##
##print(om.clear())
##
##del om
##print(om)



##om=[1,5,2,3,4,5,1,3,7,8,5,'a','b']
##print(om)
##
##for i in om:
##    print(i)
##    if i%2==0:
##        print("Even no is:",i)




###string--str---''   ""    ''' '''     """ """
# mystr="Hi Friends Welcome to Livewire"
# print(mystr)
# print(type(mystr))
#
# print(mystr[11])
# print(mystr[-1])
# print(mystr[11:18])
# print(mystr[:10])
# print(mystr[-8:])
#
# ##mystr="H"
# ##print(mystr)
#
# print(mystr.capitalize())
#
# print(mystr.lower())
#
# print(mystr.upper())
#
# print(mystr.count('i'))
#
# print(mystr.index('Welcome'))
#
# mystr="Hi Friends {} Welcome to Livewire".format("Hello")
#
# ##del mystr
# ##print(mystr)
#
#
# for i in mystr:
#     print(i)

##Task1---Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.
##Task2---Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
###Task3---Take a list of 20 random numbers and create new even and odd list using loops
##Task4---Take a give string "Python is made for everybody who loves coding"and apply string method
##Task5---Take string "Python is made for everybody who loves codind" and check inside string count of y
##Task6---Take 2 string"Python is is easy to learn" & "Python is popular language" data and make one new string

#task 6 Take 2 string"Python is is easy to learn" & "Python is popular language" data and make one new string

s1 = "Python is is easy to learn"
s2 = "Python is popular language"
s3 = s1+s2
print(s3)

#Task5---Take string "Python is made for everybody who loves coding" and check inside string count of y

s4 = "Python is made for everybody who loves coding"
print("The count of y letters in the string is",s4.count("y"))

##Task2---Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
il=[]
n = int(input("enter the number of elements in list:"))
for item in range(n):
    inn= int(input("Enter a digit:"))
    il.append(inn)
    il.sort()
print(il)
if n>=4:
