def angryProfessor(k,a):
    students_on_time =0
    for time in a:
        if time <0:
            students_on_time +=1
    if students_on_time >= k:
        return 'NO'
    else:
        return 'YES'
    
#Testing
print(angryProfessor(3,[-2,-1,0,1,2]))
