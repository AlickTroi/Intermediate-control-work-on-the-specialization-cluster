from Note import Note


class Notes:

    def __init__(self):
        self.__notes = []

    def add(self, note):
        self.__notes.append(note)

    def remove(self):
        count = 0
        for i in self.__notes:
            print (count, end=' | ')
            print (i)
            count += 1
        self.del_index()
        
    def del_index(self):
        index_del = input("Введите номер заметки который хотите удалить: ")
        if (index_del.isdigit()):
            index_del = int(index_del)
            if (index_del <= len(self.__notes) - 1 and int(index_del) >= 0):
                self.__notes.pop(index_del)
            else: self.del_index()
        else: self.del_index()

    def sort_by_order(self):
        self.__notes.sort(key=lambda x: x.get_text(), reverse=True)

    def sort_by_time(self):
        self.__notes.sort(key=lambda x: x.get_data(), reverse=True)

    def sort_by_order_increase(self):
        self.__notes.sort(key=lambda x: x.get_text(), reverse=False)

    def sort_by_time_increase(self):
        self.__notes.sort(key=lambda x: x.get_data(), reverse=False)

    def print(self):
        for i in self.__notes:
            print (i)

    def lenght(self):
        return len(self.__notes)

    def to_dict(self):
        state = {}
        j = 1
        for i in self.__notes:
            state[j] = i.to_dict()
            j += 1    
        return state
    