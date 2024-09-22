import requests
import time

def make_request_with_timeout(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.text
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")