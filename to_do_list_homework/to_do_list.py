from pandas import read_json, DataFrame, to_datetime
from datetime import datetime
from json import load

my_file = read_json('categories.json')
my_categories = my_file.categories.tolist()
file_name = 'tasks.json'
date_format = "%d.%m.%Y %H:%M"


def input_category():
    inputted_category = None
    while inputted_category is None:
        category_name = input(f'introduceti numele categoriei cu litere mici:')

        if category_name in my_categories:
            inputted_category = category_name
        else:
            print('Aceasta categorie nu exista.')

    return inputted_category


def input_date():
    the_date = None

    while the_date is None:
        date_string = input('Introduceti data & ora limita a taskului:')
        try:
            converted_date = datetime.strptime(date_string, date_format)
            the_date = converted_date
        except ValueError:
            print('This is the incorrect date string format.')
    return the_date


def input_task():
    new_task = input('Introduceti task:')
    date = input_date()
    responsible_person = input('Introduceti persoana responsabila pentru task-ul mentionat:')
    category_result = input_category()

    return{
        "task": new_task,
        "date": date,
        "person": responsible_person,
        "category": category_result
    }


def check_if_over():
    user_answer = None

    while user_answer is None:
        user_answer = input('Doriti sa mai introduceti un task? (Da/Nu):')

        if user_answer == 'Da':
            return False
        elif user_answer == 'Nu':
            return True
        else:
            print('Raspuns incorect.')


tasks = []


def open_task_inputter():
    while True:
        tasks.append((input_task()))
        is_over = check_if_over()

        if is_over:
            df = DataFrame(tasks)
            df.to_json(file_name, orient="records")
            break


# load, dumbs, deschidere fisier normala

def open_task_listing():
    file = open(file_name)
    task_data = load(file)

    for task in task_data:
        category = task['category']
        date = to_datetime(task['date'], utc=True)
        person = task['person']
        task_name = task['task']
        print(f'{category} - Until {date}, {person} has to {task_name}.')


def open_menu():
    while True:
        main_options = ['input', 'output', 'sort', 'stop']
        main_option = None

        while main_option not in main_options:
            inputted_option = input('Select an option:')
            if inputted_option in main_options:
                main_option = inputted_option
            else:
                print('This is not a valid option.')

        if main_option == 'input':
            open_task_inputter()

        if main_option == 'output':
            open_task_listing()

        if main_option == 'stop':
            break


def run_app():
    open_menu()


run_app()
