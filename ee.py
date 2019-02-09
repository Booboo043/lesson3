
 #set the attributes
    def set_name(self, name):
        self.name = name

    def set_id(self, family):
        self.family = family

    def set_department(self, department):
        self.department = department

    def set_salary(self, salary):
        self.salary = salary

 #return the attributes
    def get_name(self):
        return self.name

    def get_family(self):
        return self.family

    def get_department(self):
        return self.department

    def get_salary(self):
        return self.salary

#return the objects state as a string

    def __str__(self):
        return 'Name: ' + self.name + \
               '\nFamily: ' + self.family + \
               '\nDepartment: ' + self.department + \
               '\nSalary: ' + self.salary



html=https://en.wikipedia.org/wiki/Deep_learning
bsObj=BeautifulSoup(html.content,"html.parser")
print(bsObj)