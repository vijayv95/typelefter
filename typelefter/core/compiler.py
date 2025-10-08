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
