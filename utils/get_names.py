# python3

## create separate dataset from existing training files

import pandas as pd
import os
import shutil

file_list = pd.read_csv('train.csv')
file_list.set_index('filename', inplace=True)

original_folder = '/home/taimur/Documents/Online Courses/Fourth Brain/Week 8/Coding Assignments/train_temp/train'
folder = '/home/taimur/Documents/Online Courses/Fourth Brain/Week 8/Coding Assignments/train_temp/separated_pics'

# counters for each file type
dbr, glc, nrml, oth = 0,0,0,0

for pic in os.listdir(original_folder):
    print(pic)
    #print(file_list.loc[pic])
    max_val = 1
    labels = [i for i in file_list.loc[pic].values]

    '''commands to move files to designated folders'''
    if labels[1] == 1:
        print(file_list.loc[pic].index[1])
        dbr = dbr+1
    elif labels[2] == 1:
        print(file_list.loc[pic].index[2])
        glc = glc+1
    elif labels[6] == 1:
        print(file_list.loc[pic].index[6])
        nrml = nrml+1
    else:
        print('other')
        oth = oth+1

print('\n',dbr, 'DBR\n', glc, 'Glaucoma\n', nrml, 'Normal\n', oth, 'other\n')
