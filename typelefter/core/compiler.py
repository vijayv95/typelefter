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


import subprocess
from pathlib import Path

class Compiler:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir

    def compile_markdown(self, markdown_files: list[Path], output_file: str):
        cmd = [
            "pandoc",
            *map(str, markdown_files),
            "-o",
            str(self.output_dir / output_file)
        ]
        subprocess.run(cmd, check=True)
