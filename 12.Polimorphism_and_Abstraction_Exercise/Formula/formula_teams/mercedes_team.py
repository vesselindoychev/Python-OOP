from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    __EXPENSES_PER_RACE = 200_000

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        sponsors_revenue = {
            1: 1_000_000,
            3: 500_000,
            5: 100_000,
            7: 50_000
        }

        revenue = sponsors_revenue[race_pos] - MercedesTeam.__EXPENSES_PER_RACE
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"


