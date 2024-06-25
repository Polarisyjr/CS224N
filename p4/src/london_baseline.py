# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    correct = 0
    total = 0
    data_path = 'birth_dev.tsv'

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    with open(data_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) > 1 and parts[1] == "London":
                correct += 1
            total += 1

    if total > 0:
        accuracy = (correct / total) * 100

    ### END YOUR CODE ###

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    print(accuracy)
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
