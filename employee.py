#create a class named Employee

class employee:
    empcnt = 0
    #initialize the attributes
    def __init__(self, name, family, department, salary):
        self.name = name
        self.family = family
        self.department = department
        self.salary = salary
        employee.empcnt+=1
    def display(self):
        print("name is",self.name,"family is",self.family,"department is",self.department,"salary is",self.salary)
class fulltime(employee):
    def __init__(self,n,f,d,s):
        employee.__init__(self,n,f,d,s)
employee1=employee("TOM",'SMITH','management','5000')
employee2=employee("ANNA",'WHITE','market','3500')
employee3=employee("JENNY",'COLIN','HR','4000')
employee4=employee("BOB",'GREEN','market','5000')
employee5=employee("JACK",'HARRI','sales','2500')
print(employee1.display())
print(employee2.display())
print(employee3.display())
print(employee4.display())
print(employee5.display())
print("total employee",employee.empcnt)

lst=[5000,3500,4000,5000,2500]
def average(lst):#Averaging List Data
	avg = 0
	avg = sum(lst)/len(lst)##call sum function summation
	return avg
print("avg = %.3f"%average(lst))
