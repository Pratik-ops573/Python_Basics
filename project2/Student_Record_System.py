# A simple Student record system...

   
def store():
    n=int(input("Enter the number of students:"))
    

    for i in range(1,n+1):
        name=input("\nEnter the name of the student:")
        print(f"\n------Enter Marks of :{name}--------")
        e=int(input("English:"))
        nep=int(input("Nepali:"))
        m=int(input("Maths:"))
        p=int(input("Physics:"))
        c=int(input("Chemistry:"))
        b=int(input("Biology:"))

        total=e+nep+m+p+c+b
        percentage=(total/450)*100

        output = ""
        division = ""

        if any(x < 35 for x in [p, b, m, c, e, nep]):
            output = "Fail"
            division = "Fail"
        else:
            if(percentage>=80):
                division="Distinction"
                output = "Pass"
            elif(percentage>=60 and percentage<80):
                division="First Division"
                output = "Pass"
            elif(percentage>=40 and percentage<60):
                division="Second Division"
                output = "Pass"
            else:
                division="Third Division"
                output = "Pass"

        
        with open(f"{name}_report.txt", "w") as f:
            f.write(f"\n----- Exam Report Of {name}---------\n")
            f.write(f"English: {e}\n")
            f.write(f"Nepali: {nep}\n")
            f.write(f"Maths: {m}\n")
            f.write(f"Physics: {p}\n")
            f.write(f"Chemistry: {c}\n")
            f.write(f"Biology: {b}\n")
            f.write(f"Total: {total}\n")
            f.write(f"Percentage: {percentage:.2f}%\n")
            f.write(f"Division: {division}\n")
            f.write(f"Result: {output}\n")

            print(f"The file {name}_report.txt is successfully created.")
    
    
def view_report():
        name=input("Enter the name to print report:")

        try:
            with open(f"{name}_report.txt", "r") as f:
                show = f.read()
                print(show)
        except FileNotFoundError:
            print(f"Report for '{name}_txt' does not exist!")

while True:
        print("\n(-------Menu-------)")
        print("1.Update/Add records.\n")
        print("2.View records.\n")
        print("3.Exit.\n")
        n=int(input("Enter choice:"))
        
        if(n==1):
            store()
        elif(n==2):
            view_report()
        elif(n==3):
            print("Program exiting.........")
            break
        else:
            print("Invalid Choice!")
    


