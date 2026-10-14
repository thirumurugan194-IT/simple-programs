m=input("Enter your name:")
m1 = int(input("Enter marks 1: "))

if m1 < 0 or m1 > 300:
    print("Correct ah number kudu")
else:
    m2 = int(input("Enter marks 2: "))

    if m2 < 0 or m2 > 300:
        print("Correct ah number kudu")
    else:
        total = m1 + m2
        percentage = (total / 600) * 100

        print("Total:", total)
        print("Percentage:", percentage, "%")

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "Fail"

        print("Grade:", grade)
