class CredentialManager:
    def __init__(self, config):
        self.config = config

    def get_auth_headers(self):
        """
        Returns the appropriate headers based on the authentication method.
        Supported methods:
        - basic_auth
        - bearer_token
        - api_key_header
        """
        auth_method = self.config.get("auth_method", "none").lower()
        credentials = self.config.get("credentials", {})
        headers = {}

        if auth_method == "basic_auth":
            import base64
            user = credentials.get("username", "")
            password = credentials.get("password", "")
            if user and password:
                auth_string = f"{user}:{password}"
                encoded_auth = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
                headers["Authorization"] = f"Basic {encoded_auth}"

        elif auth_method == "bearer_token":
            token = credentials.get("token", "")
            if token:
                headers["Authorization"] = f"Bearer {token}"

        elif auth_method == "api_key_header":
            header_name = credentials.get("header_name", "X-API-Key")
            api_key = credentials.get("api_key", "")
            if header_name and api_key:
                headers[header_name] = api_key

        # Extend here for OAuth2, JWT, etc.
        return headers

    def is_valid(self):
        """Quick validation to ensure required credentials are present."""
        auth_method = self.config.get("auth_method", "none").lower()
        credentials = self.config.get("credentials", {})

        if auth_method == "basic_auth":
            return all(k in credentials for k in ["username", "password"])

        if auth_method == "bearer_token":
            return "token" in credentials

        if auth_method == "api_key_header":
            return all(k in credentials for k in ["header_name", "api_key"])

        return False


if __name__ == '__main__':
    test_config = {
        "auth_method": "basic_auth",
        "credentials": {
            "username": "admin",
            "password": "secret123"
        }
    }

    manager = CredentialManager(test_config)
    print("✅ Valid config?", manager.is_valid())
    print("🔐 Headers:", manager.get_auth_headers())
