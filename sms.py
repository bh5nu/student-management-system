def add_student():
    name = input('Enter student name : ')
    roll = (input('Enter student roll no : '))
    marks = (input('Enter student marks : '))
    with open ('sms.txt','r') as file:
        for line in file:
            al_name,al_roll,al_marks = line.strip().split(',')
            if roll == al_roll:
                print('Roll no already exists')
                return

    with open ('sms.txt','a') as file:
        file.write(f'{name},{roll},{marks}\n')
    print('Student Added Successfully')

def view_students():
    with open ('sms.txt','r') as file:
        data = file.readlines()
        if not data:
            print('No Student Founded')
        else:
            for student in data:
                print(student.strip())
        
def search_student():
    search = input('Enter the roll no. to search : ')
    with open ('sms.txt','r') as file:
        for line in file:
            name,roll,marks = line.strip().split(',')
            if roll == search:
                print('Student Founded')
                print(f'Name : {name},Roll no : {roll},Marks : {marks}')
                return
        print('Student not founded')

def delete_student():
    delete = (input('Enter Student name : '))
    data = []
    found = False
    
    with open ('sms.txt','r') as file:
        data = file.readlines()
    
    with open ('sms.txt','w') as file:
        for line in data:
            name,roll,marks = line.strip().split(',')
            if name != delete:
                file.write(line)
            else:
                found = True
    if found:
        print('Student Deleted Successfully')
    else:
        print('Student not founded')

def show_avg():
    total = 0
    count = 0
    with open ('sms.txt','r') as file:
        for line in file:
            name,roll,marks = line.strip().split(',')
            total += int(marks)
            count += 1
    if count>0:
        print('The avg of students is ',total/count)
    else:
        print('No data founded')

def update_marks():
    update = input('Enter the student name for updating marks : ')
    marks2 = input('Marks to be updated : ')
    data = []
    found = False
    with open ('sms.txt','r') as file:
        data = file.readlines()
    with open ('sms.txt','w') as file:
        for line in data:
            name,roll,marks = line.strip().split(',')
            if update == name:
                file.write(f'{name},{roll},{marks2}\n')
                found = True
            else:
                file.write(line)
    if found:
        print('Marks updated Successfully')
    else:
        print('Student not founded')
   
def main():
    while True:        
        print('\n---- Student Management System ----')
        print('1. Add Student')
        print('2. View Students')
        print('3. Search Student')
        print('4. Delete Student')
        print('5. Avg Student marks')
        print('6. Update Student Marks')
        print('7. EXIT')

        a = int(input('Enter the number : '))
        if a==1:
            add_student()
        elif a==2 :
            view_students()
        elif a==3:
            search_student()
        elif a==4:
            delete_student()
        elif a==5:
            show_avg()
        elif a==6:
            update_marks()
        elif a==7:
            break
        else:
            print('Invalid input')


if __name__ == '__main__':
    main()