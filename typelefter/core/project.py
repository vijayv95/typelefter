# -----------------------------------------------------------------------------
# Typelefter - Free and Open Source Novel Writing Application
# Copyright (C) 2025 Vijay Vasudevan, Bangalore, India
# Started: 09-10-2025
#
# This file is part of Typelefter.
#
# Typelefter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Typelefter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Typelefter.  If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------


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
