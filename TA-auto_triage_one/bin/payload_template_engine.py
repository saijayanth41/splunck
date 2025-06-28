# 📁 File: bin/payload_template_engine.py
# 🧠 Purpose: Basic dynamic templating engine for alert payloads

import re

class PayloadTemplateEngine:
    def __init__(self):
        pass

    def render_template(self, template, alert_data, config=None):
        """
        Render a dictionary-based payload template by replacing placeholders.

        Args:
            template (dict): e.g., {"summary": "$alert.alert_name$"}
            alert_data (dict): actual values to substitute
            config (dict): optional, for later advanced use

        Returns:
            dict: rendered payload
        """
        rendered = {}

        for key, value in template.items():
            if isinstance(value, str):
                rendered[key] = self._substitute(value, alert_data)
            else:
                rendered[key] = value  # keep as-is if not a string

        return rendered

    def _substitute(self, text, alert_data):
        """
        Replace placeholders like $alert.alert_name$ with values from alert_data.
        """
        def replacer(match):
            full_key = match.group(1)
            parts = full_key.split(".")
            if parts[0] == "alert" and len(parts) > 1:
                return str(alert_data.get(parts[1], f"<missing:{parts[1]}>"))
            return f"<invalid:{full_key}>"

        return re.sub(r"\$([a-zA-Z0-9_.]+)\$", replacer, text)
