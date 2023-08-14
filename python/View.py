import os
from Note import Note
from Notes import Notes
from Save_load import Save_json_file


class View:

    def __init__(self):
        self.flag = True
        self.__notes = Notes()
        self.save_load = Save_json_file("file", self.__notes)


    def greeting(self):
        print("Здравствуйте, здесь вы можете создать заметки!!!")

    def main(self):
        self.greeting()
        while (self.flag):
            self.list_of_actions()

    def list_of_actions_v2(self):
        print("Выберите действие которое хотите сделать: ")
        print("1. Создать заметку")
        print("2. Действия с заметками")
        print("3. Сохранить заметки")
        print("4. выход")
        answer = input("введите цифру команды: ")
        if (answer == "1"):
            self.create_note()
        elif (answer == "2"):
            self.note_processing()
        elif (answer == "3"):
            self.save_load.save() 
            self.list_of_actions_v2()  
        elif (answer == "4"):
            print("спасибо за использование програмой :)")
            self.flag = False
        else: 
            print("Вы ввели неверную команду")
            self.list_of_actions()

    def note_processing(self):
        print("Выберите действие которое хотите сделать: ")
        print("1. Вывести заметки")
        print("2. удалить")
        print("3. сортировки")
        print("4. сохранить")
        print("5. вернуться назад")
        print("6. выход")
        answer = input("введите цифру команды: ")
        if (answer == "1"):
            self.__notes.print()
            self.note_processing()
        elif (answer == "2"):
            if (self.remove_is_not_null()):
                self.__notes.remove()
                self.note_processing()
            else:
                print("у вас нету заметок чтобы удалть")
                self.note_processing()
        elif (answer == "3"):
            self.sorting_notes()    
        elif (answer == "4"):
            self.save_load.save()
            self.note_processing()
        elif (answer == "5"):
            self.list_of_actions_v2()    
        elif (answer == "6"):
            print("спасибо за использование програмой :)")
            self.flag = False
        else: 
            print("Вы ввели неверную команду")
            self.note_processing()

    def remove_is_not_null(self):
        if (self.__notes.lenght() == 0):
            return False
        else: return True


    def sorting_notes(self):
        print("Выберите действие которое хотите сделать: ")
        print("1. сортировка(чем новее заметка тем первее она находится)")
        print("2. сортировка(чем старее заметка тем первее она находится)")
        print("выход")
        answer = input("введите цифру команды: ")
        if (answer == "1"):
            self.__notes.sort_by_time()
            self.note_processing()
        elif (answer == "2"):
            self.__notes.sort_by_time_increase()
            self.note_processing()
        elif (answer == "3"):
            print("спасибо за использование програмой :)")
            self.flag = False   
        else: 
            print("Вы ввели неверную команду")
            self.sorting_notes()

    def list_of_actions(self):
        print("Выберите действие которое хотите сделать: ")
        print("1. Создать заметку")
        print("2. Загрузить заметки")
        print("3. выход")
        answer = input("введите цифру команды: ")
        if (answer == "1"):
            self.create_note()
        elif (answer == "2"):
            if (self.file_is_not_emty()):
                self.__notes = self.save_load.load()
                print("ваши сохранения загружены")
                self.list_of_actions_v2()
            else:
                print("Вы ничего не сохраняли")
                self.list_of_actions_v2()

        elif (answer == "3"):
            print("спасибо за использование програмой :)")
            self.flag = False
        else: 
            print("Вы ввели неверную команду")
            self.list_of_actions()

        

    def create_note(self):
        title = input("Введите заголовок заметки: ")
        text = input("Введите текст заметки: ")
        note = Note(title, text)
        print()
        print(note)
        print()
        self.question_change_note(note)

    def question_change_note(self, note): 
        print("Хотите изменить заметку?")
        print(note)
        answer = input("y - да/ n - нет: ")
        if (answer == "y"):
            self.change_note(note)
        else: 
            self.__notes.add(note)
            self.list_of_actions_v2()
            

    def change_note(self, note):
        print("Выберите действие которое хотите сделать: ")
        print("1. Заменить заголовок заметки")
        print("2. Заменить текст заметки")
        print("3. Отмена")
        print("4. Удалить заметку")

        answer = input("введите цифру команды: ")
        if (answer == "1"):
            title = input("Введите заголовок заметки: ")
            note.change_title(title)
            self.question_change_note(note)
        elif (answer == "2"):
            text = input("Введите текст заметки: ")
            note.change_text(text)
            self.question_change_note(note)
        elif (answer == "3"):
            self.__notes.add(note)
            self.__notes.print()
            self.list_of_actions_v2()
        elif (answer == "4"):
            self.list_of_actions_v2()
        else: 
            print("Вы ввели неверную команду")
            self.change_note()

    def file_is_not_emty(self):
        filename = "file.json"
        if os.stat(filename).st_size > 2:
            print ("All good")
            return True
        else:
            print ("empty file")
            return False

