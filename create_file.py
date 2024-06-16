with open("goel.txt","w") as xyz:
    xyz.write("this is stmt-1 \n")
    xyz.write("this is stmt-2")
with open("goel.txt","r") as xyz2:
    print(xyz2.read()) #this will read entire content
       
