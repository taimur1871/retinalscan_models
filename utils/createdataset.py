# python3

## create separate dataset from existing training files

import pandas as pd
import os
import shutil

file_list = pd.read_csv('train.csv')
file_list.set_index('filename', inplace=True)

original_folder = '/home/taimur/Documents/Online Courses/Fourth Brain/Week 8/Coding Assignments/Data/train/train'
target_folder = '/home/taimur/Documents/Online Courses/Fourth Brain/Week 8/Coding Assignments/train_temp/separated_pics/glaucoma'

#for i in range(len(file_list)):
for i in range(15, 20):
    #print(file_list.iloc[i].index[file_list.iloc[i].argmax()])
    #print(file_list.iloc[i].index[file_list.iloc[i].max()])
    #print(file_list.loc[i][1:].argmax())
    max_val = file_list.iloc[i].max()
    indices = [i for i, j in enumerate(file_list.iloc[i]) if j == max_val]
    #for j in range(len(indices)):
        #print(indices[j])
    #print(file_list.iloc[i])
    #print(file_list.loc[i]['filename'])

    '''commands to move files to designated folders'''
    #if (len(indices) == 1 and indices[0] == 0):
        #shutil.copy(os.path.join(original_folder, file_list.index[i]),
                    #os.path.join(target_folder, file_list.index[i]))
