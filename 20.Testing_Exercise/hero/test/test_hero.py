from demo_project.customer import Hero
import unittest


class TestHero(unittest.TestCase):
    username = 'Hero'
    level = 10
    health = 100
    damage = 30

    def setUp(self) -> None:
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_hero_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_battle_method__when_hero_attacks_himself__expect_exception(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)

        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle_method__when_hero_attacks_with_0_or_less_health__expect_exception(self):
        for health in [0, -25]:
            self.hero = Hero(self.username, self.level, health, self.damage)
            enemy = Hero('Enemy', self.level, self.health, self.damage)

            with self.assertRaises(ValueError) as context:
                self.hero.battle(enemy)

            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle_method__when_enemy_has_0_or_less_health__expect_exception(self):
        for health in [0, -25]:
            # self.hero = Hero(self.username, self.level, self.health, self.damage)
            enemy = Hero('Enemy', self.level, health, self.damage)

            with self.assertRaises(ValueError) as context:
                self.hero.battle(enemy)

            self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(context.exception))

    def test_battle_method__when_both_heroes_die__expect_draw(self):
        # self.hero = Hero(self.username, self.level, self.health, self.damage)
        hero2 = Hero('Hero2', self.level, self.health, self.damage)

        expected_health = self.hero.health - hero2.damage * hero2.level

        result = self.hero.battle(hero2)
        self.assertEqual('Draw', result)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_health, hero2.health)

    def test_battle_method__when_enemy_dies__expect_win(self):

        self.hero = Hero(self.username, self.level, 1000, self.damage)
        enemy = Hero('Enemy', self.level, self.health, self.damage)

        result = self.hero.battle(enemy)
        self.assertEqual('You win', result)
        self.assertEqual(self.level + 1, self.hero.level)
        self.assertEqual(self.hero.health, self.hero.health)
        self.assertEqual(self.damage + 5, self.hero.damage)

    def test_battle_method__when_hero_dies_expect_lose(self):
        enemy = Hero('Enemy', self.level, 1000, self.damage)
        # self.hero = Hero(self.username, self.level, 1000, self.damage)

        result = self.hero.battle(enemy)

        self.assertEqual('You lose', result)
        self.assertEqual(self.level + 1, enemy.level)
        self.assertEqual(enemy.health, enemy.health)
        self.assertEqual(self.damage + 5, enemy.damage)

    def test_str_method__expect_correct_expression(self):
        expected_expression = f"Hero {self.username}: {self.level} lvl\n" \
                              f"Health: {self.health}\n" \
                              f"Damage: {self.damage}\n"

        actual_expression = str(self.hero)

        self.assertEqual(expected_expression, actual_expression)


if __name__ == '__main__':
    unittest.main()
