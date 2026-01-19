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