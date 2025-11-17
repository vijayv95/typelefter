import os

AUTHOR = "Vijay Vasudevan"
PRODUCT = "Typelefter"
LICENSE_URL = "https://www.gnu.org/licenses/gpl-3.0.html"
START_DATE = "09-10-2025"
PLACE = "Bangalore, India"

# Unique marker line to check if license already exists
LICENSE_MARKER = f"# {PRODUCT} - Free and Open Source Novel Writing Application"

LICENSE_HEADER = f"""# -----------------------------------------------------------------------------
# {PRODUCT} - Free and Open Source Novel Writing Application
# Copyright (C) 2025 {AUTHOR}, {PLACE}
# Started: {START_DATE}
#
# This file is part of {PRODUCT}.
#
# {PRODUCT} is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# {PRODUCT} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with {PRODUCT}.  If not, see <{LICENSE_URL}>.
# -----------------------------------------------------------------------------
"""

SUPPORTED_EXTENSIONS = (".py", ".sh", ".md", ".cpp", ".h", ".hpp")


def add_license_to_file(file_path):
    if not os.path.isfile(file_path):
        return False
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if LICENSE_MARKER in content:
        return False
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(LICENSE_HEADER + "\n\n" + content)
    print(f"License added to {file_path}")
    return True


def add_license_to_folder(folder_path):
    updated_files = 0
    for root, dirs, files in os.walk(folder_path):
        # skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for file in files:
            if file.endswith(SUPPORTED_EXTENSIONS):
                file_path = os.path.join(root, file)
                if add_license_to_file(file_path):
                    updated_files += 1
    print(f"Total files updated with license headers: {updated_files}")


def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    add_license_to_folder(os.path.join(repo_root, "..", "typelefter"))


if __name__ == "__main__":
    main()
