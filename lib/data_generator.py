# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    
    # create generator with major filter
        # similar logic to the filter_students_by_major function, so may be worth importing and referencing that instead
    students_filtered = (
        student for student in student_list
        if student[2].lower() == major.lower()
    )

    return students_filtered
