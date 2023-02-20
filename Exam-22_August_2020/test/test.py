import unittest

from Exam_10_April_2021.project import StudentReportCard


class StudentReportCardTests(unittest.TestCase):
    student_name = 'Name'
    school_year = 10

    def setUp(self) -> None:
        self.student_report_card = StudentReportCard(self.student_name, self.school_year)

    def test_init__with_empty_grades(self):
        self.assertEqual(self.student_name, self.student_report_card.student_name)
        self.assertEqual(self.school_year, self.student_report_card.school_year)
        self.assertDictEqual({}, self.student_report_card.grades_by_subject)

    def test_student_name__when_it_is_empty_or_white_space__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            self.student_report_card.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))

    def test_student_name__when_it_is_valid(self):
        self.assertEqual(self.student_name, self.student_report_card.student_name)

    def test_school_year__when_it_is_less_than_1_and_bigger_than_12__expect_exception(self):
        for school_year in [0, 13]:
            with self.assertRaises(ValueError) as context:
                self.student_report_card.school_year = school_year
            self.assertEqual("School Year must be between 1 and 12!", str(context.exception))

    def test_school_year__when_it_is_valid(self):
        for school_year2 in [1, 12]:
            self.student_report_card.school_year = school_year2
            self.assertEqual(school_year2, self.student_report_card.school_year)

    def test_add_grade(self):
        subject = 'Math'
        grade = 3

        self.assertEqual(0, len(self.student_report_card.grades_by_subject))

        self.student_report_card.add_grade(subject, grade)
        self.student_report_card.add_grade(subject, 3)
        self.student_report_card.add_grade('Sport', grade)

        self.assertEqual({subject: [grade, grade], 'Sport': [grade]}, self.student_report_card.grades_by_subject)
        self.assertTrue(subject in self.student_report_card.grades_by_subject)
        self.assertTrue('Sport' in self.student_report_card.grades_by_subject)
        self.assertEqual(2, len(self.student_report_card.grades_by_subject))
        self.assertEqual(2, len(self.student_report_card.grades_by_subject[subject]))

    def test_average_grade_by_subject(self):
        subject1 = 'Physics'
        subject2 = 'Chemistry'
        grade1 = 6
        grade2 = 2

        self.student_report_card.add_grade(subject1, grade1)
        self.student_report_card.add_grade(subject1, grade2)
        self.student_report_card.add_grade(subject2, grade1)
        self.student_report_card.add_grade(subject2, grade2)

        self.assertEqual(2, len(self.student_report_card.grades_by_subject))
        self.assertEqual(2, len(self.student_report_card.grades_by_subject[subject1]))
        self.assertEqual(2, len(self.student_report_card.grades_by_subject[subject2]))
        self.assertTrue(subject1 in self.student_report_card.grades_by_subject)
        self.assertTrue(subject2 in self.student_report_card.grades_by_subject)

        average_grade_subject1 = 4
        average_grade_subject2 = 4
        result1 = self.student_report_card.average_grade_by_subject()

        self.assertEqual(f"{subject1}: {average_grade_subject1:.2f}\n{subject2}: {average_grade_subject2:.2f}", result1)

    def test_average_grade_by_all_subjects(self):
        subject1 = 'Sports'
        subject2 = 'Biology'
        grade1 = 3
        grade2 = 5

        self.student_report_card.add_grade(subject1, grade2)
        self.student_report_card.add_grade(subject1, grade1)
        self.student_report_card.add_grade(subject2, grade1)
        self.student_report_card.add_grade(subject2, grade2)

        grades_sum = 16
        count = 4

        result = self.student_report_card.average_grade_for_all_subjects()
        self.assertEqual(f"Average Grade: {grades_sum / count :.2f}", result)

    def test_repr_method(self):
        subject1 = 'Sports'
        subject2 = 'Biology'
        grade1 = 3
        grade2 = 5

        self.student_report_card.add_grade(subject1, grade2)
        self.student_report_card.add_grade(subject1, grade1)
        self.student_report_card.add_grade(subject2, grade1)
        self.student_report_card.add_grade(subject2, grade2)

        grades_sum = 16
        count = 4

        result = self.student_report_card.average_grade_for_all_subjects()
        result2 = self.student_report_card.average_grade_by_subject()

        expected = f"Name: {self.student_name}\n" \
                   f"Year: {self.school_year}\n" \
                   f"----------\n" \
                   f"{result2}\n" \
                   f"----------\n" \
                   f"{result}"
        actual = repr(self.student_report_card)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()