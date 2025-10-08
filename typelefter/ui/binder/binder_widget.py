from PySide6.QtWidgets import QWidget, QVBoxLayout, QTreeView, QFileSystemModel
from PySide6.QtCore import Signal
from pathlib import Path

class BinderWidget(QWidget):
    file_selected = Signal(str)  # emits full path of clicked file

    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.project = project

        layout = QVBoxLayout()
        self.tree = QTreeView()
        layout.addWidget(self.tree)
        self.setLayout(layout)

        self.model = QFileSystemModel()
        self.model.setRootPath(str(project.path))
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(str(project.path)))
        self.tree.setHeaderHidden(True)

        self.tree.clicked.connect(self.on_tree_clicked)

    def on_tree_clicked(self, index):
        file_path = self.model.filePath(index)
        if Path(file_path).is_file():
            self.file_selected.emit(file_path)
