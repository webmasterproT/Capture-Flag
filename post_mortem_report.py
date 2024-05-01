```python
import json
from datetime import datetime
from utils.constants import POST_MORTEM_TEMPLATES, USER_ACTIVITY_LOGS

class PostMortemReportGenerator:
    def __init__(self):
        self.templates = self.load_templates(POST_MORTEM_TEMPLATES)
        self.activity_logs = self.load_activity_logs(USER_ACTIVITY_LOGS)

    @staticmethod
    def load_templates(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def load_activity_logs(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def generate_report(self, incident_id, outcome, recommendations):
        template = self.templates.get('default')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        activities = self.get_activities_during_incident(incident_id)

        report = template.format(
            incident_id=incident_id,
            timestamp=timestamp,
            outcome=outcome,
            recommendations=recommendations,
            activities='\n'.join(activities)
        )

        self.save_report(incident_id, report)
        return report

    def get_activities_during_incident(self, incident_id):
        return [log for log in self.activity_logs if log['incident_id'] == incident_id]

    @staticmethod
    def save_report(incident_id, report):
        file_name = f"post_mortem_report_{incident_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        with open(file_name, 'w') as file:
            file.write(report)

# Example usage:
# generator = PostMortemReportGenerator()
# report = generator.generate_report(
#     incident_id='12345',
#     outcome='The red team successfully infiltrated the target system without detection.',
#     recommendations='Improve firewall configurations and update intrusion detection signatures.'
# )
# print(report)
```

This code snippet defines a `PostMortemReportGenerator` class that can load templates and activity logs, generate a post-mortem report based on a given incident, and save the report to a file. The example usage is commented out and can be used as a starting point to understand how the class is intended to be used.