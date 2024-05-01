```python
import os
import sys
import subprocess
from utils.constants import DEBUGGING_SCENARIOS

class DebuggingTool:
    def __init__(self, api_key):
        self.api_key = api_key

    def load_debugging_scenario(self, scenario_id):
        scenario = DEBUGGING_SCENARIOS.get(scenario_id)
        if not scenario:
            print(f"No scenario found with ID: {scenario_id}")
            return None
        return scenario

    def start_debugging_session(self, scenario):
        executable_path = scenario.get('executable_path')
        if not os.path.isfile(executable_path):
            print(f"Executable not found at path: {executable_path}")
            return

        # Start the debugging process
        process = subprocess.Popen(['gdb', executable_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
        return process

    def execute_debugger_command(self, process, command):
        process.stdin.write(command + '\n')
        process.stdin.flush()
        output, error = process.communicate()
        return output, error

    def interactive_debugging(self, process):
        try:
            while True:
                command = input("Enter debugger command: ")
                if command.lower() == 'exit':
                    break
                output, error = self.execute_debugger_command(process, command)
                print(output)
                if error:
                    print(f"Error: {error}", file=sys.stderr)
        finally:
            process.terminate()

    def run(self, scenario_id):
        scenario = self.load_debugging_scenario(scenario_id)
        if scenario:
            process = self.start_debugging_session(scenario)
            if process:
                self.interactive_debugging(process)

if __name__ == "__main__":
    api_key = os.getenv('API_KEY')
    if not api_key:
        print("API_KEY is not set.")
        sys.exit(1)

    debugging_tool = DebuggingTool(api_key)
    scenario_id = input("Enter the ID of the debugging scenario you want to run: ")
    debugging_tool.run(scenario_id)
```

This Python script represents a basic template for a debugging tool that can be used to interact with a debugger like GDB. It includes functionality to load predefined debugging scenarios, start a debugging session, execute debugger commands, and run an interactive debugging session. The script uses constants from a shared dependency file `utils/constants.py` which is expected to contain debugging scenarios and other configurations. The `API_KEY` is used to authenticate with any necessary services and is expected to be set in the environment.