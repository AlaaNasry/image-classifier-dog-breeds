# Pre-trained Image Classifier for Dog Breeds

Command-line tool that classifies pet images with three pre-trained CNNs (ResNet, AlexNet, VGG), checks each prediction against the true label taken from the file name, and reports how well each model identifies **dogs vs. non-dogs** and the **correct dog breed**.

Built with Python, PyTorch and torchvision as part of the Udacity / AWS AI Programmer Nanodegree.

## Results

Run on 40 labelled pet images (30 dogs, 10 non-dogs):

| Model   | Dog / not-dog correct | Dogs identified | Breed correct | Label match | Runtime |
|---------|----------------------:|----------------:|--------------:|------------:|--------:|
| ResNet  | 97.5% (39 of 40)      | 100%            | 90.0%         | 82.5%       | 0:0:1   |
| AlexNet | 100%                  | 100%            | 80.0%         | 75.0%       | 0:0:1   |
| VGG     | 100%                  | 100%            | **93.3%**     | **87.5%**   | 0:0:8   |

- **VGG is the most accurate model** on this dataset (100% dog/not-dog, 93.3% breed accuracy), at the cost of the longest runtime.
- ResNet mistook one cat for a dog (Norwegian elkhound); AlexNet and VGG made no dog/not-dog errors.
- The most common breed errors were beagles labelled as walker hounds and Great Pyrenees labelled as kuvasz.

Full per-image output for every model is in [`results/`](results/).

### Test on extra images

Four extra images I supplied (`uploaded_images/`): two dogs, a cat and an apple.

| Image | ResNet | AlexNet | VGG |
|-------|--------|---------|-----|
| Dog_01.jpg | beagle | basset hound | beagle |
| Dog_02.jpg | beagle | beagle | beagle |
| Cat_01.jpg | Egyptian cat | tabby cat | Egyptian cat |
| Galiwa_(apple).jpg | Granny Smith | pomegranate | Granny Smith |

All three models correctly recognised the cat and the apple as not dogs. VGG and ResNet agreed on both dogs; AlexNet was inconsistent between the two. The written analysis is in [`results/uploaded_images_questions_and_answers.txt`](results/uploaded_images_questions_and_answers.txt).

## How it works

1. `get_pet_labels.py` builds the true label for each image from its file name.
2. `classify_images.py` runs the chosen CNN and records whether its label matches the true label.
3. `adjust_results4_isadog.py` compares both labels against a list of dog names (`dognames.txt`) to decide dog / not-dog.
4. `calculates_results_stats.py` computes the counts and percentages.
5. `print_results.py` prints the summary and, optionally, the misclassified images.
6. `check_images.py` ties the steps together and times the run.

## Run it

```bash
pip install -r requirements.txt

# one model
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt

# compare all three models (writes to results/)
sh run_models_batch.sh

# your own images (file names should start with the true label, e.g. Cat_01.jpg)
python check_images.py --dir uploaded_images/ --arch resnet --dogfile dognames.txt
```

Options: `--arch` accepts `resnet`, `alexnet` or `vgg`. The pre-trained weights download automatically the first time a model runs.

## Project structure

```
check_images.py                  main program
get_input_args.py                command-line arguments
get_pet_labels.py                labels from file names
classify_images.py               CNN classification and label matching
adjust_results4_isadog.py        dog / not-dog assignment
calculates_results_stats.py      accuracy statistics
print_results.py                 formatted results
classifier.py                    supplied model wrapper (Udacity)
print_functions_for_lab_checks.py, test_classifier.py   supplied check helpers (Udacity)
pet_images/                      40 labelled test images
uploaded_images/                 my extra test images
results/                         saved output for each model
```

## Credits

Project template, `classifier.py`, the check helpers and the pet image set were supplied by Udacity for the AI Programming course. The workflow functions listed above, the model comparison and the analysis are my work.
