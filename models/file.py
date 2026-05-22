students = []
with open("students.csv") as file:
    for line in file:
        name, age, city = line.strip().split(",")
        city = city.upper()
        student = {"name": name, "age" : age, "city": city}
        students.append(student)

for student in sorted(students, key= lambda student : (student["city"])):
    print(f"{student['name']} is {student['age']} years old and lives in {student['city']}.")

        

    


    