def get_students_who_took_prog1_and_prog2(prog1, prog2):
    return (prog1 & prog2)

def get_students_who_took_prog1_or_prog2(prog1, prog2):
    return (prog1 | prog2)

def get_students_who_took_prog1_not_prog_2(prog1, prog2):
    return(prog1 - prog2)

def get_students_who_took_prog2_not_prog_1(prog1, prog2):
    return(prog2 - prog1)

prog1Set = {'Student1', 'Student2', 'Student3'}
prog2Set = {'Student3', 'Student4', 'Student5'}
