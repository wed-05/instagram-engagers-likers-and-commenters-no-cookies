thonimport requests
import json
from extractors.instagram_parser import InstagramParser
from outputs.exporters import Exporter

class Runner:
    def __init__(self, config):
        self.config = config
        self.parser = InstagramParser(config)
        self.exporter = Exporter(config)

    def run(self):
        posts = self.parser.fetch_data()
        self.exporter.export(posts)

if __name__ == "__main__":
    with open("config/settings.example.json") as f:
        config = json.load(f)

    runner = Runner(config)
    runner.run()