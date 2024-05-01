import os
import sys
import subprocess
import logging
from utils.constants import LOGGING_POLICY

# Initialize logging based on the LOGGING_POLICY
logging.basicConfig(filename=LOGGING_POLICY['filename'],
                    level=LOGGING_POLICY['level'],
                    format=LOGGING_POLICY['format'])

class Debugger:
    def __init__(self):
        self.breakpoints = {}
        self.current_process = None

    def attach(self, pid):
        try:
            self.current_process = subprocess.Popen(['gdb', '--pid', str(pid)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            logging.info(f"Attached to process with PID: {pid}")
        except Exception as e:
            logging.error(f"Failed to attach to process {pid}: {e}")
            sys.exit(1)

    def detach(self):
        if self.current_process:
            self.current_process.communicate('detach\n')
            self.current_process.communicate('quit\n')
            self.current_process = None
            logging.info("Detached from process.")

    def set_breakpoint(self, address):
        if self.current_process:
            self.breakpoints[address] = True
            self.current_process.stdin.write(f"break *{address}\n")
            self.current_process.stdin.flush()
            logging.info(f"Breakpoint set at address: {address}")

    def remove_breakpoint(self, address):
        if self.current_process and address in self.breakpoints:
            self.current_process.stdin.write(f"delete *{address}\n")
            self.current_process.stdin.flush()
            del self.breakpoints[address]
            logging.info(f"Breakpoint removed at address: {address}")

    def continue_execution(self):
        if self.current_process:
            self.current_process.stdin.write('continue\n')
            self.current_process.stdin.flush()
            logging.info("Continued process execution.")

    def read_memory(self, address, length):
        if self.current_process:
            self.current_process.stdin.write(f"x/{length}gx {address}\n")
            self.current_process.stdin.flush()
            output = self.current_process.stdout.readline()
            logging.info(f"Memory read at address {address}: {output}")
            return output

    def write_memory(self, address, value):
        if self.current_process:
            self.current_process.stdin.write(f"set *{address} = {value}\n")
            self.current_process.stdin.flush()
            logging.info(f"Memory written at address {address} with value {value}.")

    def execute_command(self, command):
        if self.current_process:
            self.current_process.stdin.write(f"{command}\n")
            self.current_process.stdin.flush()
            output = self.current_process.stdout.readlines()
            logging.info(f"Executed command '{command}': {output}")
            return output

def main():
    debugger = Debugger()
    # Example usage:
    # debugger.attach(1234)  # Replace 1234 with the actual PID
    # debugger.set_breakpoint('0xdeadbeef')  # Replace with the actual address
    # debugger.continue_execution()
    # debugger.detach()

if __name__ == "__main__":
    main()