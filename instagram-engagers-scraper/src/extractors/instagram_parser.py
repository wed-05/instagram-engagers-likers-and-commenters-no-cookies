thonimport requests
import json

class InstagramParser:
    def __init__(self, config):
        self.config = config
        self.api_url = self.config["api_url"]

    def fetch_data(self):
        data = []
        for post_url in self.config["post_urls"]:
            response = requests.get(f"{self.api_url}/{post_url}")
            if response.status_code == 200:
                data.append(response.json())
        return data