# 📁 File: bin/universal_api_client.py
# 🧠 Purpose: Mock REST client for ticket creation

import time
import random

class UniversalAPIClient:
    def __init__(self):
        pass  # For mock version, no setup required

    def create_ticket(self, system_type, payload, config):
        """
        Simulates creating a ticket in an external system.

        Args:
            system_type (str): e.g., "servicenow", "jira"
            payload (dict): ticket content
            config (dict): endpoint and auth config

        Returns:
            dict: ticket metadata
        """
        # Simulate API delay
        time.sleep(0.3)

        # Simulate different ticket IDs per system
        ticket_id_prefix = {
            "servicenow": "INC",
            "jira": "JIRA",
            "slack": "MSG",
            "custom": "TICKET"
        }.get(system_type, "MOCK")

        return {
            "ticket_id": f"{ticket_id_prefix}-{random.randint(100000, 999999)}",
            "processing_time_ms": round(random.uniform(100, 300))
        }
