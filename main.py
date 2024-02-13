import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
)
import zipfile
import os


class ArchiveApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simple Archive App")
        self.layout = QVBoxLayout()

        self.source_label = QLabel("Source Directory:")
        self.layout.addWidget(self.source_label)

        self.source_button = QPushButton("Select Source Directory")
        self.source_button.clicked.connect(self.selectSourceDirectory)
        self.layout.addWidget(self.source_button)

        self.output_label = QLabel("Output Archive Name:")
        self.layout.addWidget(self.output_label)

        self.output_button = QPushButton("Select Output Archive Name")
        self.output_button.clicked.connect(self.selectOutputDirectory)
        self.layout.addWidget(self.output_button)

        self.create_button = QPushButton("Create Archive")
        self.create_button.clicked.connect(self.createArchive)
        self.layout.addWidget(self.create_button)

        self.setLayout(self.layout)

    def selectSourceDirectory(self):
        self.source_dir = QFileDialog.getExistingDirectory(
            self, "Select Source Directory"
        )
        self.source_label.setText("Source Directory: " + self.source_dir)

    def selectOutputDirectory(self):
        self.output_filename, _ = QFileDialog.getSaveFileName(
            self, "Select Output Archive Name"
        )
        self.output_label.setText("Output Archive Name: " + self.output_filename)

    def createArchive(self):
        with zipfile.ZipFile(self.output_filename, "w") as zip_file:
            for root, dirs, files in os.walk(self.source_dir):
                for file in files:
                    zip_file.write(
                        os.path.join(root, file),
                        os.path.relpath(os.path.join(root, file), self.source_dir),
                    )


def main():
    app = QApplication(sys.argv)
    ex = ArchiveApp()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
