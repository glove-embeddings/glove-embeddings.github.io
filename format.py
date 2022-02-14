import json
import tqdm
import string
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--which', type=str, required=True)
parser.add_argument('--amount', type=int, required=True)
args = parser.parse_args()

n_vectors = 0

with open(f'{args.which}.txt', 'r') as glove_file:
    os.makedirs(args.which, exist_ok=True)
    for line in tqdm.tqdm(glove_file):
        word, *vector = line.split()
        if not all([c in string.ascii_lowercase for c in word]):
            continue
        vector = [float(v) for v in vector]
        with open(f'{args.which}/{word}', 'w') as f:
            json.dump(vector, f)
        n_vectors += 1
        if n_vectors >= args.amount:
            break