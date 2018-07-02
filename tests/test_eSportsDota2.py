import os
import unittest
from sportradar import eSportsDota2

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_ESPORTSDOTA2"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = eSportsDota2.eSportsDota2(api_key, format_="json", timeout=5, sleep_time=1.5)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("eSportsDota2"))
        cls.auth = api_key
        cls.api = api
        cls.sport = "dota2"
        cls.language_code = "en"
        cls.year = 2018
        cls.month = 6
        cls.day = 1
        cls.team_id_1 = "sr:competitor:247431"
        cls.team_id_2 = "sr:competitor:242738"
        cls.match_id = "sr:match:12206428"
        cls.player_id = "sr:player:971065"
        cls.team_id = "sr:competitor:247431"
        cls.tournament_id = "sr:tournament:14029"

    def test_get_dailyresults(self):
        """Test the daily results GET query"""
        msg = "Response status is not 200"
        response = self.api.get_dailyresults(self.sport, self.language_code, self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_dailyschedule(self):
        """Test the daily schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_dailyschedule(self.sport, self.language_code, self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_deletedmatches(self):
        """Test the deleted matches GET query"""
        msg = "Response status is not 200"
        response = self.api.get_deletedmatches(self.sport, self.language_code)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_head_2_head(self):
        """Test the head-2-head GET query"""
        msg = "Response status is not 200"
        response = self.api.get_head_2_head(self.sport, self.language_code, self.team_id_1, self.team_id_2)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_matchlineups(self):
        """Test the match lineups GET query"""
        msg = "Response status is not 200"
        response = self.api.get_matchlineups(self.sport, self.language_code, self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_matchprobabilities(self):
        """Test the match probabilities GET query"""
        msg = "Response status is not 200"
        response = self.api.get_matchprobabilities(self.sport, self.language_code, self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_matchsummary(self):
        """Test the match summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_matchsummary(self.sport, self.language_code, self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_playerprofile(self):
        """Test the player profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_playerprofile(self.sport, self.language_code, self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_teamprofile(self):
        """Test the team profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_teamprofile(self.sport, self.language_code, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_teamresults(self):
        """Test the team results GET query"""
        msg = "Response status is not 200"
        response = self.api.get_teamresults(self.sport, self.language_code, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_teamschedule(self):
        """Test the team schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_teamschedule(self.sport, self.language_code, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentinfo(self):
        """Test the tournament info GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentinfo(self.sport, self.language_code, self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentlivesummary(self):
        """Test the tournament live summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentlivesummary(self.sport, self.language_code)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentresults(self):
        """Test the tournament results GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentresults(self.sport, self.language_code, self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentschedule(self):
        """Test the tournament schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentschedule(self.sport, self.language_code, self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentseasons(self):
        """Test the tournament seasons GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentseasons(self.sport, self.language_code, self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_tournamentstandings(self):
    #     """Test the tournament standings GET query"""
    #     msg = "Response status is not 200"
    #     response = self.api.get_tournamentstandings(self.sport, self.language_code, self.tournament_id)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentsummary(self):
        """Test the tournament summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentsummary(self.sport, self.language_code, self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournaments(self):
        """Test the tournaments GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournaments(self.sport, self.language_code)
        self.assertEqual(response.status_code, 200, msg)