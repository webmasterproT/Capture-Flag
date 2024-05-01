import json
import requests
from utils.constants import API_KEY, USER_PREFERENCES, OPERATIONAL_PARAMETERS
from utils.helpers import generate_polymorphic_code, execute_dynamic_code
from ai_integration import query_ai_for_initial_access_strategy

def initial_access_target_system(target_info):
    """
    Attempt to gain initial access to the target system using AI-driven strategies.
    :param target_info: Dictionary containing information about the target system.
    :return: Boolean indicating success or failure of the initial access attempt.
    """
    # Query the AI for the best initial access strategy
    strategy = query_ai_for_initial_access_strategy(API_KEY, target_info)

    # Generate polymorphic code based on the AI's strategy
    polymorphic_code = generate_polorphic_code(strategy['code_snippet'])

    # Execute the polymorphic code to attempt initial access
    success = execute_dynamic_code(polymorphic_code)

    return success

def main():
    # Load operational parameters and target information
    with open('data/operational_parameters.json') as op_params_file:
        operational_params = json.load(op_params_file)
    
    with open('data/user_defined_goals.json') as user_goals_file:
        user_goals = json.load(user_goals_file)
    
    # Extract target information from user-defined goals
    target_info = user_goals.get('initial_access_target', {})

    # Perform initial access attempt
    access_granted = initial_access_target_system(target_info)

    if access_granted:
        print("Initial access to the target system was successful.")
    else:
        print("Initial access to the target system failed.")

if __name__ == "__main__":
    main()