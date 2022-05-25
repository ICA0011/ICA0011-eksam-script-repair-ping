import requests

def check_server_status(url):
    """Method for checking if server is up and running."""
    a = requests.get(url)
    return a.status_code
