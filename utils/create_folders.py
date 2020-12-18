# python3

## create separate dataset from existing training files

import pandas as pd
import os
import shutil

file_list = pd.read_csv('train.csv')
file_list.set_index('filename', inplace=True)

target_folder = '/home/taimur/Documents/Online Courses/Fourth Brain/Week 8/Coding Assignments/train_temp/separated_pics'

for i in file_list.columns:
    print(i)
    
    '''commands to create new folders'''
    try:
        os.mkdir(os.path.join(target_folder, i))
    except:
        continue
