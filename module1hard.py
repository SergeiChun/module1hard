grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5],[3,5,5,4,3]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron', 'Никита Чунарев'}
students_list = sorted(list(students))
students_grades = {}
students_grades[students_list[0]] = sum(grades[0])/len((grades[0]))
students_grades[students_list[1]] = sum(grades[1])/len((grades[1]))
students_grades[students_list[2]] = sum(grades[2])/len((grades[2]))
students_grades[students_list[3]] = sum(grades[3])/len((grades[3]))
students_grades[students_list[4]] = sum(grades[4])/len((grades[4]))
students_grades[students_list[5]]= sum(grades[5])/len((grades[5]))
print(students_grades)