import json
import logging
from splunk.rest import BaseRestHandler
from splunk.persistconn.application import PersistentServerConnectionApplication
from splunk.persistconn.util import normalizeBoolean
from splunk.clilib.bundle_paths import make_splunkhome_path

class SetupConfigHandler(PersistentServerConnectionApplication):
    def __init__(self, command_line, command_arg):
        super().__init__()

    def handle(self, args):
        method = args.get('method')
        if method == 'POST':
            return self.handle_post(args)
        elif method == 'GET':
            return self.handle_get()
        else:
            return {'payload': 'Unsupported method', 'status': 405}

    def handle_post(self, args):
        try:
            data = json.loads(args['payload'])

            # Required fields from the wizard
            required = ['system_type', 'api_url', 'auth_method', 'username', 'password',
                        'summary_template', 'description_template', 'api_path', 'custom_headers']

            for field in required:
                if not data.get(field):
                    return {'payload': f'Missing field: {field}', 'status': 400}

            kvstore = self._get_kv_collection()
            entry = {
                '_key': 'config',
                'system': data['system_type'],
                'endpoint': data['api_url'] + data['api_path'],
                'template_name': 'default',
                'username': data['username'],
                'password': data['password'],
                'headers': data['custom_headers'],
                'summary_template': data['summary_template'],
                'description_template': data['description_template'],
                'auth_method': data['auth_method'],
            }

            kvstore.update('auto_triage_configs', 'config', entry)
            return {'payload': '✅ Configuration saved!', 'status': 200}

        except Exception as e:
            logging.exception("❌ Failed to save config")
            return {'payload': str(e), 'status': 500}

    def handle_get(self):
        try:
            kvstore = self._get_kv_collection()
            result = kvstore.get('auto_triage_configs')
            return {'payload': result, 'status': 200}
        except Exception as e:
            logging.exception("❌ Failed to retrieve config")
            return {'payload': str(e), 'status': 500}

    def _get_kv_collection(self):
        from splunk.models.base import SplunkRESTModel
        from splunk.models.field import Field

        class AutoTriageKV(SplunkRESTModel):
            resource = 'storage/collections/data/auto_triage_configs'
            system = Field()
            endpoint = Field()
            template_name = Field()

        return AutoTriageKV
