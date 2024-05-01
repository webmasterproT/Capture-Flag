```python
import unittest
from forensics import ForensicAnalyzer
from data.forensic_artifacts import forensic_artifacts

class TestForensicAnalysis(unittest.TestCase):
    def setUp(self):
        self.analyzer = ForensicAnalyzer(api_key=API_KEY)

    def test_log_file_analysis(self):
        for artifact in forensic_artifacts:
            with self.subTest(artifact=artifact):
                result = self.analyzer.analyze_log_file(artifact['log_file'])
                self.assertEqual(result, artifact['expected_result'], f"Failed to analyze {artifact['log_file']}")

    def test_packet_capture_analysis(self):
        for artifact in forensic_artifacts:
            with self.subTest(artifact=artifact):
                result = self.analyzer.analyze_packet_capture(artifact['packet_capture'])
                self.assertEqual(result, artifact['expected_result'], f"Failed to analyze {artifact['packet_capture']}")

    def test_system_integrity_check(self):
        for check in SYSTEM_INTEGRITY_CHECKS:
            with self.subTest(check=check):
                result = self.analyzer.check_system_integrity(check['system_snapshot'])
                self.assertTrue(result['is_intact'], f"Integrity check failed for {check['system_snapshot']}")

    def test_forensic_investigation_report_generation(self):
        for report in forensic_artifacts:
            with self.subTest(report=report):
                result = self.analyzer.generate_investigation_report(report['evidence'])
                self.assertIn('report_id', result, "Report generation failed, no report_id found.")
                self.assertIn('findings', result, "Report generation failed, no findings found.")

if __name__ == '__main__':
    unittest.main()
```