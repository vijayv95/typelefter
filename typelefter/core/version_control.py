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
