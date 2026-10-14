#!/usr/bin/env python3
from os import listdir


def get_pet_labels(image_dir):
    """Create a filename -> [pet label] dictionary from pet image filenames."""
    results_dic = dict()

    for filename in listdir(image_dir):
        # Ignore hidden files (for example .DS_Store).
        if filename.startswith('.'):
            continue

        # Remove the file extension, normalize to lowercase, and split on '_'.
        image_name = filename.rsplit('.', 1)[0].lower()

        # Keep only alphabetic words so numeric image IDs are excluded.
        pet_label = ''
        for word in image_name.split('_'):
            if word.isalpha():
                pet_label += word + ' '
        pet_label = pet_label.strip()

        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("** Warning: Key=", filename,
                  "already exists in results_dic with value=", results_dic[filename])

    return results_dic
