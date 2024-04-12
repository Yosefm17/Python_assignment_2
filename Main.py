import os as o
def delete():
    with open("student_db.txt", 'w'):
        pass
def clear_screen():
    o.system('cls' if o.name == 'nt' else 'clear')


def register_student():
    try:
        while True:
            id_exist = False
            full_name = input("Enter student's full name: ")
            gender = input("Enter student's gender: ")
            student_id = input("Enter student's ID: ")
            department = input("Enter student's department: ")
            cgpa = float(input("Enter the CGPA of the student: "))
            

            with open("student_db.txt", "r") as file:
                for line in file:
                    _, st_id, _, _, _ = line.split(',')
                    if line and st_id:
                        if st_id == student_id:
                            id_exist = True
                            break

            if id_exist:
                print("This ID already exists")
                return

            with open('student_db.txt', 'a') as file:
                file.write(f"{full_name},{student_id},{gender},{department},{cgpa}\n")
                print("Student registered successfully")

            register_more = input("Do you want to register more students? (y for yes /any other key for no): ")
            if register_more.lower() != 'y':
                break

    except ValueError as e:
        print("Please enter valid information", e)
    except FileNotFoundError:
        print("Something went wrong loading the students database")


def student_search():
    try:
        while True:
            id_test = False
            no_students = True
            st_id = input("Enter the ID of the student you want to search for: ")
            

            with open('student_db.txt', 'r') as f:
                for line in f:
                    no_students = False
                    _, s_id, _, _, _ = line.split(',')
                    if line and s_id:
                        if st_id == s_id:
                            id_test = True
                            st_name, st_id, st_gender, st_department, st_gpa = line.split(',')
                            print(f"Name: {st_name} \n ID: {st_id} \n Gender: {st_gender} \n Department: {st_department} \n CGPA: {st_gpa}")
                            break

                if not id_test:
                    print("Student not found")

            if no_students:
                print("It seems there are no students registered yet")

            search_more = input("Do you want to search for more students? (y for yes /any other key for no): ")
            if search_more.lower() != 'y':
                break

    except ValueError:
        print("Please enter a valid ID")
    except FileNotFoundError:
        print("Something went wrong loading the students database")
    except IndexError:
        print("It seems there are no students registered yet")
    except Exception:
        print("Something went wrong or there are no students registered yet")


def update_student_name():
    try:
        while True:
            st_name_update_id = input("Enter the ID of the student you want to update the name for: ")
            
            found = False
            line_with_no_new_line = []
            st_record = []
            no_students = True

            with open('student_db.txt', 'r') as R:
                for line in R:
                    st_record.append(line)

                for line in st_record:
                    line_with_no_new_line.append(line.strip())

                reserved_list = [[st_info] for st_info in line_with_no_new_line]

                for st_info in reserved_list:
                    for s_info in st_info:
                        if s_info.split(',')[1] == st_name_update_id:
                            mod_name, s_id, s_gend, s_dept, s_cgpa = s_info.split(',')
                            st_name_update = input("Enter the new name: ")
                            mod_name = st_name_update.strip()
                            s_info = f"{mod_name},{s_id.strip()},{s_gend.strip()},{s_dept.strip()},{s_cgpa.strip()}"

                            reserved_list[reserved_list.index(st_info)] = [s_info]
                            found = True
                            break

                if found:
                    with open('student_db.txt', 'w') as file:
                        for st_info in reserved_list:
                            for stud_info in st_info:
                                name, id, gender, dept, gpa = stud_info.split(',')
                                file.write(f"{name},{id},{gender},{dept},{gpa}\n")
                        print("Name changed successfully.")
                else:
                    print("Student not found.")

            if no_students:
                print("It seems there are no students registered yet.")
            update_more = input("Do you want to update more students? (y for yes /any other key for no): ")
            if update_more.lower() != 'y':
                break

    except ValueError as e:
        print("Please enter a valid ID.", e)
    except FileNotFoundError:
        print("Something went wrong loading the student database")
    except IndexError as e:
        print("It seems there are no students registered yet.", e)
    except Exception as e:
        print("Something went wrong or there are no students registered yet.", e)


