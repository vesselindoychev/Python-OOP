import unittest

from demo_project.customer import Student


class TestStudent(unittest.TestCase):
    name = 'Student'

    def setUp(self) -> None:
        self.default_course = 'Python'
        self.default_notes = ['n1', 'n2']
        self.student = Student(self.name, {self.default_course: self.default_notes})

    def test_student_init__with_courses(self):
        self.assertEqual(self.name, self.student.name)
        self.assertEqual({'Python': ['n1', 'n2']}, self.student.courses)

    def test_student_init__without_courses(self):
        student = Student(self.name)
        self.assertEqual(self.name, student.name)
        self.assertEqual({}, student.courses)

    def test_enroll__should_extend_notes_for_already_enrolled_course(self):
        new_notes = ['n3', 'n4']
        expected_notes = self.default_notes + new_notes
        result = self.student.enroll(self.default_course, new_notes)

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertTrue(self.default_course in self.student.courses)
        self.assertEqual(expected_notes, self.student.courses[self.default_course])

    def test_enroll__should_add_new_course_with_notes(self):
        for idx, command in enumerate(['', 'Y']):
            course_name = f'JavaScript{idx}'
            course_notes = ['random', 'Firefox']
            result = self.student.enroll(course_name, course_notes, command)

            self.assertEqual('Course and course notes have been added.', result)
            self.assertTrue(course_name in self.student.courses)
            self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll__should_add_course_without_notes(self):
        course_name = 'JavaScript'
        course_notes = ['random', 'Firefox']
        result = self.student.enroll(course_name, course_notes, 'N')

        self.assertEqual("Course has been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])

    def test_add_notes__should_raise_exception__when_student_is_not_enrolled_for_the_given_course(self):
        course_name = 'JavaScript'

        with self.assertRaises(Exception) as context:
            self.student.add_notes(course_name, ['JS1', 'JS2'])

        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_add_notes__when_student_is_enrolled_for_this_course__expect_to_extend_notes(self):
        notes = ['JS1', 'JS2']

        result = self.student.add_notes(self.default_course, notes)

        self.assertEqual("Notes have been updated", result)
        self.assertTrue(notes in self.student.courses[self.default_course])

    def test_leave_course__when_student_is_enrolled__expect_to_leave_it(self):
        result = self.student.leave_course(self.default_course)

        self.assertEqual("Course has been removed", result)
        self.assertTrue(self.default_course not in self.student.courses)

    def test_leave_course__when_student_is_not_enrolled__expect_to_raise_exception(self):
        course_name = 'JavaScript'

        with self.assertRaises(Exception) as context:
            self.student.leave_course(course_name)

        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))


if __name__ == '__main__':
    unittest.main()
