import json
import subprocess
from utils.constants import REVERSE_ENGINEERING_SAMPLES
from utils.helpers import execute_command, load_sample_data

def reverse_engineer_binary(binary_path):
    """
    Reverse engineer the binary at the given path using tools like radare2 or Ghidra.
    """
    # Example using radare2
    command = f"radare2 -c 'aaa; s main; pdf' {binary_path}"
    output = execute_command(command)
    return output

def analyze_binary_for_vulnerabilities(binary_path):
    """
    Analyze the binary for common vulnerabilities using static analysis tools.
    """
    # Example using a static analysis tool like checksec
    command = f"checksec --file={binary_path}"
    output = execute_command(command)
    return output

def decompile_binary_to_c(binary_path):
    """
    Decompile the binary to C code using a decompiler like Ghidra's decompiler.
    """
    # Example using Ghidra's decompiler script
    command = f"ghidra_script -process -script=Decompile.java {binary_path}"
    output = execute_command(command)
    return output

def main():
    # Load the reverse engineering challenge sample data
    samples = load_sample_data(REVERSE_ENGINEERING_SAMPLES)

    # Iterate through the samples and perform reverse engineering
    for sample in samples:
        binary_path = sample['binary_path']
        print(f"Reverse Engineering Binary: {binary_path}")

        # Reverse engineer the binary
        disassembly = reverse_engineer_binary(binary_path)
        print("Disassembly:\n", disassembly)

        # Analyze the binary for vulnerabilities
        vulnerabilities = analyze_binary_for_vulnerabilities(binary_path)
        print("Vulnerabilities:\n", vulnerabilities)

        # Decompile the binary to C code
        decompiled_code = decompile_binary_to_c(binary_path)
        print("Decompiled C Code:\n", decompiled_code)

if __name__ == "__main__":
    main()