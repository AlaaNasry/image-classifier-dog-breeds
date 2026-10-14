#!/bin/sh
# Runs all three CNN architectures on the 40 labelled pet images and saves the output.
# Usage: sh run_models_batch.sh
mkdir -p results
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > results/resnet_pet_images.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > results/alexnet_pet_images.txt
python check_images.py --dir pet_images/ --arch vgg     --dogfile dognames.txt > results/vgg_pet_images.txt
