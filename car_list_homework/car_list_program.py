import pandas as pd
from os import path, mkdir
import shutil
from json import dump

input_file_name = "input.csv"
output_folder = "output_data"


def create_folder():
    if path.exists(f'./{output_folder}/'):
        shutil.rmtree(f'./{output_folder}/')

    mkdir(f'./{output_folder}')
    print("Directory ", output_folder, " successful created.")


def convert_from_df_to_dictionary(data_frame):
    list = []
    for entry in data_frame.to_dict('records'):
        list.append(entry)
    return list


def create_and_write_to_json_file(file_name, car_list):
    with open(file_name, 'w') as file:
        dump(car_list, file)


def generate_slow_cars_file(data_frame):
    slow_cars = data_frame[data_frame.hp < 120]
    slow_car_list = convert_from_df_to_dictionary(slow_cars)

    create_and_write_to_json_file(f'{output_folder}/slow_cars.json', slow_car_list)


def generate_fast_cars_file(data_frame):
    fast_cars = data_frame[(data_frame.hp > 120) & (data_frame.hp < 180)]
    fast_car_list = convert_from_df_to_dictionary(fast_cars)

    create_and_write_to_json_file(f'{output_folder}/fast_cars.json', fast_car_list)


def generate_sport_cars_file(data_frame):
    sport_cars = data_frame[data_frame.hp > 180]
    sport_car_list = convert_from_df_to_dictionary(sport_cars)

    create_and_write_to_json_file(f'{output_folder}/sport_cars.json', sport_car_list)


def generate_cheap_cars_file(data_frame):
    cheap_cars = data_frame[data_frame.price < 1000]
    cheap_car_list = convert_from_df_to_dictionary(cheap_cars)

    create_and_write_to_json_file(f'{output_folder}/cheap_cars.json', cheap_car_list)


def generate_medium_cars_file(data_frame):
    medium_cars = data_frame[(data_frame.price >= 1000) & (data_frame.price < 5000)]
    medium_car_list = convert_from_df_to_dictionary(medium_cars)

    create_and_write_to_json_file(f'{output_folder}/medium_cars.json', medium_car_list)


def generate_expensive_cars_file(data_frame):
    expensive_cars = data_frame[data_frame.price >= 5000]
    expensive_car_list = convert_from_df_to_dictionary(expensive_cars)

    create_and_write_to_json_file(f'{output_folder}/expensive_cars.json', expensive_car_list)


def remove_duplicates_from_list(the_list):
    return list(dict.fromkeys(the_list))


def create_files_by_car_brands(data_frame):
    brand_list = remove_duplicates_from_list(data_frame.brand)
    print(brand_list)

    for brand in brand_list:
        filtered_data_frame = data_frame[data_frame.brand == brand]
        car_list = convert_from_df_to_dictionary(filtered_data_frame)
        create_and_write_to_json_file(f'{output_folder}/{brand}.json', car_list)


def generate_files():
    df = pd.read_csv(input_file_name)
    df = pd.DataFrame(df)

    generate_slow_cars_file(df)
    generate_fast_cars_file(df)
    generate_sport_cars_file(df)
    generate_cheap_cars_file(df)
    generate_medium_cars_file(df)
    generate_expensive_cars_file(df)

    create_files_by_car_brands(df)
    print('done')


def car_app():
    create_folder()
    generate_files()


car_app()
