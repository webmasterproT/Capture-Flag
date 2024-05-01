import json
from utils.constants import RISK_ASSESSMENT_MODELS, MITRE_ATTACK, ADVERSARY_KILL_CHAINS
from utils.helpers import calculate_risk_score, load_data_from_json

class RiskAnalysis:
    def __init__(self):
        self.risk_assessment_models = load_data_from_json(RISK_ASSESSMENT_MODELS)
        self.mitre_attack_patterns = load_data_from_json(MITRE_ATTACK)
        self.kill_chains = load_data_from_json(ADVERSARY_KILL_CHAINS)

    def assess_current_risks(self, system_info, detected_threats):
        risk_scores = {}
        for threat in detected_threats:
            risk_scores[threat] = calculate_risk_score(system_info, threat, self.risk_assessment_models)
        return risk_scores

    def evaluate_mitre_attack_patterns(self, system_info):
        attack_pattern_risks = {}
        for pattern in self.mitre_attack_patterns:
            attack_pattern_risks[pattern] = calculate_risk_score(system_info, pattern, self.risk_assessment_models)
        return attack_pattern_risks

    def map_to_kill_chains(self, risks):
        kill_chain_risks = {}
        for risk, score in risks.items():
            for kill_chain in self.kill_chains:
                if risk in kill_chain['risks']:
                    if kill_chain['name'] not in kill_chain_risks:
                        kill_chain_risks[kill_chain['name']] = 0
                    kill_chain_risks[kill_chain['name']] += score
        return kill_chain_risks

    def generate_risk_report(self, system_info, detected_threats):
        risks = self.assess_current_risks(system_info, detected_threats)
        attack_pattern_risks = self.evaluate_mitre_attack_patterns(system_info)
        kill_chain_risks = self.map_to_kill_chains(risks)

        report = {
            'system_info': system_info,
            'detected_threats': detected_threats,
            'risks': risks,
            'attack_pattern_risks': attack_pattern_risks,
            'kill_chain_risks': kill_chain_risks
        }
        return report

    def save_report(self, report, filename='risk_analysis_report.json'):
        with open(filename, 'w') as file:
            json.dump(report, file, indent=4)

def main():
    risk_analyzer = RiskAnalysis()
    # Example system info and detected threats
    system_info = {'os': 'Linux', 'services': ['httpd', 'ssh']}
    detected_threats = ['CVE-2021-1234', 'CVE-2020-5678']

    report = risk_analyzer.generate_risk_report(system_info, detected_threats)
    risk_analyzer.save_report(report)

if __name__ == "__main__":
    main()