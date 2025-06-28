# 📁 File: bin/config_validator.py
# 🛠️ Purpose: Validate incoming configuration for completeness and correctness

class ConfigValidator:
    REQUIRED_FIELDS = ["system", "endpoint", "credentials"]

    def validate(self, config):
        """Validates that required config fields exist and are non-empty."""
        missing = [field for field in self.REQUIRED_FIELDS if field not in config or not config[field]]
        if missing:
            raise ValueError(f"❌ Missing required configuration field(s): {', '.join(missing)}")

        # Check nested credentials
        if "credentials" in config:
            creds = config["credentials"]
            if not isinstance(creds, dict) or not creds.get("username") or not creds.get("password"):
                raise ValueError("❌ Invalid credentials format. Expected fields: username, password")

        return True

if __name__ == '__main__':
    validator = ConfigValidator()

    valid_config = {
        "system": "servicenow",
        "endpoint": "https://example.com/api",
        "credentials": {"username": "admin", "password": "pass"}
    }

    try:
        assert validator.validate(valid_config)
        print("✅ Config validation passed")
    except Exception as e:
        print(f"❌ Validation error: {e}")
