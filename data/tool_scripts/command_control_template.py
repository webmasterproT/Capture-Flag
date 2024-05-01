import json
import requests
from utils.constants import API_KEY, COMMAND_CONTROL_SCENARIOS
from utils.helpers import generate_dynamic_code, execute_remote_command

class CommandControlTemplate:
    def __init__(self):
        self.api_key = API_KEY
        self.scenarios = self.load_scenarios()

    def load_scenarios(self):
        with open(COMMAND_CONTROL_SCENARIOS, 'r') as file:
            return json.load(file)

    def select_scenario(self, scenario_id):
        return self.scenarios.get(scenario_id)

    def execute_scenario(self, scenario):
        if scenario['type'] == 'dynamic_code_execution':
            code = generate_dynamic_code(scenario['code_snippet'])
            exec(code)
        elif scenario['type'] == 'remote_command_execution':
            response = execute_remote_command(scenario['target'], scenario['command'])
            return response
        else:
            raise ValueError("Unknown scenario type")

    def report_to_dashboard(self, result):
        # Assuming there's a function to send data to the user's dashboard
        dashboard_endpoint = "http://localhost:8000/dashboard/report"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {'result': result}
        response = requests.post(dashboard_endpoint, headers=headers, json=data)
        return response.json()

    def run(self, scenario_id):
        scenario = self.select_scenario(scenario_id)
        if not scenario:
            raise ValueError("Scenario not found")

        result = self.execute_scenario(scenario)
        report = self.report_to_dashboard(result)
        return report

if __name__ == "__main__":
    command_control = CommandControlTemplate()
    scenario_id = input("Enter the scenario ID to execute: ")
    try:
        execution_report = command_control.run(scenario_id)
        print(f"Execution Report: {execution_report}")
    except Exception as e:
        print(f"An error occurred: {e}")