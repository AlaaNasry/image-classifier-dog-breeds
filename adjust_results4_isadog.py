#!/usr/bin/env python3

def adjust_results4_isadog(results_dic, dogfile):
    """Append flags indicating whether the true and classifier labels are dogs."""
    dognames_dic = dict()
    with open(dogfile, 'r') as infile:
        for line in infile:
            dogname = line.rstrip()
            if dogname in dognames_dic:
                print("** Warning: Duplicate dog name found in dognames.txt:", dogname)
            else:
                dognames_dic[dogname] = 1

    for key in results_dic:
        pet_is_dog = 1 if results_dic[key][0] in dognames_dic else 0
        classifier_is_dog = 1 if results_dic[key][1] in dognames_dic else 0
        results_dic[key].extend([pet_is_dog, classifier_is_dog])
