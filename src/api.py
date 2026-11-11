import requests

import config


def post(data):
    response = requests.post(
        config.API_URL,
        json=data,
        headers={config.API_KEY_HEADER: config.API_KEY},
    )
    try:
        return response.status_code
    finally:
        response.close()
