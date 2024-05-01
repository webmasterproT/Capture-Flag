import os
import hashlib
import random
import string
from exec import execute_dynamic_code

API_KEY = os.getenv('API_KEY')

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def polymorphic_code_generator(code_template, variation_seed):
    """
    Generates polymorphic code based on a template and a seed for variations.
    The code changes slightly on each execution to evade detection.
    """
    # Create a hash of the seed to ensure the variation is not easily predictable
    hash_object = hashlib.sha256(variation_seed.encode())
    hex_dig = hash_object.hexdigest()

    # Modify the code template with the variation seed in a reversible way
    modified_code = code_template.replace('SEED_PLACEHOLDER', hex_dig)

    return modified_code

def execute_polymorphic_code(code):
    """
    Executes the given polymorphic code using the exec() function.
    """
    try:
        # Execute the code snippet dynamically
        execute_dynamic_code(code, API_KEY)
    except Exception as e:
        print(f"An error occurred during code execution: {e}")

def main():
    # Example code template with a placeholder for the seed
    code_template = """
import os
def run(SEED_PLACEHOLDER):
    # Placeholder function that would be modified by the polymorphic generator
    print("Executing polymorphic code with seed:", SEED_PLACEHOLDER)
run('SEED_PLACEHOLDER')
"""

    # Generate a random string to use as a seed for the polymorphic code
    variation_seed = generate_random_string()

    # Generate the polymorphic code
    polymorphic_code = polymorphic_code_generator(code_template, variation_seed)

    # Execute the polymorphic code
    execute_polymorphic_code(polymorphic_code)

if __name__ == "__main__":
    main()