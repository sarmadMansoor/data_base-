def isPresentInDataBase(rollNumber):
    with open ("student.txt" ,'r') as file:
        lines =file.readlines()
        status =False
        for element in lines:
            if (isRollNumberFound(element,rollNumber)):
                status= True
            
        return status
def addRecord():
    rollNumber=input("Enter the Roll number: ")
    while (isPresentInDataBase(rollNumber)):
        rollNumber=input("Given roll number is already found in data base !!!\nEnter the Roll number  again: ")
    name =input("Enter the name : ")
    fatherName =input("Enter your Father name : ")
    cnic=input("Enter your CNIC :  ")
    dateOfBirth=input("Enter your date of birth : ")
    section =input("Enter your section : ")
    CGPA =input("Enter your CGPA :  ")
    with open ("student.txt" ,'a') as file:
        file.write(rollNumber+','+name+','+fatherName+','+cnic+','+dateOfBirth+','+section+','+CGPA+'\n')


def display():
    count =1
    with open ("student.txt" ,'r') as file:
        lines =file.readlines()
        for element in lines:
            record=element.split(',')
            print("\n\t\tStudent number ",count)
            print ("\n")
            print ("Roll Number : ",record[0])
            print ("Name  : ",record[1])
            print ("Father name  : ",record[2])
            print ("CNIC  : ",record[3])
            print ("Date Of Birth  : ",record[4])
            print ("Section : ",record[5])
            print ("cgpa : ",record[6])
            count+=1



def isRollNumberFound(arr,rollNumber):
    record =arr.split(',')
    if (record[0]==rollNumber):
        return True
    return False

def update():
    rollNumber=input ("Enter the roll number which you want to update : ")
    with open ("student.txt" ,mode='r') as file:
        data=file.readlines()
    
    with open ("student.txt" ,mode='w') as file:
        for element in data:
            if (isRollNumberFound(element,rollNumber)):
                name =input("Enter the name : ")
                fatherName =input("Enter your Father name : ")
                cnic=input("Enter your CNIC :  ")
                dateOfBirth=input("Enter your date of birth : ")
                section =input("Enter your section : ")
                CGPA =input("Enter your CGPA :  ")
                file.write(rollNumber+','+name+','+fatherName+','+cnic+','+dateOfBirth+','+section+','+CGPA+'\n')
            else:
                file.write(element)




def delete():
    rollNumber=input ("Enter the roll number which you want to delete : ")
    with open ("student.txt" ,mode='r') as file:
        data=file.readlines()
    
    with open ("student.txt" ,mode='w') as file:
        for element in data:
            if (not(isRollNumberFound(element,rollNumber))):
                file.write(element)

def displayMain():
    print("Choose from the following:")
    print("1: Add a new Student record")
    print("2: Display all Student record")
    print("3: Update a Student record")
    print("4: Delete a Student record")
    print("5: Exit")

def main():
    status =True
    while (status):
        displayMain()
        result = int (input())
       
        if (result==1):
            addRecord()
        elif(result==2):
            display()
        elif(result==3):
            update()
        elif(result==4):
            delete()
        else:
            status =False

main()