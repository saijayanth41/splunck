# 📁 File: bin/metrics_collector.py
# 📊 Purpose: Collect performance and failure metrics for Auto-Triage One

import time
import json
import logging
import os

class MetricsCollector:
    def __init__(self, log_file='metrics_log.json'):
        self.log_file = os.path.join(os.path.dirname(__file__), log_file)
        logging.basicConfig(level=logging.INFO)

    def record(self, alert_data, result, config):
        """Record a successful alert processing run."""
        metrics = {
            "timestamp": int(time.time()),
            "status": "success",
            "alert_name": alert_data.get("alert_name"),
            "app": alert_data.get("app"),
            "severity": alert_data.get("severity"),
            "ticket_id": result.get("ticket_id"),
            "processing_time_ms": result.get("processing_time_ms"),
            "retries": result.get("retry_attempts", 0),
            "system": config.get("system")
        }
        self._append(metrics)

    def record_failure(self, alert_data, result, config):
        """Record a failed alert processing run."""
        metrics = {
            "timestamp": int(time.time()),
            "status": "failure",
            "alert_name": alert_data.get("alert_name"),
            "app": alert_data.get("app"),
            "severity": alert_data.get("severity"),
            "errors": result.get("errors"),
            "stack_trace": result.get("stack_trace"),
            "system": config.get("system")
        }
        self._append(metrics)

    def _append(self, data):
        """Append data to a local JSON lines file."""
        try:
            with open(self.log_file, "a") as f:
                f.write(json.dumps(data) + "\n")
        except Exception as e:
            logging.error(f"❌ Failed to write metrics: {str(e)}")
