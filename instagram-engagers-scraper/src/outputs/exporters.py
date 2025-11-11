thonimport json

class Exporter:
    def __init__(self, config):
        self.config = config
        self.output_file = self.config["output_file"]

    def export(self, data):
        with open(self.output_file, "w") as f:
            json.dump(data, f, indent=4)