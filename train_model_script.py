from model import StringModel
import numpy as np
from embedding import embed_strings, get_word_embedding
import json
from tensorflow import keras
import time
'''
Creates, trains, and gives the option to save a model.

'''

def main():
    

    model = StringModel(metrics = ['accuracy', 'Recall', 'Precision', keras.metrics.Precision(thresholds=0.75,name='Precision75' ), keras.metrics.Recall(thresholds=0.75,name='Recall75' )])

    with open('parsed_data/x.txt') as file:
        x = np.array(json.load(file))
    with open('parsed_data/y.txt') as file:
        y = np.array(json.load(file))


    model.train(x[:-125], y[:-125], epochs = 8, mix_pairs = False)

    model.evaluate(x[-125:], y[-125:])

    save = input("Save model? (y/n)")

    if save == 'y':
        t = time.time()
        print('Saving as model%d' % t)
        model.save('models/model%d' % time.time())

    

    

main()