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


from git import Repo, InvalidGitRepositoryError
from pathlib import Path

class GitManager:
    def __init__(self, repo_path: Path):
        try:
            self.repo = Repo(repo_path)
        except InvalidGitRepositoryError:
            self.repo = Repo.init(repo_path)

    def commit_all(self, message: str):
        self.repo.git.add(A=True)
        self.repo.index.commit(message)

    def get_status(self):
        return self.repo.git.status()
