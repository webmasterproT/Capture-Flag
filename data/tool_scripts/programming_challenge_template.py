import json
import os
import sys
from utils.helpers import execute_dynamic_code, API_KEY
from utils.constants import PROGRAMMING_CHALLENGES

def load_programming_challenges():
    with open('data/programming_challenges.json') as f:
        return json.load(f)

def save_programming_challenge_results(results):
    with open('data/programming_challenge_results.json', 'w') as f:
        json.dump(results, f, indent=4)

def solve_challenge(challenge):
    try:
        # Dynamic code execution using the exec() function
        exec(challenge['code'])
        return True, "Challenge solved successfully."
    except Exception as e:
        return False, str(e)

def main():
    challenges = load_programming_challenges()
    results = []

    for challenge in challenges:
        success, message = solve_challenge(challenge)
        results.append({
            'challenge_id': challenge['id'],
            'success': success,
            'message': message
        })

    save_programming_challenge_results(results)

    # Notify the dashboard about the completion of challenges
    os.system(f"python dashboard.py --update_challenge_results {API_KEY}")

if __name__ == "__main__":
    main()