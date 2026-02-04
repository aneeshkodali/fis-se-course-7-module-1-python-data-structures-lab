# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    
    # use set comprehension to get unique majors
        # major is 3rd (python 2nd) element
    unique_majors = {
        student[2] for student in student_list
    }

    return unique_majors
