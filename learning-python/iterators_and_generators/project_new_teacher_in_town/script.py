from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools

student_roster_iter = iter(student_roster)

# for i in range(10):
#   print(next(student_roster_iter))

student_seats = ClassroomOrganizer()
#print(student_seats.get_combi_list())

science_maths_club = itertools.combinations( \
  itertools.chain(student_seats.get_students_with_subject("Math"), \
                  student_seats.get_students_with_subject("Science")), \
  4)
print(list(science_maths_club))