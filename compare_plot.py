import matplotlib.pyplot as plt
import numpy as np
import sys
import glob

if __name__ == "__main__":
    filenames = glob.glob("logs/50ep_4conv_btch32_do0.3_*.txt")
    scores = {}
    for filename in filenames:
        scores[filename] = [0]
        with open(filename, 'r') as file:
            for line in file:
                tokens = line.split()
                epoch = int(tokens[0])
                f1 = float(tokens[4])
                while len(scores[filename]) < epoch:
                    scores[filename].append(scores[filename][-1])
                scores[filename][epoch-1] = f1
        if scores[filename][-1] > 0.65:
          plt.plot(np.arange(1,epoch+1), scores[filename], label=filename)
    plt.title('F1 score')
    plt.xlabel('Epochs')
    plt.ylabel('F1 score')
    plt.legend()
    plt.show()
