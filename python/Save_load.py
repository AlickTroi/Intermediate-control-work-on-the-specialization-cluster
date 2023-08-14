import json
from Note import Note
from Notes import Notes

class Save_json_file:
    def __init__(self, name_file, note):
        self.__name_file = name_file
        self.note = note

    def get_name_file(self):
        return self.__name_file
    
    def save(self):
        data = json.dumps(self.note.to_dict())
        data = json.loads(str(data))
        name = self.__name_file + ".json"
        with open(name, "w") as f:
            json.dump(data, f)
            
    def load(self):
        name = self.__name_file + ".json"
        with open(name, "r") as f:
            res = json.load(f)
            result_notes = self.disassembly_and_assembly(res)
            return result_notes
    
    def disassembly_and_assembly(self, result_json):
        valuesList = list(result_json.values())
        result_notes = Notes()
        for i in range(len(valuesList)):
            list_dict = list(valuesList[i].values())
            note = Note(list_dict[0], list_dict[1])
            split_data = list_dict[2].split("-")
            day = split_data[2]
            month = split_data[1]
            year = split_data[0][-2:]
            data = f"{day}-{month}-{year}"
            note.set_the_time(data)
            result_notes.add(note)
        return result_notes
