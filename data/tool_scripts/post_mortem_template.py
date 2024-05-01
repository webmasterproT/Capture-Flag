import json
from datetime import datetime

def generate_post_mortem_report(incident_details, analysis_results, recommendations):
    """
    Generate a post-mortem report based on the incident details, analysis results,
    and recommendations provided by the AI and other analysis tools.

    :param incident_details: Dictionary containing details about the incident.
    :param analysis_results: Dictionary containing the results of the analysis.
    :param recommendations: List of recommendations for future prevention and improvements.
    :return: A string containing the formatted post-mortem report.
    """
    report = {
        "report_id": incident_details.get("report_id", "N/A"),
        "incident_date": incident_details.get("incident_date", str(datetime.now())),
        "incident_description": incident_details.get("description", "No description provided."),
        "impact_assessment": incident_details.get("impact", "Impact not assessed."),
        "analysis_results": analysis_results,
        "recommendations": recommendations,
        "generated_on": str(datetime.now())
    }

    # Save the report to a JSON file
    report_filename = f"post_mortem_report_{report['report_id']}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    with open(report_filename, 'w') as report_file:
        json.dump(report, report_file, indent=4)

    return report_filename

# Example usage:
if __name__ == "__main__":
    incident = {
        "report_id": "PM123456",
        "incident_date": "2023-04-01T14:30:00",
        "description": "Unauthorized access to the internal network detected.",
        "impact": "Sensitive data potentially exposed."
    }

    analysis = {
        "entry_point": "Compromised email account used for initial access.",
        "lateral_movement": "Attacker moved laterally using obtained credentials.",
        "data_exfiltration": "Logs indicate possible data exfiltration."
    }

    recommendations = [
        "Implement multi-factor authentication for all user accounts.",
        "Conduct regular security awareness training for employees.",
        "Enhance monitoring and logging of sensitive data access."
    ]

    report_file = generate_post_mortem_report(incident, analysis, recommendations)
    print(f"Post-mortem report generated: {report_file}")