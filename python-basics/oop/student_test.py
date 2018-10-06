from student import Student
from student import StudentList

import unittest

class TestStudentClass(unittest.TestCase):

    def test_check_student_gpa(self):
        s=Student(1,1,"John","Doe","4.8")
        self.assertEqual(s.getGPA(),"4.8")


if __name__ == '__main__':
    unittest.main()
