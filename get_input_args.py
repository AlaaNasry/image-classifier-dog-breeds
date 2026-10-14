#!/usr/bin/env python3
import argparse

def get_input_args():
    """Retrieve command-line arguments for the image-classification project."""
    parser = argparse.ArgumentParser(description="Classify pet images with a pretrained CNN.")
    parser.add_argument('--dir', type=str, default='pet_images/',
                        help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', choices=['resnet', 'alexnet', 'vgg'],
                        help='CNN model architecture to use')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='text file containing valid dog breed names')
    return parser.parse_args()
