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
