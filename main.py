from text_cleaner import text_cleaner
import argparse
from Byte_Pair_Tokenizer import tokenize
import os

def main(fileName, merges):

    file = open(fileName, 'r')
    text = file.read()
    tokens = tokenize(text, merges)
    print(f"text length = {len(text)}, pair length = {len(tokens)}")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fileName', type=str, help='The file to be cleaned')
    parser.add_argument('merges', type=int, help='number of merge operations')
    args = parser.parse_args()
    main(args.fileName, args.merges)
