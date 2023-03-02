from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    __EXPENSES_PER_RACE = 250_000

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos):
        sponsors_revenue = {
            1: 1_500_000,
            2: 800_000,
            8: 20_000,
            10: 10_000
        }

        revenue = sponsors_revenue[race_pos] - RedBullTeam.__EXPENSES_PER_RACE
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

