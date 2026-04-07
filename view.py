import presenter
import os

class View:
    def __init__(self):
        self.presenter = presenter.Presenter()
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_animal_menu(self, type_id):
        self.clear_screen()
        animals = self.presenter.get_animals_list_by_type(type_id)
        
        print("Этап 2: Выбор животного\n")
        for i, animal in enumerate(animals):
            print(f"{i + 1} - {animal.get_name()}")
        print("0 - Назад")
        
        while True:
            try:
                choice = int(input("\nВыберите животное: "))
            except ValueError:
                print("Нужно ввести цифру.")
                continue
                
            if choice == 0:
                return
                
            if 1 <= choice <= len(animals):
                info = self.presenter.get_animal_info(type_id, choice - 1)
                print("\n" + "="*30)
                print(info)
                print("="*30)
                input("\nНажмите Enter, чтобы продолжить...")
                return
            else:
                print("Такого животного нет.")

    def start(self): 
        while True:
            self.clear_screen()
            print("=== Zoo Helper ===")
            print("Этап 1: Выбор типа животного\n")
            print("1 - Млекопитающие")
            print("2 - Птицы")  
            print("3 - Рептилии")  
            print("0 - Выход")
            
            try:        
                choice = int(input("\nВаш выбор: "))
            except ValueError:
                print("Нужно ввести цифру.")
                input("\nНажмите Enter...")
                continue
                
            match choice:
                case 1 | 2 | 3:
                    self.show_animal_menu(choice)
                case 0:
                    print("До встречи!")
                    break
                case _:
                    print("Неверный выбор.")
                    input("\nНажмите Enter...")