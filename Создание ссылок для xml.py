# 2000 100 000 to 2003 599 999
for item in range(2002000001,2002200001,1):
    with open("output.txt", "a") as external_file:
        print("<record from=","\"",item,"\"", sep="", file=external_file)
        print("to=\"graphics/pictures/person/",item,"/portrait\"/>", sep='', file=external_file)
        external_file.close()

#StaffFind 2000350000 2000500000 +
#StaffFind 2000500001 2000700001 +
#StaffFind 2000700001 2000900001 +
#StaffFind 2000900001 2001000001 +
#StaffFind 2001000001 2001200001 +
#StaffFind 2001200001 2001400001 +
#StaffFind 2001400001 2001600001 +
#StaffFind 2001600001 2001800001 +
#StaffFind 2001800001 2002000001 +
#StaffFind 2002000001 2002200001
#StaffFind 2002200001 2002400001
#StaffFind 2002400001 2002600001
#StaffFind 2002600001 2002800001
#StaffFind 2002800001 2003000001
#StaffFind 2003000001 2003200001
#StaffFind 2003200001 2003400001
#StaffFind 2003400001 2003600001