def update_student_gpa():
    try:
        while True:
            st_gpa_update_id = input("Enter the ID of the student you want to update their GPA: ")
            
            found = False
            line_with_no_new_line = []
            st_record = []
            no_students = True

            with open('student_db.txt', 'r') as R:
                for line in R:
                    st_record.append(line)
                    no_students = False

                for line in st_record:
                    line_with_no_new_line.append(line.strip())

                reserved_list = [[st_info] for st_info in line_with_no_new_line]

                for st_info in reserved_list:
                    for s_info in st_info:
                        if s_info.split(',')[1] == st_gpa_update_id:
                            name, s_id, s_gend, s_dept, mod_cgpa = s_info.split(',')
                            st_gpa_update = float(input("Enter the new CGPA: "))
                            mod_cgpa = st_gpa_update
                            s_info = f"{name},{s_id},{s_gend},{s_dept},{str(mod_cgpa)}"
                            reserved_list[reserved_list.index(st_info)] = [s_info]

                            found = True
                            break

                if found:
                    with open('student_db.txt', 'w') as file:
                        for st_info in reserved_list:
                            for stud_info in st_info:
                                file.write(f"{stud_info}\n")
                    print("GPA changed successfully.")
                else:
                    print("Student not found.")

            if no_students:
                print("It seems there are no students registered yet.")
            update_more = input("Do you want to update more students gpa? (y for yes /any other key for no): ")
            if update_more.lower() != 'y':
                break

    except ValueError:
        print("Please enter a valid ID")
    except FileNotFoundError:
        print("Something went wrong loading the students database")
    except IndexError:
        print("It seems there are no students registered yet")


def delete_student():
    try:
        while True:
            st_record_update = []
            no_students = True
            found = False

            st_delete_id = input("Enter the ID of the student you want to delete: ")
            

            with open('student_db.txt', 'r') as F:
                for line in F:
                    no_students = False
                    if line and line.split(',')[1] == st_delete_id:
                        found = True
                        F.seek(0)
                        for line in F:
                            if line.split(',')[1] != st_delete_id:
                                st_record_update.append(line.strip())

                        break

            if found:
                with open('student_db.txt', 'w') as file:
                    for line in st_record_update:
                        file.write(f"{line}\n")
                print("Student deleted successfully!")

            else:
                print("Student not found.")

            if no_students:
                print("It seems there are no students registered yet.")
            delete_more = input("Do you want to delete more students? (y for yes /any other key for no): ")
            if delete_more.lower() != 'y':
                break

    except ValueError:
        print("Please enter a valid ID")
    except FileNotFoundError:
        print("Something went wrong loading the students database")
    except IndexError:
        print("It seems there are no students registered yet")


def count_students():
    try:
        total_number_students = []
        no_students = True

        with open('student_db.txt', 'r') as F:
            for line in F:
                no_students = False
                if line and line.split(',')[0]:
                    total_number_students.append(line.split(',')[0])

        total_students = len(total_number_students)
        if no_students:
            print("It seems there are no students registered yet")
        else:
            print("Student names:")
            for name in total_number_students:
                print(name)
            print("Total number of students:", total_students)

    except FileNotFoundError:
        print("Something went wrong loading the students database")
    except IndexError:
        print("It seems there are no students registered yet")
    except Exception:
        print("Something went wrong. Please try again.")


def count_gender():
    try:
        male_count = 0
        female_count = 0
        no_students = True

        with open('student_db.txt', 'r') as F:
            for line in F:
                no_students = False
                if line and line.split(',')[2]:
                    if line.split(',')[2].lower() == 'm' or line.split(',')[2].lower() == 'male':
                        male_count += 1
                    else:
                        female_count += 1

        if no_students:
            print("It seems there are no students registered yet")
        else:
            print("Total number of males and females in the student:")
            print("Number of males:", male_count)
            print("Number of females:", female_count)

    except FileNotFoundError:
        print("Something went wrong loading the students database")
    except IndexError:
        print("It seems there are no students registered yet")
    except Exception:
        print("Something went wrong or there are no students registered yet")


