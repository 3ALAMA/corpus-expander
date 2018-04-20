#!/usr/bin/python3
import os 
import sys 
import argparse

#####################################################
def load_NE_lists():
    ne_dict = {}
    ne_dir = './NE/'
    for filename in os.listdir(ne_dir):
        if filename.endswith(".txt"):
            # print(filename)
            ne_file = os.path.join(ne_dir, filename)
            entities = open(ne_file).read().splitlines()
            # list.Adj.txt 
            _, entity_name, ext = filename.split('.')
            ne_dict[entity_name] = entities
            print('{} loaded. NE: {}'.format(filename, entity_name))
    return ne_dict

#####################################################    
def get_more_named_entities(word, ne_dict):
    for ne_name, ne_list in ne_dict.items():
        if word in ne_list:
            return ne_list
    return None
    
#####################################################
def generate_sentences(NEs, words, index):
    gen_list = list()
    for ne in NEs:
        sen = list(words)
        sen[index] = ne
        gen_list.append(' '.join(sen))
    return gen_list
#####################################################

            

#####################################################        
parser = argparse.ArgumentParser(description='Expanding sentences in a given text corpus. The code checks for NE in sentences and create new sentences by injecting new NEs from NE list.')

parser.add_argument('-i', '--infile', type=argparse.FileType(mode='r', 
                    encoding='utf-8'), help='input file.', required=True)

parser.add_argument('-o', '--outfile', type=argparse.FileType(mode='w', 
                    encoding='utf-8'), help='out file.', required=True)
#####################################################                    
                    
                    
if __name__ == '__main__':
    args = parser.parse_args()
    ne_dict = load_NE_lists()
    input = args.infile.readlines()
    out = args.outfile
    for line in input:
        words = line.strip().split()
        for i, word in enumerate(words):
            NEs = get_more_named_entities(word, ne_dict)
            if NEs:
                new_sentences = generate_sentences(NEs, words, i)
                out.writelines('\n'.join(new_sentences))
                out.write('\n')
    print('expansion is done!')
    
    
    
    