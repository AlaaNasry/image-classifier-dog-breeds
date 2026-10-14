#!/bin/sh
# Runs all three CNN architectures on the images in uploaded_images/ and saves the output.
# Usage: sh run_models_batch_uploaded.sh
mkdir -p results
python check_images.py --dir uploaded_images/ --arch resnet  --dogfile dognames.txt > results/resnet_uploaded_images.txt
python check_images.py --dir uploaded_images/ --arch alexnet --dogfile dognames.txt > results/alexnet_uploaded_images.txt
python check_images.py --dir uploaded_images/ --arch vgg     --dogfile dognames.txt > results/vgg_uploaded_images.txt
