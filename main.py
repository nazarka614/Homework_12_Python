import os
import re
import string
from data import awards_list


main_directory = "Harry Potter"

if not os.path.exists(main_directory):
    os.mkdir(main_directory)

films_titles = {
    "results": [
        {
            "imdb_id": "tt1201607",
            "title": "Harry Potter and the Deathly Hallows: Part 2"
        },
        {
            "imdb_id": "tt0241527",
            "title": "Harry Potter and the Sorcerer's Stone"
        },
        {
            "imdb_id": "tt0926084",
            "title": "Harry Potter and the Deathly Hallows: Part 1"
        },
        {
            "imdb_id": "tt0304141",
            "title": "Harry Potter and the Prisoner of Azkaban"
        },
        {
            "imdb_id": "tt0417741",
            "title": "Harry Potter and the Half-Blood Prince"
        },
        {
            "imdb_id": "tt0295297",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "imdb_id": "tt0330373",
            "title": "Harry Potter and the Goblet of Fire"
        },
        {
            "imdb_id": "tt0373889",
            "title": "Harry Potter and the Order of the Phoenix"
        }
    ]
}

def create_alpha_folders(directory_path):
    for letter in string.ascii_uppercase:
        folder_path = os.path.join(directory_path, letter)
        os.mkdir(folder_path)

for film in films_titles["results"]:

    cleaned_title = re.sub(r'[^\w\s]', '', film["title"])

    directory_name = cleaned_title.replace(" ", "_")
    directory_path = os.path.join(main_directory, directory_name)

    if not os.path.exists(directory_path):
        os.mkdir(directory_path)

    create_alpha_folders(directory_path)

awards_data = awards_list[0]["results"]

awards_list = []

for data in awards_data:
    award_dict = {
        'award_name': data.get("award_name", ""),
        'award': data.get("award", ""),
        'type': data.get("type", "")
    }
    awards_list.append(award_dict)

print(awards_list)

sorted_awards_list = sorted(awards_list, key=lambda x: x["award_name"])

print(sorted_awards_list)

for film in films_titles["results"]:
    film_title = film["title"]

    cleaned_film_title = re.sub(r'[^\w\s]', '', film_title)
    directory_name = cleaned_film_title.replace(" ", "_")
    film_directory = os.path.join(main_directory, directory_name)

    for letter in string.ascii_uppercase:
        letter_directory = os.path.join(film_directory, letter)
        os.makedirs(letter_directory, exist_ok=True)

        for award in awards_list:
            award_name = award["award_name"]
            if award_name and award_name[0].upper() == letter:
                award_file_name = award_name + ".txt"
                award_file_path = os.path.join(letter_directory, award_file_name)

                with open(award_file_path, 'w') as award_file:
                    award_file.write(award_name)

for film in films_titles["results"]:
    film_title = film["title"]
    cleaned_film_title = re.sub(r'[^\w\s]', '', film_title)
    directory_name = cleaned_film_title.replace(" ", "_")
    film_directory = os.path.join(main_directory, directory_name)

    for letter in string.ascii_uppercase:
        letter_directory = os.path.join(film_directory, letter)

        for award in awards_list:
            award_name = award["award_name"]
            if award_name and award_name[0].upper() == letter:
                nominations = [nomination["award"] for nomination in awards_data if
                               nomination["award_name"] == award_name]

                award_file_name = award_name + ".txt"
                award_file_path = os.path.join(letter_directory, award_file_name)

                with open(award_file_path, 'w') as award_file:
                    for nomination in nominations:
                        award_file.write(nomination + "\n")