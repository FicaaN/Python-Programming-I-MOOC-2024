def add_student(database: dict, student: str):

    database[student] = ""
    return database

def print_student(database: dict, student: str):

    default = "no completed courses"
    
    if student in database:
        print(f"{student}:")

        if database[student] == "":
            database[student] = default
            print(" " + str(database[student]))

        else:
            if len(database[student]) > 0:
                average = 0
                print(" " + str(len(database[student])) + " completed courses:") 

                for key, value in database[student]: 
                    print(f"  {key} {value}")
                    average += value
                if average > 0:
                    average = average / len(database[student])
                    print(" average grade", average)
            else:
                print(" "+ default)
    else:
        print(f"{student}: no such person in the database")

def add_course(database: dict, student: str, course: tuple):

    test = []
    list_tuple = []

    if database[student] == "no completed courses" or database[student] == "": 
        database[student] = []

    database[student].append(tuple(course))

    copy = sorted(database[student])[::-1]

    for key, value in database.items():
        if value == "":
            continue
     
    for subject, grade in copy:
        if subject not in test and grade > 0:
            test.append(subject)
            test.append(grade)

    for i in range(len(test) - 1):
        pair = test[i], test[i + 1] 
        if pair not in list_tuple and i % 2 == 0: 
            list_tuple.append(pair)
    
    database[student] = list_tuple

    return database

def summary(database: dict):

    total_sudents = 0
    most_courses_completed = 0
    most_courses_name = ""
    best_average = 0
    best_average_name = ""
    best_average_copy = 0
    best_average_name_copy = ""

    for key,value in database.items():
        total_sudents += 1
        if most_courses_completed < len(value):
            most_courses_completed = len(value)
            most_courses_name = key

        for a, b in value:
            best_average_copy += b
            best_average_name_copy = key
        best_average_copy = best_average_copy / len(value)

        if best_average < best_average_copy:
            best_average = best_average_copy
            best_average_name = best_average_name_copy
        best_average_copy = 0

    print("students", total_sudents)
    print("most courses completed", most_courses_completed, most_courses_name)
    print("best average grade", best_average, best_average_name)

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")

    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Introduction to Programming", 2))

    add_course(students, "Peter", ("Data Structures and Algorithms", 0))

    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Peter")
    summary(students)