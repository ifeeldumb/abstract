import model

class Presenter:
    def __init__(self):
        self.db = model.animals_db
        
    def get_animals_list_by_type(self, type_id):
        if type_id in self.db:
            return self.db[type_id]
        return []

    def get_animal_info(self, type_id, animal_index):
        try:
            animal = self.db[type_id][animal_index]
            return f"{animal.get_name()} ({animal.get_type()}) — возраст {animal.get_age()} лет"
        except (KeyError, IndexError):
            return "Ошибка: данные не найдены."