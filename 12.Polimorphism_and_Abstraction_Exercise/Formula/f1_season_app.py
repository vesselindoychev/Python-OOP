from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None
        self.registered_teams = {}

    def register_team_for_season(self, team_name, budget):
        valid_team_names = ['Red Bull', 'Mercedes']

        if team_name not in valid_team_names:
            raise ValueError('Invalid team name!')

        registered_team = self.__register_team(team_name, budget)
        if team_name not in self.registered_teams:
            self.registered_teams[team_name] = registered_team
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name, red_bull_pos, mercedes_pos):
        teams = ['Red Bull', 'Mercedes']
        for team in teams:
            if team not in self.registered_teams:
                raise Exception('Not all teams have registered for the season.')

        better_pos = self.__find_better_pos(red_bull_pos, mercedes_pos)
        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        result = f"Red Bull: {red_bull_revenue}. Mercedes: {mercedes_revenue}. {better_pos} is ahead at the {race_name} race."
        return result

    def __register_team(self, team_name, budget):
        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)
            return self.red_bull_team
        if team_name == 'Mercedes':
            self.mercedes_team = MercedesTeam(budget)
            return self.red_bull_team

    @staticmethod
    def __find_better_pos(red_bull_pos, mercedes_pos):
        if red_bull_pos > mercedes_pos:
            return 'Mercedes'
        return 'Red Bull'


f1_season = F1SeasonApp()

print(f1_season.register_team_for_season("Red Bull", 2000000))
print(f1_season.register_team_for_season("Mercedes", 2500000))
print(f1_season.new_race_results("Nurburgring", 1, 7))
print(f1_season.new_race_results("Silverstone", 10, 1))
