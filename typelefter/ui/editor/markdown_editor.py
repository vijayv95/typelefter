from PySide6.QtWidgets import QTextEdit

class MarkdownEditor(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_file = None
        self.textChanged.connect(self.on_text_changed)
    
    def load_file(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.setPlainText(f.read())
        self.current_file = path

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(self.toPlainText())

    def on_text_changed(self):
        pass
