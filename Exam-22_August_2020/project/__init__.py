from Exam_10_April_2021.project import Everland
from Exam_10_April_2021.project import Child
from Exam_10_April_2021.project import YoungCouple
from Exam_10_April_2021.project import YoungCoupleWithChildren

everland = Everland()


def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)

    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()