def top_scorer_department():
    try:
        top_scorer_students = {}
        no_students = True

        with open('student_db.txt', 'r') as F:
            for line in F:
                no_students = False
                if line and line.split(',')[0]:
                    name, id, gender, dept, gpa = line.split(',')
                    if dept not in top_scorer_students or float(gpa) > top_scorer_students[dept][3]:
                        top_scorer_students[dept] = ([name], id, gender, float(gpa))
                    elif float(gpa) == top_scorer_students[dept][3]:
                        top_scorer_students[dept][0].append(name)

        for department, (names, _, _, cgpa) in top_scorer_students.items():
            print(f"Top scored student in {department} department, with GPA {cgpa} is/are:")
            for name in names:
                print(name)

        if no_students:
            print("It seems there are no students registered yet")

    except FileNotFoundError:
        print("Something went wrong loading the students database")
    except KeyError:
        print("It seems there are no students registered yet")
    except IndexError:
        print("It seems there are no students registered yet")
    except Exception:
        print("Something went wrong or there are no students registered yet")


def top_female_scorer_department():
    try:
        female_students = []
        f_students = {}
        max_female = {}
        no_students = True

        with open('student_db.txt', 'r') as F:
            for line in F:
                no_students = False
                if line and line.split(',')[0]:
                    name, id, sex, dept, gpa = line.split(',')
                    if sex.lower().strip() == 'f' or sex.lower().strip() == 'female':
                        female_students.append((id, dept, name, gpa))

        for female in female_students:
            s_id, s_dpt, s_name, s_gpa = female
            f_students[s_id] = (s_name, s_gpa, s_dpt)

        for _, s_info in f_students.items():
            st_name, s_cgpa, s_dp = s_info
            if s_dp not in max_female or s_cgpa > max_female[s_dp][1]:
                max_female[s_dp] = ([st_name], s_cgpa)
            elif s_cgpa == max_female[s_dp][1]:
                max_female[s_dp][0].append(st_name)

        for s_dpt, st_info in max_female.items():
            stud_names, stud_cgp = st_info
            print(f"Top scored female students in {s_dpt}, with CGPA: {stud_cgp}")
            for name in stud_names:
                print(name)

        if no_students or max_female == {}:
            print("It seems there are no students registered yet or there are no girls in the students database")

    except FileNotFoundError:
        print("Something went wrong loading the students database")
    except KeyError:
        print("It seems there are no students registered yet")
    except IndexError:
        print("It seems there are no students registered yet")
    except Exception:
        print("Something went wrong or there are no students registered yet")


def gpa_threshold():
    try:
        student_gpa_threshold = []
        no_students = True
        gpa = float(input("Enter the GPA you want to see students who scored greater than: "))
        

        with open('student_db.txt', 'r') as F:
            for line in F:
                no_students = False
                if line and line.split(',')[0]:
                    if gpa < float(line.split(',')[4]):
                        student_gpa_threshold.append(line.split(',')[0])

        if student_gpa_threshold == []:
            print("There are no students who scored GPA greater than:", gpa)
        else:
            print("Students who scored greater than", gpa, ":")
            for student in student_gpa_threshold:
                print(student)
        if no_students:
            print("It seems there are no students registered yet")
            return

    except ValueError:
        print("Please enter a valid GPA gpa should be only numeric value:")
    except FileNotFoundError:
        print("Something went wrong loading the students database")
    except IndexError:
        print("It seems there are no students registered yet")
    except Exception:
        print("Something went wrong or there are no students registered yet")


