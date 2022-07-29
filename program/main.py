"""
Проект выполнен учениками 2-ого курса ИВТ, группы Бив-203
Омаровым Маратом Тимуровичем и Савастьяновой Александрой Владимировной
"""

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import commands_lib


class Window(QtWidgets.QMainWindow):
    """
    Класс содержит в себе методы, позволяющие запуститься и полностью функционировать приложению
    Автор: Омаров М.Т.
    Вход: класс главного окна из библиотеки pyqt5
    Выход: приложение
    """
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("TextEditor")
        self.setGeometry(600, 340, 650, 400)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.document = self.text_edit.document()
        self.cursor = QtGui.QTextCursor(self.document)

        self.open_new_file_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+O'), self)
        self.open_new_file_shortcut.activated.connect(self.shortcut_open)

        self.save_current_file_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+S'), self)
        self.save_current_file_shortcut.activated.connect(self.shortcut_save)

        self.save_current_file_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+B'), self)
        self.save_current_file_shortcut.activated.connect(self.shortcut_bold)

        self.save_current_file_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+I'), self)
        self.save_current_file_shortcut.activated.connect(self.shortcut_italic)

        self.save_current_file_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+U'), self)
        self.save_current_file_shortcut.activated.connect(self.shortcut_underline)

        self.create_menu_bar()

    def shortcut_save(self):
        """
        Функция обрабатывает нажатие "горячей клавиши": вызывает функцию сохранения файла
        Автор: Омаров М.Т.
        Вход:
        Выход: отсутствует
        """
        commands_lib.save_current_file(self)

    def shortcut_open(self):
        """
        Функция обрабатывает нажатие "горячей клавиши": вызывает функцию открытия файла
        Автор: Омаров М.Т.
        Вход:
        Выход: отсутствует
        """
        commands_lib.open_file(self)

    def shortcut_bold(self):
        """
        Функция обрабатывает нажатие "горячей клавиши": делает выделенный фрагмент текста "жирным"
        Автор: Омаров М.Т.
        Вход: выделенный текст
        Выход: измененный текст
        """
        self.text_edit.setFontWeight(QtGui.QFont.Bold)

    def shortcut_italic(self):
        """
        Функция обрабатывает нажатие "горячей клавиши": делает выделенный фрагмент текста "курсивом"
        Автор: Омаров М.Т.
        Вход: выделенный текст
        Выход: измененный текст
        """
        self.text_edit.setFontItalic(True)

    def shortcut_underline(self):
        '''
        Функция обрабатывает нажатие "горячей клавиши": подчеркивает выделенный фрагмент текста
        Автор: Омаров М.Т.
        Вход: выделенный текст
        Выход: измененный текст
        '''
        self.text_edit.setFontUnderline(True)

    def closeEvent(self, event):
        """
        Функция обрабатывает закрытие приложения
        Автор: Омаров М.Т.
        Вход: сигнал о закрытие приложения
        Выход: информационное окно
        """
        messagebox = QtWidgets.QMessageBox()
        title = "Quit Application?"
        message = "If you quit without saving, any changes made to the file will be lost.\n" \
                  "Save file before quitting?"
        reply = messagebox.question(self, title, message, messagebox.Yes | messagebox.No |
                                    messagebox.Cancel, messagebox.Cancel)
        if reply == messagebox.Yes:
            commands_lib.save_current_file(self)
        elif reply == messagebox.No:
            event.accept()
        else:
            event.ignore()

    def create_menu_bar(self):
        """
        Функция отрисовывает выпадающие списки и кпонки верхней панели (меню)
        Автор: Омаров М.Т.
        Вход: отсутствует
        Выход: отсутствует
        """
        self.menubar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menubar)

        filemenu = QtWidgets.QMenu("&File", self)
        self.menubar.addMenu(filemenu)
        filemenu.addAction('Open', self.action_clicked)
        filemenu.addAction('Save', self.action_clicked)

        align = QtWidgets.QMenu("&Align", self)
        self.menubar.addMenu(align)
        align.addAction('Left', self.action_align)
        align.addAction('Center', self.action_align)
        align.addAction('Right', self.action_align)
        
        font_style = QtWidgets.QMenu("&Style", self)
        self.menubar.addMenu(font_style)
        font_style.addAction('Change', self.action_font)

        text_colour = QtWidgets.QMenu("&Colour", self)
        self.menubar.addMenu(text_colour)
        text_colour.addAction('Change', self.action_colour)

        save_as = filemenu.addMenu("&Save as...")
        save_as.addAction('Save as txt', self.action_save_as)
        save_as.addAction('Save as PDF', self.action_save_as)

    @QtCore.pyqtSlot()
    def action_align(self):
        """
        Функция обрабатывает нажатия на кнопки, отвечающие за расположение текста на листе,
        и вызывает соответствующие команды
        Автор: Савастьянова А.В.
        Вход: сигнал о нажатии
        Выход: отсутствует
        """
        action = self.sender()
        if action.text() == "Left":
            print("Left")
        elif action.text() == "Center":
            print("Center")
        elif action.text() == "Right":
            print("Right")

    def action_colour(self):
        """
        Функция обрабатывает нажатие на кнопку (Colour), отвечающую за изменение цвета текста,
        и вызывает соответствующие команды
        Автор: Омаров М.Т.
        Вход: сигнал о нажатии
        Выход: отсутствует
        """
        commands_lib.change_colour(self)

    def action_clicked(self):
        """
        Функция обрабатывает нажатия на кнопки,
        отвечающие за открытие и сохранение файлов на устройстве,
        и вызывает соответствующие команды
        Автор: Савастьянова А.В.
        Вход: сигнал о нажатии
        Выход: отсутствует
        """
        action = self.sender()
        if action.text() == "Open":
            commands_lib.open_file(self)
        elif action.text() == "Save":
            commands_lib.save_current_file(self)

    def action_save_as(self):
        """
        Функция обрабатывает нажатия на кнопки,
        отвечающие за сохранение файлов на устройстве в определенном формате,
        и вызывает соответствующие команды
        Автор: Савастьянова А.В.
        Вход: сигнал о нажатии
        Выход: отсутствует
        """
        action = self.sender()
        if action.text() == "Save as txt":
            commands_lib.save_as_txt(self)
        elif action.text() == "Save as PDF":
            commands_lib.save_as_pdf(self)

    def action_font(self):
        """
        Функция обрабатывает нажатие на кнопку (Font Style), отвечающую за изменение стиля текста,
        и вызывает соответствующие команды
        Автор: Савастьянова А.В.
        Вход: сигнал о нажатии
        Выход: отсутствует
        """
        commands_lib.change_font(self)


def application():
    """
    Функция запускает полностью отрисовывает приложение
    Автор: Омаров М.Т.
    Вход: сигнал о нажатии
    Выход: отсутствует
    """
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()   # запуск приложения
