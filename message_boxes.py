from PySide6.QtWidgets import QMessageBox


def info_box(parent, title: str, text: str):
    info_message = QMessageBox()
    info_message.setWindowTitle(title)
    info_message.setInformativeText(text)
    info_message.setParent(parent)
    info_message.show()