def frequent_names():
    try:
        stud_data = {}
        freq_names = {}
        list_of_freq_names = []
        no_students = True

        with open('student_db.txt', 'r') as F:
            for line in F:
                no_students = False
                if line and line.split(',')[0]:
                    stud_data[line.split(',')[1]] = (line.split(",")[0])

        for _, name in stud_data.items():
            freq_names[name.split()[0]] = freq_names.get(name.split()[0], 0) + 1

        for name_key, name_freq in freq_names.items():
            if name_freq >= 2:
                list_of_freq_names.append(name_key)

        if list_of_freq_names == []:
            print("Every name is unique")
        else:
            print("frequent names in the students list:")
            for name in list_of_freq_names:
                print(name)

        if no_students:
            print("It seems there are no students registered yet")

    except FileNotFoundError:
        print("Something went wrong loading the students database")
    except IndexError:
        print("It seems there are no students registered yet")
    except KeyError:
        print("It seems there are no students registered yet")
    except Exception:
        print("Something went wrong or there are no students registered yet")


def students_per_department():
    try:
        no_students = True
        total_students = []
        total_students_sorted_id = {}
        students_per_dp = {}

        with open('student_db.txt', 'r') as F:
            for line in F:
                no_students = False
                if line and line.split(',')[0]:
                    name, id, _, dept, _ = line.split(',')
                    total_students.append((name, id, dept))

        for st_info in total_students:
            st_name, st_id, st_dept = st_info
            total_students_sorted_id[st_id] = (st_name, st_dept)

        for _, s_info in total_students_sorted_id.items():
            stud_name, stud_dept = s_info
            if stud_dept not in students_per_dp:
                students_per_dp[stud_dept] = [stud_name]
            else:
                students_per_dp[stud_dept].append(stud_name)

        no_of_students_per_dp = {dp: len(no_of_st_per_dp) for dp, no_of_st_per_dp in students_per_dp.items()}
        print("Students Per Department:")

        for dpt, no_st in no_of_students_per_dp.items():
            print(dpt, ":", no_st)

        if no_students:
            print("It seems there are no students registered yet")

    except FileNotFoundError:
        print("Something went wrong loading the students database")
    except IndexError:
        print("It seems there are no students registered yet")
    except KeyError:
        print("It seems there are no students registered yet")
    except Exception:
        print("Something went wrong or there are no students registered yet")

def menu():
    while True:
        
        try:
           
            print("\nSelect Your Choice!")
            print("0. Register A New Student")
            print("1. Search For Student")
            print("2. Update Student Name")
            print("3. Update Student GPA")
            print("4. Delete Student by ID")
            print("5. Count And Display Total Number Of The Students")
            print("6. Count Total Number Of Males And Females In The Students")
            print("7. Display Name And Department Of Top Scored Student for each Department")
            print("8. Display Name And Department Of Top Scored Female Student For Each Department")
            print("9. List Names Of The Students Who Scored Given GPA")
            print("10. Show Frequent Student Names")
            print("11. Show Total Number Of Students In Each Department")
            print("12. Exit")
            print("if you want to delete the whole record press 13!")
            

            opt = int(input("Enter Your Choice: "))
            clear_screen()

            if opt == 0:
                register_student()
            elif opt == 1:
                
                student_search()
            elif opt == 2:
                
                update_student_name()
            elif opt == 3:
                
                update_student_gpa()
            elif opt == 4:
                
                delete_student()
            elif opt == 5:
                
                count_students()
            elif opt == 6:
                
                count_gender()
            elif opt == 7:
                
                top_scorer_department()
            elif opt == 8:
                
                top_female_scorer_department()
            elif opt == 9:
                
                gpa_threshold()
            elif opt == 10:
                
                frequent_names()
            elif opt == 11:
                
                students_per_department()
            elif opt == 12:
                print("Thank you for using our system")
                break
            elif opt == 13:
                delete()
            else:
                print("Please choose a valid option:")
                
        except ValueError:
            print("Please insert a valid input:")

   


def main():
    print("Welcome to Student Management System")
    while True:
        print("1. Main Menu")
        print("2. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            clear_screen()
            menu()
            
        elif choice == 2:
            print("Thank you for using our system")
            break
        else:
            print("Please choose a valid option:")
    
    

if __name__ == "__main__":
    main()
