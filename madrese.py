from re import fullmatch

def isvalid(value: str, pattern: str) -> bool:
    """It takes a value and a pattern,
     and returns `true` if the value matches the pattern.

    Args:
        value (str): can use for names numbers or ...
        pattern (str): Regex pattern (r"[a-zA-Z]+") 

    Returns:
        bool: true | false
    """
    from re import fullmatch

    if fullmatch(pattern, value):
        return True
    else:
        return False

students = {
    
}

while True:
    
    number_of_student = input("How many students do you have? (Enter \"view\" to see the results): ")
    if number_of_student == "view":
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
                    break
                else:
                    print("Error in input data","\n")
                    
            while True:
                student_Literature_grade = input("Literature grade: ")
                if isvalid(student_Literature_grade, r"(?:[1-9]|1[0-9]|20)"):
                    break
                else:
                    print("Error in input data","\n")
                    
            while True:
                student_physics_grade = input("Physics grade: ")
                if isvalid(student_physics_grade, r"(?:[1-9]|1[0-9]|20)"):
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
        