import datetime

class Note:
    
    def __init__(self, title, text):
        self.__title = title
        self.__text = text
        self.__data = datetime.date.today()

    

    def get_title(self):
        return self.__title
    
    def __set_title(self, str):
        self.__title = str

    def get_text(self):
        return self.__text
    
    def __set_text(self, str):
        self.__text = str

    def get_data(self):
        return self.__data
    
    def __set_data(self):
        self.__data = datetime.date.today()

    def set_the_time(self, data):
        self.__data = datetime.datetime.strptime(data, '%d-%m-%y').date()

    def change(self, title, text):
        self.__set_title(title)
        self.__set_text(text)
        self.__set_data()

    def change_title(self, title):
        self.__set_title(title)

    def change_text(self, text):
        self.__set_text(text)


    def __str__(self):
        return(f"Заголовок: {self.__title}, " + f"Текст: {self.__text}, " + f"Дата: {str(self.__data)}")
    
    def __repr__(self):
        return str(self)
    
    def __getstate__(self) -> dict: 
        state = {}
        state["text"] = self.__text
        state["data"] = self.__data
        return state

    def __setstate__(self, state: dict):
        self.__text = state["text"]
        self.__data = state["data"]

    def to_dict(self):
        state = {}
        state["title"] = self.__title
        state["text"] = self.__text
        state["data"] = str(self.__data)
        return state