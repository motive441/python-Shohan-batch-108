# class Person:
#     def Information(self,id,name,depertment):
#         return id,name,depertment

# class Student(Person):
#     def st_info(self,st_roll):
#         return st_roll


# em_obj=Student()

# my_var=em_obj.Information(202,'Shohan','EEE')
# my_var1=em_obj.st_info('202272')

# print (my_var,my_var1)

# class employee:
#     def emp_info(self,Id,name,department):
#         return Id, name, department
# obj_emp = employee()
    
# class present_add:
#     def add1(self,section,block,road, house):
#         return section,block,road, house
# obj_pre_add = present_add()
    
# class permanent_add:
#     def add2(self,vill,thana,district):
#         return vill,thana,district
# obj_par_add = permanent_add()
    
# class all_class(employee,present_add, permanent_add):
#     pass
    
# obj1 = all_class()

# m_info = obj1.emp_info(100,'Aslam', 'Admin')
# m_preadd = obj1.add1(10, 'C', 14, 6)
# m_peradd = obj1.add2('Rasulpur', 'Nandail', 'Mymensingh')

# print(m_info, m_preadd, m_peradd)



class Person():
    def info(self,ID,name,age,dep):
        return ID,name,age,dep
class Student(Person):
    def info_student(self,roll):
        return roll
class Teacher(Person):
    def t_info(self,salary):
        return salary
class Emp(Person):
    def emp_info(self,designation):
        return designation
em_obj=Student()
e_var1=em_obj.info(1001,'asraf',39,'CSE')
e_var2=em_obj.info_student(101)
print(e_var1,e_var2)

