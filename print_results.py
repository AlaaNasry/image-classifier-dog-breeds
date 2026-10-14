#!/usr/bin/env python3


def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """Print summary results and optionally print misclassified images."""
    print("\n\n*** Results Summary for CNN Model Architecture",
          model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images',
                                results_stats_dic['n_notdogs_img']))

    print(" ")
    for key in results_stats_dic:
        if key.startswith('p'):
            print("{:20}: {:5.1f}".format(key, results_stats_dic[key]))

    # Print images whose dog/non-dog status was misclassified.
    if (print_incorrect_dogs and
            (results_stats_dic['n_correct_dogs'] +
             results_stats_dic['n_correct_notdogs'] !=
             results_stats_dic['n_images'])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print("Real: {:>26}   Classifier: {:>30}".format(
                    results_dic[key][0], results_dic[key][1]))

    # Print dog images where the classifier got the dog category correct
    # but selected the wrong breed.
    if (print_incorrect_breed and
            results_stats_dic['n_correct_dogs'] !=
            results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Real: {:>26}   Classifier: {:>30}".format(
                    results_dic[key][0], results_dic[key][1]))
