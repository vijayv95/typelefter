#!/usr/bin/env python3# -----------------------------------------------------------------------------
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
# along with Typelefter.  If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
# -----------------------------------------------------------------------------


import os
import sys

AUTHOR = "Vijay Vasudevan"
PRODUCT = "Typelefter"
LICENSE_URL = "https://www.gnu.org/licenses/gpl-3.0.html"
START_DATE = "09-10-2025"
PLACE = "Bangalore, India"

LICENSE_MARKER = f"# {PRODUCT} - Free and Open Source Novel Writing Application"

LICENSE_HEADER = (
    "# -----------------------------------------------------------------------------\n"
    f"# {PRODUCT} - Free and Open Source Novel Writing Application\n"
    f"# Copyright (C) 2025 {AUTHOR}, {PLACE}\n"
    f"# Started: {START_DATE}\n"
    "#\n"
    f"# This file is part of {PRODUCT}.\n"
    "#\n"
    f"# {PRODUCT} is free software: you can redistribute it and/or modify\n"
    "# it under the terms of the GNU General Public License as published by\n"
    "# the Free Software Foundation, either version 3 of the License, or\n"
    "# (at your option) any later version.\n"
    "#\n"
    f"# {PRODUCT} is distributed in the hope that it will be useful,\n"
    "# but WITHOUT ANY WARRANTY; without even the implied warranty of\n"
    "# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n"
    "# GNU General Public License for more details.\n"
    "#\n"
    "# You should have received a copy of the GNU General Public License\n"
    f"# along with {PRODUCT}.  If not, see <{LICENSE_URL}>.\n"
    "# -----------------------------------------------------------------------------\n"
)

SUPPORTED_EXTENSIONS = (
    ".py",
    ".sh",
    ".md",
    ".cpp",
    ".h",
    ".hpp",
)


def add_license_to_file(file_path: str) -> bool:
    if not os.path.isfile(file_path):
        return False

    if not file_path.endswith(SUPPORTED_EXTENSIONS):
        return False

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return False

    if LICENSE_MARKER in content:
        return False

    new_content = LICENSE_HEADER + "\n" + content

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"License added: {file_path}")
    return True


def main():
    file_paths = sys.argv[1:]

    if not file_paths:
        print("No files provided.")
        return 0

    for path in file_paths:
        add_license_to_file(path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
