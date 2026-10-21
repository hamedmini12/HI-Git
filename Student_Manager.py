from Func import isvalid
from Func import shomenu
students = {
    
}

while True:
    
    number_of_student = input("How many students do you have? (Enter \"v\"(veiw) to see the results): ")
    if number_of_student == "v":
        break
    elif isvalid(number_of_student, r"[1-9]+"):
        
        numbers = 0
        number = 0
        for _ in range(int(number_of_student)):
            
            number += 1
            print(f"student {number} :")
            

            while True:  
                student_name = input("please Enter student name: ")
                if isvalid(student_name, r"[a-zA-Z]+( [a-zA-Z]+)*"):
                    break
                else:
                        print("name is Incorrect","\n")
                
            while True:
                student_last_name = input("please Enter student lastname: ")
                if isvalid(student_last_name, r"[a-zA-Z]+"):
                    break
                else:
                    print("lastname is Incorrect","\n")
                    
            while True:
                student_Math_grade = input("Math grade: ")
                if isvalid(student_Math_grade, r"(?:[1-9]|1[0-9]|20)"):
                    student_Math_grade = int(student_Math_grade)
                    break
                else:
                    print("Error in input data","\n")
                    
            while True:
                student_Literature_grade = input("Literature grade: ")
                if isvalid(student_Literature_grade, r"(?:[1-9]|1[0-9]|20)"):
                    student_Literature_grade = int(student_Literature_grade)
                    break
                else:
                    print("Error in input data","\n")
                    
            while True:
                student_physics_grade = input("Physics grade: ")
                if isvalid(student_physics_grade, r"(?:[1-9]|1[0-9]|20)"):
                    student_physics_grade = int(student_physics_grade)
                    break
                else:
                    print("Error in input data","\n")
                    
            numbers += 1
            Temporary_students = {
                        "name" : student_name,
                        "last name" : student_last_name,
                        "Math grade" : student_Math_grade,
                        "Literature grade" : student_Literature_grade,
                        "Physics grade" : student_physics_grade
                    }
            students.setdefault(numbers, Temporary_students)
            
    else:   
        print("Error in input data","\n")
        
number = 1
for i in range(int(numbers)):
    moadel:list = []   
    moadel.append(students[number].get("Math grade"))
    moadel.append(students[number].get("Literature grade"))
    moadel.append(students[number].get("Physics grade"))
    len_moadel = len(moadel)
    moadel = sum(moadel)
    average = moadel / len_moadel
    students[number].setdefault("moadel", average)
    number += 1
    
number = 1
for i in range(numbers):
    shomenu(students[number])
    number += 1