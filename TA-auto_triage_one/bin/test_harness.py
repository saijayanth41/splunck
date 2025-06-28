# 📁 File: bin/test_harness.py
# 🔍 Purpose: Run end-to-end test of Auto-Triage One engine

import json
import logging
from alert_orchestrator import AlertOrchestrator

# 🔧 Sample alert for testing
test_alert = {
    "alert_name": "🚨 CPU Spike Detected",
    "severity": "critical",
    "timestamp": "2025-06-21T13:30:00Z",
    "app": "infrastructure",
    "results_count": 9
}

# 🛠️ Config with mock endpoint and basic auth
test_config = {
    "system": "mockapi",
    "endpoint": "http://localhost:5000/mock/incident",
    "auth_method": "basic_auth",
    "credentials": {
        "username": "admin",
        "password": "secret123"
    },
    "template": {
        "summary": "🚨 Incident: $alert.alert_name$",
        "description": "App: $alert.app$ | Severity: $alert.severity$",
        "priority": "1"
    }
}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    orchestrator = AlertOrchestrator()

    print("🧪 Running Auto-Triage Test...")
    output = orchestrator.process_alert(test_alert, test_config)
    
    print("\n✅ TEST RESULT:")
    print(json.dumps(output, indent=4))
