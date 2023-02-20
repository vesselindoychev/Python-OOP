import unittest

from project.team import Team


class TestTeam(unittest.TestCase):
    name = 'Team'

    def setUp(self) -> None:
        self.team = Team(self.name)

    def test_init(self):
        self.assertEqual(self.name, self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_property(self):
        with self.assertRaises(Exception) as context:
            self.team.name = 'Team1'
            self.team.name = 'Team!@'
        self.assertEqual("Team Name can contain only letters!", str(context.exception))

    def test_add_member(self):
        added_members_by_name = []
        result = self.team.add_member(Ivan=18, Gosho=18)

        self.assertEqual(18, self.team.members['Ivan'])
        self.assertTrue('Ivan' in self.team.members)
        added_members_by_name.append('Ivan')
        added_members_by_name.append('Gosho')
        self.assertEqual(added_members_by_name, ['Ivan', 'Gosho'])
        self.assertEqual(f"Successfully added: {', '.join(added_members_by_name)}", result)

    def test_remove_member__when_he_is_not_added(self):
        result = self.team.remove_member('Ivan')
        self.assertEqual(f"Member with name Ivan does not exist", result)

    def test_remove_member(self):
        self.team.add_member(Ivan=18)
        result = self.team.remove_member('Ivan')

        self.assertFalse('Ivan' in self.team.members)
        self.assertEqual(0, len(self.team.members))
        self.assertEqual(f"Member Ivan removed", result)

    def test_gt_method(self):
        team2 = Team('Loko')
        team2.add_member(Ivan=18)
        self.team.add_member(Gosho=17, Peter=16)

        result = self.team > team2

        self.assertEqual(True, result)
        result = self.team < team2
        self.assertEqual(False, result)

    def test_len_method(self):
        self.team.add_member(Ivan=10, Gosho=21, Peter=19)

        result = Team.__len__(self.team)
        self.assertEqual(3, result)
        self.assertTrue(len(self.team.members) == 3)

    def test_add_method(self):
        team2 = Team('Loko')
        team2.add_member(Ivan=20, Gosho=18, Peter=17)
        self.team.add_member(Vesko=20, Dani=18)

        new_team = self.team + team2

        self.assertEqual({'Ivan': 20, 'Gosho': 18, 'Peter': 17, 'Vesko': 20, 'Dani': 18}, new_team.members)
        self.assertEqual(5, len(new_team.members))
        self.assertEqual('TeamLoko', new_team.name)

    def test_str_method(self):
        self.team.add_member(Ivan=30, Gosho=20)

        actual_msg = str(self.team)
        expected_msg = f'Team name: Team\nMember: Ivan - 30-years old\nMember: Gosho - 20-years old'

        self.assertEqual(expected_msg, actual_msg)


if __name__ == '__main__':
    unittest.main()
