def grade(m1,m2,m3):
    avg=(m1+m2+m3)/3
    if avg>=75:
        grade='A'
    elif avg>=60:
        grade='B'
    elif avg>=50:
        grade='C'
    else:
        grade='F'
    return avg,grade
m1=int(input("Enter marks for maths: "))
m2=int(input("Enter marks for english: "))
m3=int(input("Enter marks for science 3: "))