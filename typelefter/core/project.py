from pathlib import Path
import json

class Project:
    def __init__(self, path: Path):
        self.path = path
        self.config_file = self.path / "project.json"
        self.files = []
        self.load()

    def load(self):
        if self.config_file.exists():
            with open(self.config_file, "r") as f:
                data = json.load(f)
                self.files = [Path(p) for p in data.get("files", [])]

    def save(self):
        with open(self.config_file, "w") as f:
            json.dump({"files": [str(p) for p in self.files]}, f)

    def add_file(self, file_path: Path):
        if file_path not in self.files:
            self.files.append(file_path)
            self.save()

    def remove_file(self, file_path: Path):
        self.files = [f for f in self.files if f != file_path]
        self.save()
