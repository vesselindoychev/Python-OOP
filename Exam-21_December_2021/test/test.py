import unittest

from project.movie import Movie


class TestMovie(unittest.TestCase):
    name = 'Movie'
    year = 2000
    rating = 2

    name2 = 'Movie2'
    year2 = 1998
    rating2 = 10

    def setUp(self) -> None:
        self.movie = Movie(self.name, self.year, self.rating)
        self.movie2 = Movie(self.name2, self.year2, self.rating2)

    def test_init(self):
        self.assertEqual(self.name, self.movie.name)
        self.assertEqual(self.year, self.movie.year)
        self.assertEqual(self.rating, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_property(self):
        with self.assertRaises(ValueError) as context:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(context.exception))

    def test_year_property(self):
        with self.assertRaises(ValueError) as context:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(context.exception))

    def test_add_actor(self):
        actor_name = 'Ivan'

        self.movie.add_actor(actor_name)
        self.assertEqual(['Ivan'], self.movie.actors)

        result = self.movie.add_actor(actor_name)
        self.assertEqual(f"{actor_name} is already added in the list of actors!", result)

    def test_gt_method(self):
        result = ''
        if self.movie2.rating > self.movie.rating:
            result = f'"{self.movie2.name}" is better than "{self.name}"'
        self.assertEqual(f'"{self.movie2.name}" is better than "{self.movie.name}"', result)

