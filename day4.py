#looping ,function,oops
#switch condition is replaccement of multiple if else block

# friendname=["pawan","ivan","anshu"]
# #print before add name
# print("before",friendname)
# #to add the new friend name in list
# friendname.append("dil bhardwaj")
# #print after adding name
# print("After",friendname)

# #to add the name in specific position
# friendname.insert(0,"harsh")
# friendname.insert(3,"harsh")
# #print after adding name at 0 index
# print("add name at index 0",friendname)
# # #to remove the name from list
# # friendname.remove("harsh")
# # #print after removing name from the list
# # print(friendname)
# #to clear the list
# # friendname.clear()
# # print(friendname)

# friendname.pop(2)
# print(friendname)
# #whenever we use pop it remove last word but we use index in it it remove list from start
# #to sort the list it work when data is similar it not work data is string and intergers
# friendname.sort()
# print(friendname) 

#to print the given list
# for names in friendname:
#     print(names)

#     #to print the 1 to 10 list
#     numbers=[1,2,3,4,5,6,7,8,9,10]
# for number  in numbers:
#     print(number)  

#     #range
#     for x in range(11):
#         print(x)
# #for(int x = 0; x<10;x++)
# for x in range(1,11)
# print(x)

#to print the even no 1 to 10 using for and if
# for evenNo in range(2,11,2):
#     print(evenNo)

#     #method2
#     for no in range(1,11):
#         if no %2 ==0:
#             print(no)

#sets used to store the data and data is changeable eg. adhar number cannot change
# sets = {"pawan","ivan","anshu","ivan"}
# sets.add("harsh")
# sets.remove("harsh")
# sets[0] ="ghfgdh"
# print(sets)
# print(type(sets))

#set is unchangeable and unordered 

# friendname=["ahana","jiggu","vANDU","Shalu","Shilpi"]
# friendname.sort()
# print(friendname)

# for a in friendname:
#     print(friendname)

#     #datetime import
# import datetime
# x = datetime.datetime.now()
# print(x.month)

# #with the help of this function how many days old i am
# #to create new file and add my name also close the file it help to make notepad file application we can create any type of file expected image file and video
# f=open("suhanafile.txt","w")
# f.write("my name is suhana,i am mca student")
# f.close() 
# f = open("suhanafile.txt","r")
# print(f.read())

# #to create new file and add my name also close the file
# name=input("Enter your name")
# email=input("Enter your name")
# collegename=input("Enter your collegename")
# data= name + email + collegeName

# f=open("suhu.txt","w")
# f.write("")
# f.close() 
# f = open("suhanafile.txt","r")
# print(f.read())

# #while print 1 to 10
i=1
while i < 11:
    print(i)
    i=i+1

    
    # i=10
    # while i > 10:
    #     print(i)
    #     i=i-1

 #function in python
 #create function to print statement
def myFunction():
     print("my function clled")

 #call the function by name
myFunction()

def myFunction(x,y):
     z=x*y
     print("area is",z)

 #call the function by name
width = int(input("Enter the width"))
height = int(input("Enter your height"))
myFunction(height,width)

area = myFunction(width,height)
print("the area is", area)


        





