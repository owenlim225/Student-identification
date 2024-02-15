import datetime

class Student:
    def __init__(self, id_number:int, name:str, course:str):
        self.id_number = id_number
        self.name = name
        self.course = course
        
    def __str__(self) -> str:
        return f"{self.id_number} - {self.name} - {self.course}"

    #check if input is valid
    def validate_info(self) -> None:
        valid = True
        
        current_date_time = datetime.datetime.now()
        
        if not self.name.replace(" ", "").isalpha():
            valid = False
        
        if len(str(self.id_number)) != 9:
            valid = False
        
        if valid:
            print("Student information is valid.")
            print(current_date_time)
        else:
            print("Student information is not valid.")
            print(current_date_time)
            



test_input = input("Testing Student: ").split(' - ')


#split input into three parts
id_number = int(test_input[0])
name = test_input[1]
course = test_input[2]  

#validate input
student = Student(id_number, name, course)
student.validate_info()



