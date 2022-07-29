"""
Файл содержит функции, необходимые для полноценного функционирования приложения
"""

from PyQt5 import QtWidgets, Qt


def save_current_file(self):
    """
    Функция сохраняет файл
    Автор: Савастьянова А.В.
    Вход: текст в редакторе
    Выход: файл
    """
    filename = QtWidgets.QFileDialog.getSaveFileName(self)[0]
    file = open(filename, 'w+')
    text = self.text_edit.toPlainText()
    file.write(text)
    file.close()


def open_file(self):
    """
    Функция открывает файл
    Автор: Савастьянова А.В.
    Вход: отстутствует
    Выход: содержимое файла
    """
    filename = QtWidgets.QFileDialog.getOpenFileName(self)[0]
    try:
        file = open(filename, 'r')
        with file:
            data = file.read()
            self.text_edit.setText(data)
        file.close()
    except FileNotFoundError:
        print("No such file")
        messagebox = QtWidgets.QMessageBox()
        messagebox.setWindowTitle("Invalid file")
        messagebox.setText("Selected filename is not valid or file was not selected.\n"
                           "Please select a valid file.")
        messagebox.exec()


def save_as_txt(self):
    """
    Функция сохраняет файл в txt формате
    Автор: Савастьянова А.В.
    Вход: текст в редакторе
    Выход: файл в txt формате
    """
    filename = QtWidgets.QFileDialog.getSaveFileName(self, filter='*.txt')[0]
    file = open(filename, 'w')
    text = self.text_edit.toPlainText()
    file.write(text)
    file.close()


def save_as_pdf(self):
    """
    Функция сохраняет файл в pdf формате
    Автор: Савастьянова А.В.
    Вход: текст в редакторе
    Выход: файл в pdf формате
    """
    filename = QtWidgets.QFileDialog.getSaveFileName(self, filter='*.pdf')[0]
    print_pdf = Qt.QPrinter()
    print_pdf.setOutputFormat(Qt.QPrinter.OutputFormat.PdfFormat)
    print_pdf.setOutputFileName(filename)
    self.text_edit.print_(print_pdf)


def change_font(self):
    """
    Функция вызывает окно выбора стиля шрифта, изменяет выделенный текст/задает новый шрифт
    Автор: Савастьянова А.В.
    Вход: выделенный текст
    Выход: измененный текст/установка нового шрифта
    """
    font, b_ok = QtWidgets.QFontDialog.getFont()
    print(font, b_ok)

    if b_ok:
        self.text_edit.setFontFamily(font.family())
        self.text_edit.setFontWeight(font.weight())
        self.text_edit.setFontItalic(font.italic())
        self.text_edit.setFontPointSize(font.pointSize())
        self.text_edit.setFontUnderline(font.underline())


def change_colour(self):
    """
    Функция вызывает окно выбора цвета текста, изменяет выделенный текст
    Автор: Омаров М.Т.
    Вход: выделенный текст
    Выход: измененный текст
    """
    colour = QtWidgets.QColorDialog.getColor()
    print(colour)
    self.text_edit.setTextColor(colour)
