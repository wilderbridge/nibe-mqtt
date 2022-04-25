import unittest

from nibe_mqtt.config import schema

class ConfigTestCase(unittest.TestCase):
    def test_something(self):
        config = schema({
            'mqtt': {
                'host': '192.168.1.2'
            },
            'nibe': {
                'nibegw': {
                    'ip': '192.168.1.3'
                },
                'model': 'F1255'
            }
        })

        print(config)


if __name__ == '__main__':
    unittest.main()
