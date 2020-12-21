# python3

## create separate dataset from existing training files

import pandas as pd
import os
import shutil

file_list = pd.read_csv('train.csv')
file_list.set_index('filename', inplace=True)

original_folder = '/home/taimur/Documents/Online Courses/Fourth Brain/Week 8/Coding Assignments/train_temp/train'
folder = '/home/taimur/Documents/Online Courses/Fourth Brain/Week 8/Coding Assignments/train_temp/separated_pics'

count = 0

# index = 0
#target_folder = os.path.join(folder, 'opacity') 

# index = 1
#target_folder = os.path.join(folder, 'diabetic retinopathy')

# index = 2
#target_folder = os.path.join(folder, 'glaucoma')

# index = 3
#target_folder = os.path.join(folder, 'macular edema')

# index = 4
#target_folder = os.path.join(folder, 'macular degeneration')

# index = 5
#target_folder = os.path.join(folder, 'retinal vascular occlusion')

# index = 6
#target_folder = os.path.join(folder, 'normal')

# general folder
target_folder = os.path.join(folder, 'general')

for i in range(len(file_list)):
    max_val = file_list.iloc[i].max()
    indices = [i for i, j in enumerate(file_list.iloc[i]) if j == max_val]

    '''commands to move files to designated folders'''
    if 6 not in indices and 2 not in indices and 1 not in indices:
        count +=1
        print(file_list.iloc[i])
        shutil.copy(os.path.join(original_folder, file_list.index[i]), os.path.join(target_folder, file_list.index[i]))

print(count)
