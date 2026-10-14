#!/usr/bin/env python3

def calculates_results_stats(results_dic):
    """Calculate counts and percentages for a classifier run."""
    results_stats_dic = dict()
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    for key in results_dic:
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
            if results_dic[key][2] == 1:
                results_stats_dic['n_correct_breed'] += 1
        else:
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] -
                                          results_stats_dic['n_dogs_img'])

    n_images = results_stats_dic['n_images']
    n_dogs = results_stats_dic['n_dogs_img']
    n_notdogs = results_stats_dic['n_notdogs_img']

    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / n_images * 100.0
                                      if n_images else 0.0)
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / n_dogs * 100.0
                                             if n_dogs else 0.0)
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / n_dogs * 100.0
                                              if n_dogs else 0.0)
    results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / n_notdogs * 100.0
                                                if n_notdogs else 0.0)
    return results_stats_dic
