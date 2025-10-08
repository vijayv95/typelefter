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


from PySide6.QtWidgets import QMainWindow, QSplitter, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from typelefter.ui.editor.markdown_editor import MarkdownEditor
from typelefter.ui.binder.binder_widget import BinderWidget
from typelefter.core.project import Project
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Typelefter")

        self.project = Project(Path("my_first_project"))

        splitter = QSplitter(Qt.Horizontal)
        self.binder = BinderWidget(self.project)
        self.editor = MarkdownEditor()
        splitter.addWidget(self.binder)
        splitter.addWidget(self.editor)
        splitter.setStretchFactor(1, 1)
        self.setCentralWidget(splitter)

        # Connect binder signal to editor
        self.binder.file_selected.connect(self.editor.load_file)

        # --- Toolbar with Save ---
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.editor.save_file)
        toolbar.addAction(save_action)
