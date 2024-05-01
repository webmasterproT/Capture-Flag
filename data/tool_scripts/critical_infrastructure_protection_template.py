```python
import json
from utils.constants import CRITICAL_INFRASTRUCTURE_PROTECTION_PLANS
from utils.helpers import load_data, save_data
from ai_integration import analyze_threats, recommend_protection_measures

class CriticalInfrastructureProtection:
    def __init__(self):
        self.protection_plans = load_data(CRITICAL_INFRASTRUCTURE_PROTECTION_PLANS)

    def update_protection_plan(self, infrastructure_id, new_plan):
        self.protection_plans[infrastructure_id] = new_plan
        save_data(CRITICAL_INFRASTRUCTURE_PROTECTION_PLANS, self.protection_plans)

    def analyze_and_protect(self, infrastructure_data):
        threats = analyze_threats(infrastructure_data)
        for threat in threats:
            protection_measures = recommend_protection_measures(threat)
            self.apply_protection_measures(infrastructure_data['id'], protection_measures)

    def apply_protection_measures(self, infrastructure_id, protection_measures):
        if infrastructure_id in self.protection_plans:
            self.protection_plans[infrastructure_id].update(protection_measures)
        else:
            self.protection_plans[infrastructure_id] = protection_measures
        save_data(CRITICAL_INFRASTRUCTURE_PROTECTION_PLANS, self.protection_plans)

    def get_protection_plan(self, infrastructure_id):
        return self.protection_plans.get(infrastructure_id, "No plan found for the given ID.")

if __name__ == "__main__":
    cip = CriticalInfrastructureProtection()
    # Example usage:
    # Load infrastructure data from an external source or user input
    infrastructure_data = {
        'id': 'power_grid_01',
        'type': 'Power Grid',
        'location': 'Sector 7G',
        'vulnerabilities': ['unpatched_software', 'legacy_hardware'],
        'current_protections': ['firewall', 'intrusion_detection_system']
    }
    cip.analyze_and_protect(infrastructure_data)
    print(cip.get_protection_plan('power_grid_01'))
```