"Customer Management System"
#BLL:Business Logic Layer
id_list=[]
name_list=[]
age_list=[]
mob_list=[]
def addCustomer(id,name,age,mob):
    id_list.append(id)
    name_list.append(name)
    age_list.append(age)
    mob_list.append(mob)
    return
def searchCustomer(id):
    index=id_list.index(id)
    return index
def deleteCustomer(id):
    i=id_list.index(id)
    id_list.pop(i)
    name_list.pop(i)
    age_list.pop(i)
    mob_list.pop(i)
def modifyCustomer(id,name,age,mob):
    i=id_list.index(id)
    name_list[i]=name
    age_list[i]=age
    mob_list[i]=mob

#PL: Presentation Layer
def showCustomer(i):
    print("Cust ID:",id_list[i],"Cust Name:",name_list[i],"Cust Age:",age_list[i],"Cust Mob:",mob_list[i])

print("Welcome to lavish's Management System")
while(1):
    choice=input("Enter Choice:1 for Add Cust, 2 Search, 3 Delete, 4 Modify, 5 Display all, 6 for Exit::  ")
    if(choice=="1"):
        id=input("Enter Customer ID: ")
        name = input("Enter Customer Name:")
        age = input("Enter Customer Age:")
        mob = input("Enter Customer Mob:")
        addCustomer(id,name,age,mob)
        print("Customer Added Successfully")
    elif(choice=="2"):
        id=input("Enter Customer Id to Search:")
        i=searchCustomer(id)
        showCustomer(i)
    elif(choice=="3"):
        id=input("Enter Customer Id to Delete:")
        deleteCustomer(id)
        print("Customer Deleted Successfully")
    elif(choice=="4"):
        id=input("Enter Customer Id to Modify:")
        name=input("Enter Customer updated name:")
        age = input("Enter Customer updated age:")
        mob = input("Enter Customer updated mob:")
        modifyCustomer(id,name,age,mob)
        print("Customer Modified Successfully")
    elif(choice=="5"):
        for i in range(len(id_list)):
            showCustomer(i)
    elif(choice=="6"):
        print("Thanks for using lavish's CRM")
        break
    else:
        print("Incorrect Choice")



