import datetime
import json

from constants import RESULTS_PATH


class ResultsDAO:

    def save_result(self, username: str, points: int) -> None:
        try:
            with open(RESULTS_PATH) as file:
                results = json.load(file)
        except FileNotFoundError:
            results = []

        new_result = {
            'username': username,
            'points': points,
            'date': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        }
        results.append(new_result)

        with open(RESULTS_PATH, 'w', ) as file:
            json.dump(results, file, ensure_ascii=False)

    def get_results(self) -> list:
        try:
            with open(RESULTS_PATH) as file:
                results = json.load(file)
        except FileNotFoundError:
            results = []

        results.sort(key=lambda x: x['points'], reverse=True)

        return results
