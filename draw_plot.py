import matplotlib.pyplot as plt
import numpy as np
import sys

if __name__ == "__main__":
    train_losses = [0]
    valid_losses = [0]
    train_score = [0]
    valid_score = [0]
    lastEpoch = -1
    for idx,filename in enumerate(sys.argv):
        if idx == 0:
            continue
        with open(filename, 'r') as file:
            for line in file:
                tokens = line.split()
                epoch = int(tokens[0])
                train_loss = float(tokens[1])
                train_f1 = float(tokens[2])
                valid_loss = float(tokens[3])
                valid_f1 = float(tokens[4])
                if lastEpoch < 0:
                    startEpoch = epoch
                while len(train_losses) < epoch:
                    train_losses.append(train_losses[-1])
                    valid_losses.append(valid_losses[-1])
                    train_score.append(train_score[-1])
                    valid_score.append(valid_score[-1])
                train_losses[epoch-1] = train_loss
                valid_losses[epoch-1] = valid_loss
                train_score[epoch-1] = train_f1
                valid_score[epoch-1] = valid_f1
                lastEpoch = epoch
    endEpoch = lastEpoch
    plt.plot(np.arange(startEpoch,endEpoch+1), train_losses, label='Training loss')
    plt.plot(np.arange(startEpoch,endEpoch+1), valid_losses, label='Validation loss')
    plt.title('Losses')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
    
    plt.plot(np.arange(startEpoch,endEpoch+1), train_score, label='Training F1 score')
    plt.plot(np.arange(startEpoch,endEpoch+1), valid_score, label='Validation F1 score')
    plt.title('F1 score')
    plt.xlabel('Epochs')
    plt.ylabel('F1 score')
    plt.legend()
    plt.show()