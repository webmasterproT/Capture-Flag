```python
import os
import subprocess
from utils.constants import REVERSE_ENGINEERING_SAMPLES
from utils.helpers import load_json_data, save_json_data

class ReverseEngineeringTool:
    def __init__(self):
        self.samples = load_json_data(REVERSE_ENGINEERING_SAMPLES)

    def analyze_binary(self, binary_path):
        """
        Analyze a binary executable to understand its behavior.
        """
        # Placeholder for binary analysis logic
        # This could involve disassemblers, decompilers, and other reverse engineering tools
        analysis_result = subprocess.run(["radare2", "-A", binary_path], capture_output=True, text=True)
        return analysis_result.stdout

    def decompile_binary(self, binary_path, output_path=None):
        """
        Decompile a binary to high-level code to understand its structure and logic.
        """
        if output_path is None:
            output_path = os.path.splitext(binary_path)[0] + ".c"
        # Placeholder for decompilation logic
        # This could involve tools like Ghidra, IDA Pro, or Binary Ninja
        decompilation_result = subprocess.run(["ghidra", "-decompile", binary_path, "-o", output_path], capture_output=True, text=True)
        return decompilation_result.stdout

    def debug_binary(self, binary_path):
        """
        Debug a binary to step through its execution and analyze its behavior.
        """
        # Placeholder for debugging logic
        # This could involve debuggers like GDB or WinDbg
        debug_result = subprocess.run(["gdb", binary_path], capture_output=True, text=True)
        return debug_result.stdout

    def save_sample(self, sample_data):
        """
        Save a new reverse engineering sample to the database.
        """
        self.samples.append(sample_data)
        save_json_data(REVERSE_ENGINEERING_SAMPLES, self.samples)

    def get_sample(self, sample_id):
        """
        Retrieve a reverse engineering sample by its ID.
        """
        return next((sample for sample in self.samples if sample['id'] == sample_id), None)

# Example usage
if __name__ == "__main__":
    re_tool = ReverseEngineeringTool()
    binary_analysis = re_tool.analyze_binary("/path/to/binary")
    print("Binary Analysis Result:", binary_analysis)

    decompiled_code = re_tool.decompile_binary("/path/to/binary")
    print("Decompiled Code:", decompiled_code)

    debug_output = re_tool.debug_binary("/path/to/binary")
    print("Debug Output:", debug_output)

    # Save a new sample
    new_sample = {
        "id": "sample123",
        "name": "Example Binary",
        "description": "An example binary for reverse engineering",
        "path": "/path/to/binary"
    }
    re_tool.save_sample(new_sample)

    # Retrieve a sample
    retrieved_sample = re_tool.get_sample("sample123")
    print("Retrieved Sample:", retrieved_sample)
```

Please note that the actual implementation of binary analysis, decompilation, and debugging would require the respective tools to be installed and properly configured on the system where this script is executed. The subprocess calls to tools like `radare2`, `ghidra`, and `gdb` are placeholders and should be replaced with actual calls to these tools, including the correct command-line arguments for each tool. The `load_json_data` and `save_json_data` functions are assumed to be utility functions for handling JSON file operations, which should be implemented in the `utils/helpers.py` file.