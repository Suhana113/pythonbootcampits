# #make an excel file with name email and address
# #make an json file with name email and address
# #make an csv file with name email and address
f=open("excel.xls","w")

x=input("Write the candidate name:")
y=input("Write the candidate age:")
z=input("Write the candidate phone number:")
datum= x+y+z
f.write(datum)
f.close()
f=open("excel.xls","r")
print(f.read())

#jason
f=open("jason.json","w")

x=input("Write the candidate name:")
y=input("Write the candidate age:")
z=input("Write the candidate phone number:")
datum= x+y+z
f.write(datum)
f.close()
f=open("jason.json","r")
print(f.read())
f=open("hi.csv","w")

x=input("Write the candidate name:")
y=input("Write the candidate age:")
z=input("Write the candidate phone number:")
datum= x+y+z
f.write(datum)
f.close()
f=open("hi.csv","r")
print(f.read())