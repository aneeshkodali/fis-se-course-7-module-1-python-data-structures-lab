# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
    
    # filter list
        # student major is 3rd (python 2nd) element
        # compare lower case just in case the casing of student major and user input does not match
    filtered_list = [
        student for student in student_list
        if student[2].lower() == major.lower()
    ]

    return filtered_list
