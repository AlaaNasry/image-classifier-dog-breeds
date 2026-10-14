#!/usr/bin/env python3
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """Classify each image and append classifier label and match flag."""
    for key in results_dic:
        model_label = classifier(images_dir + key, model)
        model_label = model_label.lower().strip()
        truth = results_dic[key][0]
        if truth in model_label:
            results_dic[key].extend([model_label, 1])
        else:
            results_dic[key].extend([model_label, 0])
