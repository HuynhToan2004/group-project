"""
    Required functions for scraping dishes.
"""

import os
import json as js

def dump_links_json(links):
    """
    Scrape links and save them to a JSON file.
    """
    data = {"link": links}
    file_path = os.path.join('./group-project', 'links.json')
    with open(file_path, 'w', encoding='utf-8') as json_file:
        js.dump(data, json_file, ensure_ascii=False, indent=4)

def dump_dish_json(title, ingredients, quantities):
    """
    Scrape dish data and save them to a JSON file
    """
    dish_data = {}
    for i in ingredients.index:
        dish_data[ingredients[i]] = quantities[i]
    data = {title: dish_data}
    file_path = os.path.join('./group-project', 'dishes.json')
    with open(file_path, 'a', encoding='utf-8') as json_file:
        js.dump(data, json_file, ensure_ascii=False, indent=4)
